import unittest
from calc123 import add, subtract, multiply, divide, calculate, parse_input, validate_operator, parse_complex_expression

class TestCalculatorFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)
        
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 5), -6)
        self.assertEqual(subtract(0, 0), 0)
        
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 100), 0)
        
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-10, 5), -2)
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(1, 0), "Error: Division by zero is not allowed.")
        
    def test_validate_operator(self):
        self.assertTrue(validate_operator('+'))
        self.assertTrue(validate_operator('-'))
        self.assertTrue(validate_operator('*'))
        self.assertTrue(validate_operator('/'))
        self.assertFalse(validate_operator('%'))
        self.assertFalse(validate_operator('x'))
        
    def test_parse_input(self):
        self.assertEqual(parse_input("5 + 3"), (5, '+', 3))
        self.assertEqual(parse_input("-1 * 5"), (-1, '*', 5))
        self.assertEqual(parse_input("10/2"), (None, None, None))  # This format isn't supported by parse_input
        # Test invalid input
        self.assertEqual(parse_input("abc"), (None, None, None))
        
    def test_calculate(self):
        self.assertEqual(calculate(5, '+', 3), 8)
        self.assertEqual(calculate(5, '-', 3), 2)
        self.assertEqual(calculate(5, '*', 3), 15)
        self.assertEqual(calculate(10, '/', 2), 5)
        self.assertEqual(calculate(1, '/', 0), "Error: Division by zero is not allowed.")
        self.assertEqual(calculate(1, '%', 2), "Error: Invalid operator. Please use one of the following operators: +, -, *, /")
        
    def test_parse_complex_expression(self):
        self.assertEqual(parse_complex_expression("2+3"), 5)
        self.assertEqual(parse_complex_expression("2+3*4"), 14)  # Tests operator precedence
        self.assertEqual(parse_complex_expression("(2+3)*4"), 20)  # Tests parentheses
        self.assertEqual(parse_complex_expression("10/2"), 5)
        self.assertEqual(parse_complex_expression("10/0"), "Error: Division by zero is not allowed.")

if __name__ == "__main__":
    unittest.main()
