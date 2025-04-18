import concurrent.futures
import sympy
from math import gcd
import os # Import os module


def basic_conditions(n):
    """
    Check if n satisfies basic odd perfect number necessary conditions.
    """
    # Odd perfect numbers must be > 1
    if n <= 1:
        return False
    return n % 105 != 0 and (n % 12 == 1 or n % 468 == 117 or n % 324 == 81)


def prime_factor_filters(n):
    """
    Analyze prime factors of n for odd perfect number criteria.
    Returns True if filters pass.
    """
    factors = sympy.factorint(n)
    primes = list(factors.keys())
    if len(primes) < 2 or primes[0] < 10**4:
        return False
    if any(p < 100 for p in primes[:3]) or gcd(n, sum(primes)) > 1:
        return False
    return True


def explore_odd(start, end, workers=4):
    """
    Explore range for potential odd perfect number candidates.
    Returns list of (n, reason) for candidates.
    """
    candidates = []

    def check(n):
        if not basic_conditions(n):
            return None
        if not prime_factor_filters(n):
            return None
        return (n, "Passes basic and prime-factor filters")

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        for result in ex.map(check, range(start, end+1)):
            if result:
                candidates.append(result)
    return candidates


def plot_filters(results, show=True, save_path=None):
    """
    Plot histogram of how many numbers passed odd filters.
    Only calls plt.show() if show is True.
    Creates the directory for save_path if it doesn't exist.
    """
    import matplotlib.pyplot as plt
    counts = len(results)
    plt.figure()
    plt.bar(['Candidates'], [counts])
    plt.ylabel('Count')
    plt.title('Odd Perfect Number Filter Passes')
    if save_path:
        # Ensure the directory exists before saving
        dir_path = os.path.dirname(save_path)
        if dir_path: # Check if dir_path is not empty
            os.makedirs(dir_path, exist_ok=True)
        plt.savefig(save_path)
    if show:
        plt.show()
    plt.close() # Close the figure after showing/saving