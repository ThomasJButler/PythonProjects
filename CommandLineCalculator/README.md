# Command Line Calculator

A versatile command-line calculator application written in Python that supports basic arithmetic operations and complex mathematical expressions.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division
- Support for complex expressions with proper operator precedence
- Parentheses for grouping operations
- Error handling for invalid inputs and division by zero
- Interactive command-line interface with help documentation

## Usage

### Running the Calculator

To start the calculator, navigate to the project directory and run:

```bash
python CommandLineCalculator/calc123.py
```

### Basic Operations

Enter expressions in the format: `number1 operator number2`

Examples:
```
5 + 3
10 - 7
4 * 6
15 / 3
```

### Complex Expressions

You can also enter complex expressions with proper operator precedence:

```
2+3*4       # Result: 14 (multiplication before addition)
(2+3)*4     # Result: 20 (parentheses change the precedence)
10/2+5      # Result: 10
```

### Commands

- Type `help` to display usage instructions
- Type `exit` to quit the application

## Development

### Project Structure

- `calc123.py` - Main calculator implementation with core arithmetic functions
- `Unittest.py` - Unit tests for the calculator logic

### Running Tests

To run the unit tests:

```bash
python CommandLineCalculator/Unittest.py
```

## Recommendations

1. **Use spaceless expressions for complex calculations**: The calculator supports expressions without spaces for complex calculations (e.g., `5+3*2`), which is useful for quickly entering multi-operation formulas.

2. **Parentheses for clarity**: When working with complex expressions, use parentheses to make your intentions clear and override default operator precedence.

3. **Error checking**: The calculator provides helpful error messages for invalid inputs, division by zero, and syntax errors.

4. **Help command**: If you're unsure about the calculator's capabilities, type `help` for quick instructions.

5. **Consider the format**: For basic operations, follow the format `number1 operator number2` with spaces. For complex expressions, you can omit spaces.

## Future Enhancements

Potential features for future versions:
- Support for more mathematical functions (sin, cos, log, etc.)
- Variable storage and reference
- Ability to save calculation history
- Command-line arguments for non-interactive usage