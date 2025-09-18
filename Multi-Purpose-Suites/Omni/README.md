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

### General Dependencies
```bash
pip install requests beautifulsoup4 pandas numpy scikit-learn matplotlib seaborn psutil
```

### OmniV1 Dependencies
```bash
pip install psutil requests
```

### OmniMarket Seer Dependencies
```bash
pip install yfinance requests beautifulsoup4 pandas numpy scikit-learn matplotlib seaborn
```

### OmniMarket Seer v2 Dependencies
```bash
pip install yfinance requests beautifulsoup4 pandas numpy scikit-learn matplotlib seaborn nltk statsmodels pytrends
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
│   └── omni.py              # System monitoring
├── OmniMarket Seer/
│   └── omni.py              # Basic market analysis
├── OmniMarket Seer v2/
│   └── omni.py              # Enhanced market analysis
└── README.md
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

## Future Development

Potential areas for expansion:
- Real-time data streaming
- Cryptocurrency market analysis
- Advanced technical indicators
- Portfolio optimization algorithms
- Alert and notification systems