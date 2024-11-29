import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from datetime import datetime, timedelta
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from concurrent.futures import ThreadPoolExecutor
import statsmodels.api as sm
from pytrends.request import TrendReq
import warnings

warnings.filterwarnings('ignore')
nltk.download('vader_lexicon', quiet=True)

class OmniMarketSeerV2:
    def __init__(self, symbols, start_date=None, end_date=None):
        self.symbols = symbols if isinstance(symbols, list) else [symbols]
        self.start_date = start_date or (datetime.now() - timedelta(days=365*5)).strftime('%Y-%m-%d')
        self.end_date = end_date or datetime.now().strftime('%Y-%m-%d')
        self.data = {}
        self.models = {}
        self.sia = SentimentIntensityAnalyzer()
        self.pytrends = TrendReq(hl='en-US', tz=360)

    def fetch_stock_data(self):
        with ThreadPoolExecutor() as executor:
            self.data = {symbol: yf.download(symbol, start=self.start_date, end=self.end_date) 
                         for symbol in executor.map(lambda s: s, self.symbols)}

    def fetch_news_sentiment(self, symbol):
        url = f"https://finviz.com/quote.ashx?t={symbol}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        news_table = soup.find(id='news-table')
        if news_table is None:
            print(f"No news data found for {symbol}. The website structure might have changed.")
            return pd.DataFrame()

        parsed_news = []
        for row in news_table.findAll('tr'):
            title = row.a.text if row.a else "No title"
            date_data = row.td.text.split(' ') if row.td else ["", ""]
            date = date_data[0] if len(date_data) > 1 else ""
            time = date_data[1] if len(date_data) > 1 else date_data[0]
            parsed_news.append([date, time, title])

        df = pd.DataFrame(parsed_news, columns=['date', 'time', 'title'])
        df['sentiment'] = df['title'].apply(lambda x: self.sia.polarity_scores(x)['compound'])
        return df

    def prepare_data(self, symbol):
        df = self.data[symbol].copy()
        df['Returns'] = df['Close'].pct_change()
        df['MA50'] = df['Close'].rolling(window=50).mean()
        df['MA200'] = df['Close'].rolling(window=200).mean()
        df['Volatility'] = df['Returns'].rolling(window=20).std() * np.sqrt(252)
        df['RSI'] = self.calculate_rsi(df['Close'])
        df['MACD'], df['Signal'] = self.calculate_macd(df['Close'])
        df = df.dropna()

        X = df[['Open', 'High', 'Low', 'Volume', 'MA50', 'MA200', 'Volatility', 'RSI', 'MACD', 'Signal']]
        y = df['Close']

        return train_test_split(X, y, test_size=0.2, random_state=42)

    def calculate_rsi(self, prices, period=14):
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def calculate_macd(self, prices, slow=26, fast=12, smooth=9):
        exp1 = prices.ewm(span=fast, adjust=False).mean()
        exp2 = prices.ewm(span=slow, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=smooth, adjust=False).mean()
        return macd, signal

    def train_model(self, symbol):
        X_train, X_test, y_train, y_test = self.prepare_data(symbol)
        model = RandomForestRegressor(n_estimators=200, random_state=42)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        print(f"{symbol} Model - Mean Squared Error: {mse}, R2 Score: {r2}")

        self.models[symbol] = model

