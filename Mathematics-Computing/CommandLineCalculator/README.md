# Command Line Calculator

A simple Python calculator supporting basic arithmetic and complex expressions with proper operator precedence.

## Usage

Run the calculator:

```bash
python CommandLineCalculator/calc123.py
```

Basic operations use the format `number1 operator number2`:
```
5 + 3
10 - 7
4 * 6
15 / 3
```

Complex expressions work with standard operator precedence:
```
2+3*4       # Result: 14 (multiply first)
(2+3)*4     # Result: 20 (parentheses override)
10/2+5      # Result: 10
```

Type `help` for instructions or `exit` to quit.

## Testing

Run the unit tests:

```bash
python CommandLineCalculator/Unittest.py
```

## Features

- Addition, subtraction, multiplication, division
- Complex expressions with operator precedence
- Parentheses for grouping
- Error handling for invalid input and division by zero
