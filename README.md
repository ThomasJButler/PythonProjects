# PythonProjects

A comprehensive collection of Python hobby projects ranging from mathematical exploration and climate visualizations to AI-powered development tools and interactive adventures.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/ThomasJButler/PythonProjects.git
cd PythonProjects

# Each project is self-contained - see individual project READMEs for specific setup
```

## 📋 Project Overview

| Project | Status | Description | Key Technologies |
|---------|--------|-------------|------------------|
| [CommandLineCalculator](./CommandLineCalculator/) | ✅ **Stable** | Terminal-based calculator with expression evaluation | Python AST, Argparse |
| [CtrlS](./CtrlS/) | ✅ **Stable** | Interactive text-based adventure game | Interactive Fiction |
| [DevelopersOracle](./DevelopersOracle/) | 🚧 **In Development** | AI-powered developer assistant with platform integrations | OpenAI, JIRA, GitHub, ML |
| [Fibonacci](./Fibonacci/) | ✅ **Stable** | Fibonacci sequence generation and visualization | Matplotlib, ASCII Art |
| [NumberExplorer](./NumberExplorer/) | ✅ **Stable** | Mathematical tool for exploring perfect numbers | SymPy, Matplotlib, Pytest |
| [Omni](./Omni/) | 🔄 **Multi-Version** | System monitoring and market analysis suite | Multiple variants |
| [ProjectAetheris](./ProjectAetheris/) | ✅ **Stable** | Climate data visualization and chaos theory | Pandas, APIs, Lorenz Attractor |

## 🏗️ Project Structure

```
PythonProjects/
├── CommandLineCalculator/     # Basic terminal calculator
│   ├── calc123.py
│   ├── Unittest.py
│   └── README.md
├── CtrlS/                     # Text-based adventure game
│   ├── src/
│   └── README.md
├── DevelopersOracle/          # AI developer assistant
│   ├── DevelopersOracle.py
│   └── README.md
├── Fibonacci/                 # Fibonacci sequence tools
│   ├── src/epicFibonacci.py
│   └── README.md
├── NumberExplorer/            # Perfect number exploration
│   ├── src/
│   ├── tests/
│   └── README.md
├── Omni/                      # Multi-project suite
│   ├── OmniV1/               # System monitoring
│   ├── OmniMarket Seer/      # Basic market analysis
│   ├── OmniMarket Seer v2/   # Enhanced market analysis
│   └── README.md
├── ProjectAetheris/           # Climate visualization
│   ├── aetheris.py
│   ├── lorenz/               # Chaos theory demonstrations
│   └── README.md
└── README.md                  # This file
```

## 📚 Detailed Project Descriptions

### CommandLineCalculator
A robust terminal calculator supporting basic arithmetic operations and complex expression evaluation. Features comprehensive error handling and a clean command-line interface.

### CtrlS
An interactive text-based adventure game that combines storytelling with coding challenges. Navigate through a humorous narrative that blends programming concepts with adventure gaming.

### DevelopersOracle
An ambitious AI-powered development assistant integrating with multiple platforms (GitHub, GitLab, Bitbucket, JIRA). Features include intelligent code analysis, automated commit message generation, task estimation using machine learning, and sentiment analysis of project communications.

### Fibonacci
A comprehensive tool for exploring Fibonacci sequences with multiple visualization options including ASCII art, matplotlib graphs, and golden ratio calculations. Perfect for mathematical education and exploration.

### NumberExplorer
A sophisticated mathematical exploration tool focused on perfect numbers. Uses the Euclid-Euler theorem for even perfect numbers and provides preliminary filtering for odd perfect number candidates. Features comprehensive testing and visualization capabilities.

### Omni Suite
A multi-faceted project containing three distinct tools:
- **OmniV1**: System monitoring and optimization with resource tracking and network diagnostics
- **OmniMarket Seer**: Stock market analysis with basic sentiment analysis and prediction models
- **OmniMarket Seer v2**: Enhanced market analysis with multi-symbol support, advanced sentiment analysis using NLTK, and Google Trends integration

### ProjectAetheris
Climate data visualization tool that fetches real-time data from NASA GISS and NOAA APIs. Includes correlation analysis between temperature and CO2 trends, plus an optional Lorenz attractor demonstration showcasing chaos theory principles.

## 🛠️ Installation & Setup

### General Requirements
- Python 3.8+
- Individual projects may have specific requirements (see project READMEs)

### Environment Setup
Many projects benefit from isolated environments:

```bash
# For projects requiring conda (NumberExplorer, ProjectAetheris)
conda create --name project_name python=3.9 -y
conda activate project_name
cd ProjectName
pip install -r requirements.txt

# For projects with minimal dependencies
pip install -r requirements.txt
```

### Running Projects
Each project is designed to be run from the repository root:

```bash
# Examples
python CommandLineCalculator/calc123.py
python Fibonacci/src/epicFibonacci.py
python ProjectAetheris/aetheris.py
```

## 🧪 Testing

Projects with test suites:
```bash
# CommandLineCalculator
python CommandLineCalculator/Unittest.py

# NumberExplorer (requires conda environment)
conda activate numberexplorer
cd NumberExplorer
pytest
```

## 🤝 Contributing

Each project is independent with its own coding standards and requirements. Please:
1. Check individual project READMEs for specific guidelines
2. Maintain existing code style and conventions
3. Add tests for new functionality where applicable
4. Update documentation for any changes

## 📄 License

This collection represents hobby projects for educational and experimental purposes.

## 🏷️ Tags

`python` `mathematics` `climate-science` `machine-learning` `data-visualization` `api-integration` `game-development` `system-monitoring` `financial-analysis` `chaos-theory`
