from calc123 import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5, "Test case 1 failed"
    assert add(-1, 5) == 4, "Test case 2 failed"
    assert add(0, 0) == 0, "Test case 3 failed"
    print("All test cases for addition passed.")

def test_subtract():
    assert subtract(5, 3) == 2, "Test case 1 failed"
    assert subtract(-1, 5) == -6, "Test case 2 failed"
    assert subtract(0, 0) == 0, "Test case 3 failed"
    print("All test cases for subtraction passed.")

def test_multiply():
    assert multiply(2, 3) == 6, "Test case 1 failed"
    assert multiply(-1, 5) == -5, "Test case 2 failed"
    assert multiply(0, 100) == 0, "Test case 3 failed"
    print("All test cases for multiplication passed.")

def test_divide():
    assert divide(6, 3) == 2, "Test case 1 failed"
    assert divide(-10, 5) == -2, "Test case 2 failed"
    assert divide(0, 1) == 0, "Test case 3 failed"
    assert divide(1, 0) == "Error: Division by zero is not allowed.", "Test case 4 failed"
    print("All test cases for division passed.")

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