def predict_future(self, symbol, days=30):
    df = self.data[symbol]
    last_date = df.index[-1]
    future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=days)
    future_data = pd.DataFrame(index=future_dates, columns=df.columns)
    
    future_data.iloc[0] = df.iloc[-1]
    
    for column in future_data.columns:
        if pd.api.types.is_integer_dtype(df[column]):
            future_data[column] = future_data[column].astype(float)
        else:
            future_data[column] = future_data[column].astype(df[column].dtype)

    for i in range(1, days):
        future_data.iloc[i] = future_data.iloc[i-1]
        future_data.loc[future_data.index[i], 'MA50'] = future_data.iloc[max(0, i-50):i+1]['Close'].mean()
        future_data.loc[future_data.index[i], 'MA200'] = future_data.iloc[max(0, i-200):i+1]['Close'].mean()
        returns = future_data.iloc[max(0, i-20):i+1]['Close'].pct_change()
        future_data.loc[future_data.index[i], 'Volatility'] = returns.std() * np.sqrt(252)
        future_data.loc[future_data.index[i], 'RSI'] = self.calculate_rsi(future_data['Close'])[-1]
        macd, signal = self.calculate_macd(future_data['Close'])
        future_data.loc[future_data.index[i], 'MACD'] = macd.iloc[-1]
        future_data.loc[future_data.index[i], 'Signal'] = signal.iloc[-1]

    X_future = future_data[['Open', 'High', 'Low', 'Volume', 'MA50', 'MA200', 'Volatility', 'RSI', 'MACD', 'Signal']]
    future_predictions = self.models[symbol].predict(X_future)
    future_data['Predictions'] = future_predictions

    return future_data

    def visualize_predictions(self, symbol, future_data):
        plt.figure(figsize=(15, 10))
        plt.plot(self.data[symbol].index, self.data[symbol]['Close'], label='Historical Close Price')
        plt.plot(future_data.index, future_data['Predictions'], label='Predicted Close Price', color='red')
        plt.title(f"{symbol} Stock Price Prediction")
        plt.xlabel("Date")
        plt.ylabel("Close Price")
        plt.legend()
        plt.show()

    def visualize_sentiment(self, symbol, sentiment_df):
        if sentiment_df.empty:
            print(f"No sentiment data to visualize for {symbol}.")
            return
        plt.figure(figsize=(15, 10))
        sns.lineplot(x=sentiment_df.index, y='sentiment', data=sentiment_df)
        plt.title(f"{symbol} News Sentiment Analysis")
        plt.xlabel("Date")
        plt.ylabel("Sentiment Score")
        plt.xticks(rotation=45)
        plt.show()

    def analyze_correlation(self):
        combined_data = pd.DataFrame()
        for symbol in self.symbols:
            combined_data[symbol] = self.data[symbol]['Close']
        correlation_matrix = combined_data.corr()
        
        plt.figure(figsize=(12, 10))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title("Stock Price Correlation Heatmap")
        plt.show()

    def fetch_economic_indicators(self):
        # This is a placeholder. In a real-world scenario, you'd fetch actual economic data.
        dates = pd.date_range(start=self.start_date, end=self.end_date, freq='D')
        indicators = pd.DataFrame({
            'GDP_Growth': np.random.normal(2, 0.5, len(dates)),
            'Inflation_Rate': np.random.normal(2, 0.3, len(dates)),
            'Unemployment_Rate': np.random.normal(5, 0.5, len(dates))
        }, index=dates)
        return indicators

    def analyze_macroeconomic_impact(self, symbol):
        stock_data = self.data[symbol]['Close'].resample('D').last().dropna()
        indicators = self.fetch_economic_indicators()
        combined_data = pd.concat([stock_data, indicators], axis=1).dropna()
        
        X = sm.add_constant(combined_data[['GDP_Growth', 'Inflation_Rate', 'Unemployment_Rate']])
        y = combined_data['Close']
        
        model = sm.OLS(y, X).fit()
        print(f"\nMacroeconomic Impact Analysis for {symbol}:")
        print(model.summary())

    def analyze_google_trends(self, symbol):
        self.pytrends.build_payload([symbol], timeframe=f'{self.start_date} {self.end_date}')
        interest_over_time = self.pytrends.interest_over_time()
        
        fig, ax1 = plt.subplots(figsize=(15, 10))
        ax2 = ax1.twinx()
        
        ax1.plot(self.data[symbol].index, self.data[symbol]['Close'], 'g-')
        ax2.plot(interest_over_time.index, interest_over_time[symbol], 'b-')
        
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Stock Price', color='g')
        ax2.set_ylabel('Google Trends Interest', color='b')
        
        plt.title(f"{symbol} Stock Price vs Google Trends Interest")
        plt.show()

def run_analysis(self):
        print("Fetching stock data...")
        self.fetch_stock_data()
        
        for symbol in self.symbols:
            print(f"\nAnalyzing {symbol}...")
            print("Training predictive model...")
            self.train_model(symbol)
            
            print("Predicting future prices...")
            future_data = self.predict_future(symbol)
            self.visualize_predictions(symbol, future_data)
            
            print("Analyzing news sentiment...")
            sentiment_df = self.fetch_news_sentiment(symbol)
            self.visualize_sentiment(symbol, sentiment_df)
            
            print("Analyzing macroeconomic impact...")
            self.analyze_macroeconomic_impact(symbol)
            
            print("Analyzing Google Trends...")
            self.analyze_google_trends(symbol)
        
        if len(self.symbols) > 1:
            print("\nAnalyzing correlation between stocks...")
            self.analyze_correlation()

        print("\nAnalysis complete. May the market forces be with you!")


if __name__ == "__main__":
    seer = OmniMarketSeerV2(["TSLA", "AMZN", "FB"])
    seer.run_analysis()