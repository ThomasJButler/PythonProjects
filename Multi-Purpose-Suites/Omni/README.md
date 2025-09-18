# Omni

A comprehensive suite of tools for system monitoring and market analysis. The Omni project contains multiple variants focused on different aspects of technology and finance integration.

## Projects Overview

### OmniV1 - Tech Harmony System Monitor
A system monitoring and optimization tool that tracks resource usage and network connectivity.

**Features:**
- Real-time CPU, memory, and disk usage monitoring
- Network connectivity testing and issue resolution
- Resource optimization alerts and automation
- Comprehensive logging system

### OmniMarket Seer - Financial Analysis Tool
A market analysis tool for stock prediction using machine learning and sentiment analysis.

**Features:**
- Stock data fetching via Yahoo Finance
- News sentiment analysis from financial websites
- Random Forest regression for price prediction
- Basic sentiment scoring using keyword analysis

### OmniMarket Seer v2 - Enhanced Financial Analysis
An enhanced version with improved features and capabilities.

**Features:**
- Multi-symbol portfolio analysis with parallel processing
- Advanced sentiment analysis using NLTK's VADER
- Google Trends integration for market sentiment
- Statistical modeling with statsmodels
- Enhanced error handling and data validation
- Comprehensive visualization with matplotlib and seaborn

## Installation

Each sub-project has its own requirements file for easy dependency management:

### OmniV1 (System Monitoring)
```bash
cd Multi-Purpose-Suites/Omni/OmniV1
pip install -r requirements.txt
```

### OmniMarket Seer (Basic Market Analysis)
```bash
cd Multi-Purpose-Suites/Omni/"OmniMarket Seer"
pip install -r requirements.txt
```

### OmniMarket Seer v2 (Enhanced Market Analysis) - **Recommended**
```bash
cd Multi-Purpose-Suites/Omni/"OmniMarket Seer v2"
pip install -r requirements.txt
```

### Additional Setup for Market Seer v2
```bash
# Download NLTK sentiment analysis data
python -c "import nltk; nltk.download('vader_lexicon')"
```

## Usage

### OmniV1 - System Monitor
```python
from OmniV1.omni import OmniTechHarmony

monitor = OmniTechHarmony()
monitor.monitor_resources()  # Check system resources
monitor.check_network()      # Test network connectivity
```

### OmniMarket Seer
```python
from "OmniMarket Seer".omni import OmniMarketSeer

seer = OmniMarketSeer('AAPL')
seer.fetch_stock_data()
sentiment_data = seer.fetch_news_sentiment()
```

### OmniMarket Seer v2
```python
from "OmniMarket Seer v2".omni import OmniMarketSeerV2

seer = OmniMarketSeerV2(['AAPL', 'GOOGL', 'MSFT'])
seer.fetch_stock_data()
sentiment_data = seer.fetch_news_sentiment('AAPL')
```

## Key Features Comparison

| Feature | OmniV1 | Market Seer | Market Seer v2 |
|---------|---------|-------------|----------------|
| System Monitoring | ✅ | ❌ | ❌ |
| Stock Analysis | ❌ | ✅ | ✅ |
| Multi-symbol Support | ❌ | ❌ | ✅ |
| Advanced Sentiment | ❌ | ❌ | ✅ |
| Google Trends | ❌ | ❌ | ✅ |
| Parallel Processing | ❌ | ❌ | ✅ |

## Architecture

```
Omni/
├── OmniV1/
│   ├── omni.py              # System monitoring
│   └── requirements.txt     # Dependencies
├── OmniMarket Seer/
│   ├── omni.py              # Basic market analysis
│   └── requirements.txt     # Dependencies
├── OmniMarket Seer v2/
│   ├── omni.py              # Enhanced market analysis
│   └── requirements.txt     # Dependencies
├── Omni.ipynb               # Interactive Jupyter notebook demo
└── README.md                # This documentation
```

## Data Sources

- **Yahoo Finance**: Stock price and volume data
- **Finviz**: Financial news and sentiment data
- **Google Trends**: Search trend analysis
- **System APIs**: Resource usage monitoring

## Machine Learning Models

- **Random Forest Regressor**: Stock price prediction
- **VADER Sentiment Analysis**: News sentiment scoring
- **Statistical Models**: Time series analysis and correlation

## Status & Recommendations

### OmniV1 ✅
**Status**: Functional system monitoring tool
**Recommendation**: Keep as-is, suitable for basic system monitoring

### OmniMarket Seer ⚠️
**Status**: Basic implementation with limitations
**Recommendation**: Consider deprecation in favor of v2, or use for educational purposes only

### OmniMarket Seer v2 🚧
**Status**: Most advanced but needs improvements
**Known Issues**:
- Prediction logic uses basic Random Forest (consider ARIMA/Prophet/LSTM)
- Web scraping is fragile (replace with news APIs)
- Placeholder economic indicators (integrate real APIs like FRED)

## Future Development

Potential areas for expansion:
- **Real-time data streaming** with WebSocket connections
- **Cryptocurrency market analysis** via Binance/Coinbase APIs
- **Advanced technical indicators** (RSI, MACD, Bollinger Bands)
- **Portfolio optimization algorithms** using Modern Portfolio Theory
- **Alert and notification systems** via email/SMS/Discord
- **Time-series forecasting** with Prophet/ARIMA models
- **News API integration** replacing web scraping