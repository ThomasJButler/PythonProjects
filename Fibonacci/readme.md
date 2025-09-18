# Fibonacci

A Python tool for generating and visualizing Fibonacci sequences with multiple visualization options and mathematical analysis.

## Features

- **Fibonacci Generation**: Generate Fibonacci sequences up to any specified term
- **ASCII Visualization**: Display sequences using ASCII art bars
- **Graphical Plotting**: Create matplotlib visualizations of the sequence
- **Golden Ratio Analysis**: Calculate golden ratio approximations from the sequence
- **Interactive CLI**: User-friendly command-line interface

## Installation

1. Navigate to the Fibonacci directory
2. Install dependencies:
   ```bash
   pip install matplotlib
   ```

## Usage

Run the main script from the repository root:

```bash
python Fibonacci/src/epicFibonacci.py
```

### Interactive Options

The program will prompt you to:
1. Enter the number of terms to generate
2. Choose visualization method:
   - **ASCII (a)**: Text-based bar chart visualization
   - **Plot (p)**: Matplotlib graph with markers and lines
   - **Golden Ratio (g)**: Calculate the golden ratio approximation

### Example Session

```
Enter the number of terms in the Fibonacci sequence: 10
Choose your visualization method: ASCII (a), Plot (p), Golden Ratio (g): p
```

This will generate a matplotlib plot showing the first 10 terms of the Fibonacci sequence.

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

## File Structure

```
Fibonacci/
├── src/
│   └── epicFibonacci.py
└── README.md
```