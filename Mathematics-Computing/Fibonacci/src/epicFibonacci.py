import matplotlib.pyplot as plt
import math

def fibonacci(n):
    """Generate a Fibonacci sequence up to the nth term"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def visualize_fibonacci_ascii(sequence):
    """Visualize the Fibonacci sequence using ASCII art with improved scaling"""
    if not sequence:
        print("No sequence to visualize")
        return

    if len(sequence) == 1:
        print(f"{sequence[0]}: *")
        return

    max_value = max(sequence)
    max_width = 50  # Maximum width for ASCII visualization

    print("\nFibonacci Sequence ASCII Visualization:")
    print("-" * 40)

    for i, value in enumerate(sequence):
        if max_value > 0:
            # Use logarithmic scaling for large numbers
            if max_value > 100:
                scaled_width = int((math.log(value + 1) / math.log(max_value + 1)) * max_width)
            else:
                scaled_width = int((value / max_value) * max_width)
        else:
            scaled_width = 1

        print(f"F({i:2d}) = {value:8d}: " + "*" * scaled_width)

def plot_fibonacci(sequence):
    """Plot the Fibonacci sequence using matplotlib"""
    plt.plot(sequence, marker='o', linestyle='-', color='b')
    plt.title('Fibonacci Sequence')
    plt.xlabel('Term')
    plt.ylabel('Value')
    plt.show()

def golden_ratio_approximation(sequence):
    """Calculate the Golden Ratio approximation from the sequence"""
    if len(sequence) < 2:
        return None

    if sequence[-2] == 0:
        return None

    return sequence[-1] / sequence[-2]

def main():
    """Main function with improved input validation and error handling"""
    try:
        # Input validation with try-except
        n = int(input("Enter the number of terms in the Fibonacci sequence: "))

        if n < 1:
            print("Please enter a positive integer.")
            return

        if n > 50:
            print("Warning: Large sequences may take time to compute and display.")
            proceed = input("Do you want to continue? (y/n): ").lower()
            if proceed != 'y':
                return

        fib_sequence = fibonacci(n)
        print(f"\nGenerated Fibonacci sequence with {len(fib_sequence)} terms:")
        print(f"Sequence: {fib_sequence}")

        choice = input("\nChoose your visualization method: ASCII (a), Plot (p), Golden Ratio (g): ").lower()

        if choice == 'a':
            visualize_fibonacci_ascii(fib_sequence)
        elif choice == 'p':
            try:
                plot_fibonacci(fib_sequence)
            except Exception as e:
                print(f"Error creating plot: {e}")
                print("Make sure matplotlib is installed: pip install matplotlib")
        elif choice == 'g':
            ratio = golden_ratio_approximation(fib_sequence)
            if ratio is None:
                print("Cannot calculate golden ratio approximation for sequences with less than 2 terms or containing zeros.")
            else:
                print(f"Golden Ratio Approximation: {ratio:.10f}")
                print(f"Actual Golden Ratio: {(1 + math.sqrt(5)) / 2:.10f}")
                print(f"Difference: {abs(ratio - (1 + math.sqrt(5)) / 2):.10f}")
        else:
            print("Invalid choice. Please select 'a' for ASCII, 'p' for Plot, or 'g' for Golden Ratio.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
