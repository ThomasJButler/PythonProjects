# calc123.py
import ast
import operator

def add(number1, number2):
    """
    Adds two numbers.

    Parameters:
    number1 (float): The first number.
    number2 (float): The second number.

    Returns:
    float: The sum of number1 and number2.
    """
    return number1 + number2

def subtract(number1, number2):
    """
    Subtracts the second number from the first.

    Parameters:
    number1 (float): The first number.
    number2 (float): The second number.

    Returns:
    float: The difference between number1 and number2.
    """
    return number1 - number2

def multiply(number1, number2):
    """
    Multiplies two numbers.

    Parameters:
    number1 (float): The first number.
    number2 (float): The second number.

    Returns:
    float: The product of number1 and number2.
    """
    # Removed unnecessary check for zero values
    return number1 * number2

def divide(number1, number2):
    """
    Divides the first number by the second.

    Parameters:
    number1 (float): The first number.
    number2 (float): The second number.

    Returns:
    float or str: The quotient of number1 divided by number2, or an error message if dividing by zero.
    """
    if number2 == 0:
        return "Error: Division by zero is not allowed."
    return number1 / number2

def parse_input(expression):
    """
    Parses a mathematical expression.

    Parameters:
    expression (str): The input expression in the format "number1 operator number2".

    Returns:
    tuple: A tuple containing number1, operator, and number2 if the parsing is successful, or (None, None, None) if it fails.
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
    Validates if the operator is one of the supported operators.

    Parameters:
    operator (str): The operator to validate.

    Returns:
    bool: True if the operator is valid, False otherwise.
    """
    return operator in ['+', '-', '*', '/']

def calculate(number1, operator, number2):
    """
    Performs the calculation based on the operator.

    Parameters:
    number1 (float): The first number.
    operator (str): The operator (+, -, *, /).
    number2 (float): The second number.

    Returns:
    float or str: The result of the calculation, or an error message if the operator is invalid.
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
    Parses and evaluates complex mathematical expressions with operator precedence.
    
    Parameters:
    expression (str): The complex mathematical expression (e.g., "10 + 2 * 6")
    
    Returns:
    float or str: The result of the expression or an error message
    """
    # Define mapping for operators
    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }
    
    try:
        # Parse the expression
        node = ast.parse(expression, mode='eval').body
        
        # Define a recursive function to evaluate the AST
        def evaluate(node):
            # If it's a number, return its value
            if isinstance(node, ast.Num):
                return node.value
            
            # If it's an operation (BinOp), evaluate both sides and apply the operator
            elif isinstance(node, ast.BinOp):
                left = evaluate(node.left)
                right = evaluate(node.right)
                
                # Check for division by zero
                if isinstance(node.op, ast.Div) and right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                
                return operations[type(node.op)](left, right)
            
            # If it's a unary operation (e.g., -5)
            elif isinstance(node, ast.UnaryOp):
                operand = evaluate(node.operand)
                if isinstance(node.op, ast.USub):
                    return -operand
                if isinstance(node.op, ast.UAdd):
                    return operand
            
            # For any other type of node, raise an exception
            else:
                raise TypeError(f"Unsupported operation: {node}")
        
        # Evaluate the expression
        result = evaluate(node)
        return result
    
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except (SyntaxError, TypeError, ValueError) as e:
        return f"Error: Invalid expression. {str(e)}"

def perform_calculation(expression):
    """
    Parses the input expression, validates it, and performs the calculation.

    Parameters:
    expression (str): The input mathematical expression.

    Returns:
    str: The result of the calculation or an error message.
    """
    # First, try to parse as a complex expression
    if any(op in expression for op in "+-*/") and not expression.count(' ') == 2:
        result = parse_complex_expression(expression)
        if not isinstance(result, str) or result.startswith("Error"):
            return f"Result: {result}" if not isinstance(result, str) else result
    
    # If complex parsing fails or it's a simple expression, fall back to the original logic
    number1, operator, number2 = parse_input(expression)
    if number1 is None or operator is None or number2 is None:
        return "Error: Invalid input format. Please ensure that both operands are numbers and use the format: [number1] [operator] [number2]"

    if not validate_operator(operator):
        return "Error: Invalid operator. Please use one of the following operators: +, -, *, /"

    result = calculate(number1, operator, number2)
    if isinstance(result, str):
        return result  # This is an error message from the divide function
    return f"Result: {result}"

def show_help():
    """
    Displays the help message for the calculator.
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
    Manages the user interaction loop for the calculator.
    """
    print("Welcome to the Command-Line Calculator!")
    print("Type 'help' for instructions or 'exit' to quit.")
    
    while True:
        # Prompt user for input
        expression = input("Enter a mathematical expression: ").strip().lower()
        
        if expression == 'exit':
            break
        elif expression == 'help':
            show_help()
        else:
            # Perform calculation and display the result
            output = perform_calculation(expression)
            print(output)
            
            # Ask user if they want to perform another calculation
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
