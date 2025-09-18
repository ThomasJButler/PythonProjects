import sympy
import os # Import os module


def generate_perfect(p_max):
    """
    Generate even perfect numbers using Euclid–Euler theorem up to exponent p_max.
    Returns a list of tuples (p, perfect_number).
    """
    perfects = []
    for p in range(2, p_max + 1):
        mersenne = (1 << p) - 1
        if sympy.isprime(mersenne):
            perfect = (1 << (p - 1)) * mersenne
            perfects.append((p, perfect))
    return perfects


def validate_perfect(n):
    """
    Validate n is a perfect number by checking sum of proper divisors equals n.
    """
    if n < 2:
        return False
    return sympy.divisors(n)[:-1] and sum(sympy.divisors(n)) - n == n


def plot_perfects(perfects, show=True, save_path=None):
    """
    Plot perfect numbers growth: exponents vs values on log scale.
    Only calls plt.show() if show is True.
    Creates the directory for save_path if it doesn't exist.
    """
    import matplotlib.pyplot as plt
    exponents, values = zip(*perfects) if perfects else ([], [])
    plt.figure()
    plt.plot(exponents, values, 'o-')
    plt.yscale('log')
    plt.xlabel('Exponent p')
    plt.ylabel('Perfect number (log scale)')
    plt.title('Even Perfect Numbers')
    if save_path:
        # Ensure the directory exists before saving
        dir_path = os.path.dirname(save_path)
        if dir_path: # Check if dir_path is not empty
            os.makedirs(dir_path, exist_ok=True)
        plt.savefig(save_path)
    if show:
        plt.show()
    plt.close() # Close the figure after showing/saving