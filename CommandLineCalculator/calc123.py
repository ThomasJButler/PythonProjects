# calc123.py

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
    if number1 == 0 or number2 == 0:
        return 0
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

def perform_calculation(expression):
    """
    Parses the input expression, validates it, and performs the calculation.

    Parameters:
    expression (str): The input mathematical expression.

    Returns:
    str: The result of the calculation or an error message.
    """
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
