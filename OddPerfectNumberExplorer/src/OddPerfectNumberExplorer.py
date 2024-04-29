import concurrent.futures
import sympy
from math import gcd

def basic_conditions_met(n):
    """Check if n satisfies basic odd perfect number conditions."""
    if n % 105 != 0 and (n % 12 == 1 or n % 468 == 117 or n % 324 == 81):
        return True
    return False

def prime_factor_analysis(n):
    """Analyze the prime factors of n for odd perfect number criteria."""
    prime_factors = sympy.factorint(n)
    primes = list(prime_factors.keys())

    if not primes or len(primes) < 2 or primes[0] < 10**4:
        return False
    if any(p < 100 for p in primes[:3]) or gcd(n, sum(primes)) > 1:
        return False
    return True

def explore_number(n):
    """Explore a single number to check for odd perfect number conditions."""
    if not basic_conditions_met(n):
        return n, False, "Fails basic conditions."
    
    if not prime_factor_analysis(n):
        return n, False, "Fails prime factor analysis."
    
    return n, True, "Potentially satisfies conditions (Note: incomplete check)."

def explore_range(start, end, workers=4):
    """Explore a range of numbers in parallel to find potential odd perfect numbers."""
    potential_candidates = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(explore_number, n) for n in range(start, end + 1)]
        for future in concurrent.futures.as_completed(futures):
            n, result, reason = future.result()
            if result:
                potential_candidates.append((n, reason))
            else:
                print(f"Number: {n} {reason}")

    return potential_candidates

def main():
    print("Odd Perfect Number Explorer")
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    if start >= end or start < 1 or end > 10**4:
        print("Invalid range. Please enter a valid range within computational limits.")
        return
    
    potential_candidates = explore_range(start, end)
    if potential_candidates:
        print("Potential candidates found:")
        for n, reason in potential_candidates:
            print(f"Number: {n} {reason}")
    else:
        print("No potential candidates found in the given range.")

if __name__ == "__main__":
    main()
