`# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

This is a collection of Python hobby projects organized as independent modules, each focusing on different mathematical, scientific, or utility applications:

- **CommandLineCalculator**: Basic terminal calculator with expression evaluation
- **CtrlS**: Text-based adventure game
- **DevelopersOracle**: AI-powered developer assistant (under development)
- **Fibonacci**: Fibonacci sequence generation and visualization
- **NumberExplorer**: Mathematical tool for exploring perfect numbers
- **Omni**: Container for multiple sub-projects (market analysis, system monitoring)
- **ProjectAetheris**: Climate data visualization (temperature & CO2 trends)

## Development Commands

### Running Individual Projects

Each project is self-contained. Run from the repository root:

```bash
# Command Line Calculator
python CommandLineCalculator/calc123.py

# Project Aetheris (requires conda environment)
conda create --name aetheris python=3.9 -y
conda activate aetheris
cd ProjectAetheris
pip install -r requirements.txt
python aetheris.py

# NumberExplorer (requires conda environment)
conda create -n numberexplorer python=3.8 -y
conda activate numberexplorer
cd NumberExplorer
pip install -r requirements.txt
python src/main.py -h
```

### Testing

Each project handles testing differently:

```bash
# CommandLineCalculator
python CommandLineCalculator/Unittest.py

# NumberExplorer (requires active conda environment)
conda activate numberexplorer
cd NumberExplorer
pytest
```

### Dependencies

Projects use different dependency management approaches:
- **CommandLineCalculator**: No external dependencies
- **NumberExplorer**: Uses `requirements.txt` with sympy, matplotlib, pytest
- **ProjectAetheris**: Uses `requirements.txt` with pandas, requests, matplotlib
- Most projects recommend conda environments for isolation

## Architecture Notes

### NumberExplorer
- Structured as a proper Python package with `src/` directory
- Uses argparse for CLI with subcommands (`even`, `odd`)
- Modular design: separate modules for even/odd perfect number logic
- Supports visualization with matplotlib and parallel processing

### CommandLineCalculator
- Simple functional design with dedicated arithmetic functions
- Uses AST parsing for complex expression evaluation
- Error handling for division by zero and invalid inputs
- Interactive CLI with help system

### ProjectAetheris
- Data science pipeline: fetch → process → visualize
- Fetches real-time data from NASA GISS and NOAA APIs
- Uses pandas for data processing and matplotlib for visualization
- Includes optional Lorenz attractor chaos theory demonstration

## Important Notes

- Each project is independent - no shared dependencies or common utilities
- Most projects expecting to be run from repository root, not their subdirectories
- Conda environments are preferred for projects with dependencies
- No centralized build system - each project manages its own setup