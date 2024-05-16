import unittest
from unittest.mock import patch
from calc123 import run_calculator

class TestCalculatorCLI(unittest.TestCase):

    @patch('builtins.input', side_effect=['2 + 2', 'no'])
    def test_addition(self, mock_input):
        with patch('builtins.print') as mock_print:
            run_calculator(input)
            mock_print.assert_any_call("Result: 4.0")

    @patch('builtins.input', side_effect=['5 - 3', 'no'])
    def test_subtraction(self, mock_input):
        with patch('builtins.print') as mock_print:
            run_calculator(input)
            mock_print.assert_any_call("Result: 2.0")

    @patch('builtins.input', side_effect=['2 * 3', 'no'])
    def test_multiplication(self, mock_input):
        with patch('builtins.print') as mock_print:
            run_calculator(input)
            mock_print.assert_any_call("Result: 6.0")

    @patch('builtins.input', side_effect=['6 / 3', 'no'])
    def test_division(self, mock_input):
        with patch('builtins.print') as mock_print:
            run_calculator(input)
            mock_print.assert_any_call("Result: 2.0")

    @patch('builtins.input', side_effect=['6 / 0', 'no'])
    def test_division_by_zero(self, mock_input):
        with patch('builtins.print') as mock_print:
            try:
                run_calculator(input)
                mock_print.assert_any_call("Error: Division by zero is not allowed.")
            except AssertionError:
                print("Captured print calls:")
                for call in mock_print.mock_calls:
                    print(call)
                raise

    @patch('builtins.input', side_effect=['invalid input', 'no'])
    def test_invalid_input_format(self, mock_input):
        with patch('builtins.print') as mock_print:
            run_calculator(input)
            mock_print.assert_any_call("Error: Invalid input format. Please ensure that both operands are numbers and use the format: [number1] [operator] [number2]")

    @patch('builtins.input', side_effect=['2 + 2', 'yes', '5 * 3', 'no'])
    def test_continuous_operations(self, mock_input):
        with patch('builtins.print') as mock_print:
            run_calculator(input)
            mock_print.assert_any_call("Result: 4.0")
            mock_print.assert_any_call("Result: 15.0")

if __name__ == "__main__":
    unittest.main()
