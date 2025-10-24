"""
@author Tom Butler
@date 2025-10-24
@description Command-line calculator implementing basic arithmetic operations with support for complex expressions and operator precedence.
"""
import ast
import operator

def add(number1, number2):
    """
    @param {float} number1 - First operand.
    @param {float} number2 - Second operand.
    @return {float} Sum of the two numbers.
    """
    return number1 + number2

def subtract(number1, number2):
    """
    @param {float} number1 - First operand.
    @param {float} number2 - Second operand.
    @return {float} Difference of the two numbers.
    """
    return number1 - number2

def multiply(number1, number2):
    """
    @param {float} number1 - First operand.
    @param {float} number2 - Second operand.
    @return {float} Product of the two numbers.
    """
    return number1 * number2

def divide(number1, number2):
    """
    @param {float} number1 - Dividend.
    @param {float} number2 - Divisor.
    @return {float|str} Quotient or error message if dividing by zero.
    """
    if number2 == 0:
        return "Error: Division by zero is not allowed."
    return number1 / number2

def parse_input(expression):
    """
    @param {str} expression - Input in format "number1 operator number2".
    @return {tuple} (number1, operator, number2) or (None, None, None) if parsing fails.
    """
    try:
        number1, operator, number2 = expression.split()
        number1 = float(number1)
        number2 = float(number2)
        return number1, operator, number2
    except ValueError:
        return None, None, None

def validate_operator(operator):
    """
    @param {str} operator - Operator to validate.
    @return {bool} True if operator is supported, False otherwise.
    """
    return operator in ['+', '-', '*', '/']

def calculate(number1, operator, number2):
    """
    @param {float} number1 - First operand.
    @param {str} operator - Mathematical operator (+, -, *, /).
    @param {float} number2 - Second operand.
    @return {float|str} Result of calculation or error message.
    """
    if operator == '+':
        return add(number1, number2)
    elif operator == '-':
        return subtract(number1, number2)
    elif operator == '*':
        return multiply(number1, number2)
    elif operator == '/':
        return divide(number1, number2)
    else:
        return "Error: Invalid operator. Please use one of the following operators: +, -, *, /"

def parse_complex_expression(expression):
    """
    @param {str} expression - Complex mathematical expression (e.g., "10 + 2 * 6").
    @return {float|str} Result of the expression or error message.
    """
    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }

    try:
        node = ast.parse(expression, mode='eval').body

        def evaluate(node):
            if isinstance(node, ast.Num):
                return node.value
            elif isinstance(node, ast.BinOp):
                left = evaluate(node.left)
                right = evaluate(node.right)

                if isinstance(node.op, ast.Div) and right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")

                return operations[type(node.op)](left, right)
            elif isinstance(node, ast.UnaryOp):
                operand = evaluate(node.operand)
                if isinstance(node.op, ast.USub):
                    return -operand
                if isinstance(node.op, ast.UAdd):
                    return operand
            else:
                raise TypeError(f"Unsupported operation: {node}")

        result = evaluate(node)
        return result

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except (SyntaxError, TypeError, ValueError) as e:
        return f"Error: Invalid expression. {str(e)}"

def perform_calculation(expression):
    """
    @param {str} expression - Mathematical expression to evaluate.
    @return {str} Result with "Result: " prefix or error message.
    """
    # Try complex expression parsing first for multi-operation expressions
    if any(op in expression for op in "+-*/") and not expression.count(' ') == 2:
        result = parse_complex_expression(expression)
        if not isinstance(result, str) or result.startswith("Error"):
            return f"Result: {result}" if not isinstance(result, str) else result

    number1, operator, number2 = parse_input(expression)
    if number1 is None or operator is None or number2 is None:
        return "Error: Invalid input format. Please ensure that both operands are numbers and use the format: [number1] [operator] [number2]"

    if not validate_operator(operator):
        return "Error: Invalid operator. Please use one of the following operators: +, -, *, /"

    result = calculate(number1, operator, number2)
    if isinstance(result, str):
        return result
    return f"Result: {result}"

def show_help():
    """
    @return None - Prints help message to stdout.
    """
    help_message = """
    Command-Line Calculator Help:
    - Enter expressions in the format: [number1] [operator] [number2]
      Example: 5 + 3
    - You can also enter complex expressions with operator precedence:
      Example: 5 + 3 * 2
    - Supported operators: + (addition), - (subtraction), * (multiplication), / (division)
    - Type 'help' to display this help message.
    - Type 'exit' to exit the calculator.
    """
    print(help_message)

def handle_user_interaction():
    """
    @return None - Manages interactive REPL loop for calculator operations.
    """
    print("Welcome to the Command-Line Calculator!")
    print("Type 'help' for instructions or 'exit' to quit.")

    while True:
        expression = input("Enter a mathematical expression: ").strip().lower()

        if expression == 'exit':
            break
        elif expression == 'help':
            show_help()
        else:
            output = perform_calculation(expression)
            print(output)

            while True:
                continue_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
                if continue_calculation == 'yes':
                    break
                elif continue_calculation == 'no':
                    print("Thank you for using the calculator. Goodbye!")
                    return
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    handle_user_interaction()
