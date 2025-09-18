`# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

This is a collection of Python hobby projects organized into thematic folders for better organization:

### Mathematics-Computing/
- **CommandLineCalculator**: Enhanced terminal calculator with robust input validation
- **Fibonacci**: Advanced sequence explorer with golden ratio analysis and improved ASCII visualization
- **NumberExplorer**: Mathematical tool for exploring perfect numbers with comprehensive testing

### Data-Visualization/
- **ProjectAetheris**: Climate data visualization with chaos theory demonstrations

### Development-AI-Tools/
- **DevelopersOracle**: AI-powered developer assistant with complete configuration setup

### Multi-Purpose-Suites/
- **Omni**: Three-variant suite (OmniV1 system monitoring, OmniMarket Seer v1 & v2 for market analysis)

### Interactive-Gaming/
- **CtrlS**: Refactored text-based adventure game with modular chapter system

## Development Commands

### Running Individual Projects

Each project is self-contained. Run from the repository root:

```bash
# CommandLineCalculator (Enhanced)
python Mathematics-Computing/CommandLineCalculator/calc123.py

# Fibonacci Explorer (Enhanced)
python Mathematics-Computing/Fibonacci/src/epicFibonacci.py

# CtrlS Game (Refactored with new engine)
python Interactive-Gaming/CtrlS/src/game_engine.py
# Or use legacy version: python Interactive-Gaming/CtrlS/src/ctrl-s.py

# Project Aetheris (requires conda environment)
conda create --name aetheris python=3.9 -y
conda activate aetheris
cd Data-Visualization/ProjectAetheris
pip install -r requirements.txt
python aetheris.py

# NumberExplorer (requires conda environment)
conda create -n numberexplorer python=3.8 -y
conda activate numberexplorer
cd Mathematics-Computing/NumberExplorer
pip install -r requirements.txt
python src/main.py -h

# DevelopersOracle (requires configuration)
cd Development-AI-Tools/DevelopersOracle
cp config.json.template config.json
# Edit config.json with your API keys
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python DevelopersOracle.py

# Omni Suite (multiple variants)
cd Multi-Purpose-Suites/Omni/OmniV1
pip install -r requirements.txt
python omni.py
```

### Testing

Each project handles testing differently:

```bash
# CommandLineCalculator
python Mathematics-Computing/CommandLineCalculator/Unittest.py

# NumberExplorer (requires active conda environment)
conda activate numberexplorer
cd Mathematics-Computing/NumberExplorer
pytest
```

### Dependencies

All projects now have proper requirements.txt files for easy dependency management:
- **CommandLineCalculator**: No external dependencies (uses only Python stdlib)
- **Fibonacci**: matplotlib for plotting functionality
- **NumberExplorer**: sympy, matplotlib, pytest for mathematical analysis
- **ProjectAetheris**: pandas, requests, matplotlib for data visualization
- **DevelopersOracle**: Comprehensive ML/AI stack (openai, scikit-learn, spacy, PyQt5, etc.)
- **CtrlS**: No external dependencies (Python stdlib only)
- **Omni Suite**: Each variant has its own requirements.txt

## Architecture Notes

### NumberExplorer
- Structured as a proper Python package with `src/` directory
- Uses argparse for CLI with subcommands (`even`, `odd`)
- Modular design: separate modules for even/odd perfect number logic
- Supports visualization with matplotlib and parallel processing

### CommandLineCalculator (Enhanced)
- Simple functional design with dedicated arithmetic functions
- Uses AST parsing for complex expression evaluation
- Comprehensive error handling and input validation
- Interactive CLI with help system
- Complete test suite with Unittest.py

### Fibonacci (Enhanced)
- Advanced sequence generation with edge case handling
- Improved ASCII visualization with logarithmic scaling
- Golden ratio approximation with comparison to actual value
- Comprehensive input validation and error handling
- matplotlib plotting with error handling

### CtrlS (Refactored)
- Modular architecture with separate game engine (game_engine.py)
- Chapter loading system for sequential gameplay
- Centralized utilities module (utils.py) for shared functions
- Proper Python package structure with __init__.py files
- Legacy support for original ctrl-s.py file

### ProjectAetheris
- Data science pipeline: fetch → process → visualize
- Fetches real-time data from NASA GISS and NOAA APIs
- Uses pandas for data processing and matplotlib for visualization
- Includes optional Lorenz attractor chaos theory demonstration

### DevelopersOracle (Configured)
- Complete configuration template system with config.json.template
- Comprehensive requirements.txt with all ML/AI dependencies
- Security-focused approach with .gitignore protection
- Documentation for obtaining all required API keys
- Ready for implementation of core ML functionality

### Omni Suite (Enhanced)
- Three distinct variants: OmniV1 (system monitoring), OmniMarket Seer v1 & v2 (market analysis)
- Each variant has its own requirements.txt file
- Comprehensive documentation explaining differences and recommendations
- OmniMarket Seer v2 is the most advanced with NLTK sentiment analysis and Google Trends

## Important Notes

- Projects are now organized into thematic folders for better discoverability
- Each project has its own requirements.txt for easy dependency management
- All projects expected to be run from repository root
- Conda environments recommended for data science projects (ProjectAetheris, NumberExplorer)
- Complete documentation and setup instructions for all projects
- Security best practices implemented (config files in .gitignore)

## Recent Improvements (2024)

- ✅ **Refactored CtrlS** with modular game engine and chapter loading
- ✅ **Enhanced Fibonacci** with improved input validation and ASCII visualization
- ✅ **Configured DevelopersOracle** with complete setup documentation and security
- ✅ **Organized Projects** into thematic folders (Mathematics-Computing, etc.)
- ✅ **Added Requirements Files** to all projects for easy dependency management
- ✅ **Updated Documentation** across all projects with comprehensive setup guides