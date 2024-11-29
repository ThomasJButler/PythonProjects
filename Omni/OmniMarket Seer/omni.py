import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from datetime import datetime, timedelta

class OmniMarketSeer:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data = None
        self.model = None

    def fetch_stock_data(self):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365*5)  # 5 years of data
        self.data = yf.download(self.symbol, start=start_date, end=end_date)

    def fetch_news_sentiment(self):
        url = f"https://finviz.com/quote.ashx?t={self.symbol}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        news_table = soup.find(id='news-table')
        news_rows = news_table.findAll('tr')

        parsed_news = []
        for row in news_rows:
            title = row.a.text
            date_data = row.td.text.split(' ')
            if len(date_data) == 1:
                time = date_data[0]
            else:
                date = date_data[0]
                time = date_data[1]
            parsed_news.append([date, time, title])

        df = pd.DataFrame(parsed_news, columns=['date', 'time', 'title'])
        df['sentiment'] = df['title'].apply(self.simple_sentiment_analysis)
        return df

    def simple_sentiment_analysis(self, text):
        # List of positive and negative words
        positive_words = ['up', 'rise', 'gain', 'positive', 'grow', 'increase', 'higher']
        negative_words = ['down', 'fall', 'loss', 'negative', 'shrink', 'decrease', 'lower']

        # Convert text to lowercase for easier matching
        text = text.lower()

        # Count positive and negative words
        positive_count = sum(1 for word in positive_words if word in text)
        negative_count = sum(1 for word in negative_words if word in text)

        # Calculate sentiment
        if positive_count > negative_count:
            return 1  # Positive sentiment
        elif negative_count > positive_count:
            return -1  # Negative sentiment
        else:
            return 0  # Neutral sentiment

    def prepare_data(self):
        self.data['Returns'] = self.data['Close'].pct_change()
        self.data['MA50'] = self.data['Close'].rolling(window=50).mean()
        self.data['MA200'] = self.data['Close'].rolling(window=200).mean()
        self.data['Volatility'] = self.data['Returns'].rolling(window=20).std() * np.sqrt(252)
        self.data = self.data.dropna()

        X = self.data[['Open', 'High', 'Low', 'Volume', 'MA50', 'MA200', 'Volatility']]
        y = self.data['Close']

        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        X_train, X_test, y_train, y_test = self.prepare_data()
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Model Mean Squared Error: {mse}")

    def predict_future(self, days=30):
        last_date = self.data.index[-1]
        future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=days)
        future_data = pd.DataFrame(index=future_dates, columns=self.data.columns)
        future_data = future_data.fillna(0)

        for i in range(days):
            if i == 0:
                future_data.iloc[i] = self.data.iloc[-1]
            else:
                future_data.iloc[i] = future_data.iloc[i-1]
            
            future_data.iloc[i, future_data.columns.get_loc('MA50')] = future_data.iloc[max(0, i-50):i+1]['Close'].mean()
            future_data.iloc[i, future_data.columns.get_loc('MA200')] = future_data.iloc[max(0, i-200):i+1]['Close'].mean()
            future_data.iloc[i, future_data.columns.get_loc('Volatility')] = future_data.iloc[max(0, i-20):i+1]['Returns'].std() * np.sqrt(252)

        X_future = future_data[['Open', 'High', 'Low', 'Volume', 'MA50', 'MA200', 'Volatility']]
        future_predictions = self.model.predict(X_future)
        future_data['Predictions'] = future_predictions

        return future_data

    def visualize_predictions(self, future_data):
        plt.figure(figsize=(15, 10))
        plt.plot(self.data.index, self.data['Close'], label='Historical Close Price')
        plt.plot(future_data.index, future_data['Predictions'], label='Predicted Close Price', color='red')
        plt.title(f"{self.symbol} Stock Price Prediction")
        plt.xlabel("Date")
        plt.ylabel("Close Price")
        plt.legend()
        plt.show()

    def visualize_sentiment(self, sentiment_df):
        plt.figure(figsize=(15, 10))
        sns.barplot(x=sentiment_df.index, y='sentiment', data=sentiment_df)
        plt.title(f"{self.symbol} News Sentiment Analysis")
        plt.xlabel("Date")
        plt.ylabel("Sentiment (-1: Negative, 0: Neutral, 1: Positive)")
        plt.xticks(rotation=45)
        plt.show()

    def run_analysis(self):
        print("Fetching stock data...")
        self.fetch_stock_data()
        
        print("Training predictive model...")
        self.train_model()
        
        print("Predicting future prices...")
        future_data = self.predict_future()
        self.visualize_predictions(future_data)
        
        print("Analyzing news sentiment...")
        sentiment_df = self.fetch_news_sentiment()
        self.visualize_sentiment(sentiment_df)

        print("Analysis complete. May the market forces be with you!")


# Example usage
if __name__ == "__main__":
    seer = OmniMarketSeer("MSFT")  # You can change this to any stock symbol
    seer.run_analysis()