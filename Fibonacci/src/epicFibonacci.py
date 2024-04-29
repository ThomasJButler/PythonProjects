import matplotlib.pyplot as plt

def fibonacci(n):
    """Generate a Fibonacci sequence up to the nth term"""
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def visualize_fibonacci_ascii(sequence):
    """Visualize the Fibonacci sequence using ASCII art"""
    for value in sequence:
        print(f"{value}: " + "*" * (value // max(sequence) * 100))

def plot_fibonacci(sequence):
    """Plot the Fibonacci sequence using matplotlib"""
    plt.plot(sequence, marker='o', linestyle='-', color='b')
    plt.title('Fibonacci Sequence')
    plt.xlabel('Term')
    plt.ylabel('Value')
    plt.show()

def golden_ratio_approximation(sequence):
    """Calculate the Golden Ratio approximation from the sequence"""
    return sequence[-1] / sequence[-2]

def main():
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))
    fib_sequence = fibonacci(n)
    print("\nGenerated Fibonacci sequence:")

    choice = input("Choose your visualization method: ASCII (a), Plot (p), Golden Ratio (g): ").lower()

    if choice == 'a':
        visualize_fibonacci_ascii(fib_sequence)
    elif choice == 'p':
        plot_fibonacci(fib_sequence)
    elif choice == 'g':
        print(f"Golden Ratio Approximation: {golden_ratio_approximation(fib_sequence)}")
    else:
        print("Invalid choice. Please select a valid option next time.")

if __name__ == "__main__":
    main()
