# NumberExplorer

[![Python](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)

Unified tool for exploring even perfect numbers (via Euclid–Euler theorem) and preliminary filtering of odd perfect number candidates.

## Installation

```bash
# Create and activate conda environment (if you haven't already)
conda create -n numberexplorer python=3.8 -y
conda activate numberexplorer

# Install dependencies into the active environment
pip install -r requirements.txt
```

## Usage

**Important:** Ensure the `numberexplorer` conda environment is active (`conda activate numberexplorer`) before running commands.

For detailed examples, see [examples.txt](examples.txt).

Show help message and available commands/options:
```bash
python src/main.py -h
```

### Even perfect numbers
Generate even perfect numbers up to exponent `p` (max 31):
```bash
python src/main.py even --max-exponent 7
python src/main.py even -m 7 --plot --save visualizations/even.png
```

### Odd perfect number filters
Find candidates in a range with basic necessary conditions:
```bash
python src/main.py odd --start 1 --end 10000
python src/main.py odd -s 1 -e 100000 --workers 8 --plot --save visualizations/odd.png
```

## Testing

**Important:** Ensure the `numberexplorer` conda environment is active (`conda activate numberexplorer`) before running tests.

Run pytest from the `NumberExplorer` project root directory:
```bash
conda activate numberexplorer
pytest
```

## Visualizations
Saved under `visualizations/` when using `--save` flag.

## Mathematical Notes
- **Even perfect numbers**: Fully characterized by Euclid–Euler theorem. No limit to exponent, but practical limit ~31 for 32-bit.
- **Odd perfect numbers**: None known. `odd` module applies necessary filters only; does not prove existence.

## License
This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.