# Fibonacci Sequence Explorer

A comprehensive Python tool for exploring Fibonacci sequences with multiple visualization options, robust input validation, and golden ratio analysis.

## Features

- **Fibonacci Generation**: Generate Fibonacci sequences up to any specified term with edge case handling
- **ASCII Visualization**: Display sequences using intelligent ASCII art with logarithmic scaling
- **Graphical Plotting**: Create matplotlib visualizations of the sequence
- **Golden Ratio Analysis**: Calculate golden ratio approximations with comparison to actual value
- **Interactive CLI**: User-friendly command-line interface with comprehensive error handling
- **Input Validation**: Robust validation for all user inputs with helpful error messages

## Installation

1. Navigate to the Fibonacci directory
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script from the repository root:

```bash
python Mathematics-Computing/Fibonacci/src/epicFibonacci.py
```

### Interactive Options

The program will prompt you to:
1. Enter the number of terms to generate
2. Choose visualization method:
   - **ASCII (a)**: Text-based bar chart visualization
   - **Plot (p)**: Matplotlib graph with markers and lines
   - **Golden Ratio (g)**: Calculate the golden ratio approximation

### Example Sessions

**Golden Ratio Calculation:**
```
Enter the number of terms in the Fibonacci sequence: 15

Generated Fibonacci sequence with 15 terms:
Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

Choose your visualization method: ASCII (a), Plot (p), Golden Ratio (g): g

Golden Ratio Approximation: 1.6180257511
Actual Golden Ratio: 1.6180339887
Difference: 0.0000082376
```

**ASCII Visualization:**
```
Choose your visualization method: ASCII (a), Plot (p), Golden Ratio (g): a

Fibonacci Sequence ASCII Visualization:
----------------------------------------
F( 0) =        0:
F( 1) =        1: *
F( 2) =        1: *
F( 3) =        2: ***
F( 4) =        3: ****
F( 5) =        5: *******
...
```

## Mathematical Background

The Fibonacci sequence is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

As the sequence progresses, the ratio between consecutive terms approaches the golden ratio (φ ≈ 1.618).

## Functions

- `fibonacci(n)`: Generate Fibonacci sequence up to nth term
- `visualize_fibonacci_ascii(sequence)`: ASCII art visualization
- `plot_fibonacci(sequence)`: Matplotlib graph visualization
- `golden_ratio_approximation(sequence)`: Calculate golden ratio from sequence

## Dependencies

- matplotlib (for graphical plotting)

## Error Handling

The program includes comprehensive error handling for:
- Invalid numeric input
- Empty or insufficient sequences for golden ratio calculation
- Matplotlib installation issues
- Large sequence performance warnings
- Keyboard interrupts

## File Structure

```
Fibonacci/
├── src/
│   └── epicFibonacci.py      # Main program with improved features
├── requirements.txt          # Dependencies
├── README.md                 # This documentation
└── Fibonacci.ipynb          # Interactive Jupyter notebook
```