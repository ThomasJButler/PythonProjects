# PythonProjects

Collection of Python hobby projects including mathematical tools, climate visualisation, AI development assistants, and interactive games.

## Quick Start

```bash
git clone https://github.com/ThomasJButler/PythonProjects.git
cd PythonProjects
```

Each project is self-contained. See individual READMEs for specific setup.

## Projects

### Mathematics & Computing

- [CommandLineCalculator](./Mathematics-Computing/CommandLineCalculator/) - Terminal calculator with input validation and testing
- [Fibonacci](./Mathematics-Computing/Fibonacci/) - Fibonacci sequence explorer with visualisation
- [NumberExplorer](./Mathematics-Computing/NumberExplorer/) - Perfect number exploration tool

### Data Visualisation

- [ProjectAetheris](./Data-Visualization/ProjectAetheris/) - Climate data visualisation with Lorenz attractor

### Development Tools

- [DevelopersOracle](./Development-AI-Tools/DevelopersOracle/) - AI-powered developer assistant

### Multi-Purpose Tools

- [Omni](./Multi-Purpose-Suites/Omni/) - System monitoring and market analysis suite

### Games

- [CtrlS](./Interactive-Gaming/CtrlS/) - Text-based adventure game

## Setup

### Requirements

- Python 3.8+
- Individual projects may have additional requirements

### Installation

```bash
# Basic projects
pip install -r requirements.txt

# Projects with conda environments (NumberExplorer, ProjectAetheris)
conda create --name project_name python=3.9 -y
conda activate project_name
pip install -r requirements.txt
```

### Running Projects

```bash
# Examples
python Mathematics-Computing/CommandLineCalculator/calc123.py
python Mathematics-Computing/Fibonacci/src/epicFibonacci.py
python Data-Visualization/ProjectAetheris/aetheris.py
```

## Testing

```bash
# CommandLineCalculator
python Mathematics-Computing/CommandLineCalculator/Unittest.py

# NumberExplorer (requires conda environment)
cd Mathematics-Computing/NumberExplorer
pytest
```

## Contributing

1. Check individual project READMEs for specific guidelines
2. Maintain existing code style and conventions
3. Add tests for new functionality where applicable
4. Update documentation for any changes

## License

Hobby projects for educational and experimental purposes.
