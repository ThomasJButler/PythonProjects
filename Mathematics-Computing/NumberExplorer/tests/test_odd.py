import pytest
# Revert to direct import from src
from src.odd import basic_conditions, prime_factor_filters, explore_odd


@ pytest.mark.parametrize("n,expected", [
    (1, False),    # fails basic condition (1 mod 12 != 1)
    (13, True),    # 13 mod 12 == 1, basic condition
    (105, False),  # divisible by 105
])
def test_basic_conditions(n, expected):
    assert basic_conditions(n) is expected


@ pytest.mark.parametrize("n", [
    1234567891,  # large prime ~ passes factor check? but prime_factor_filters needs composite
])
def test_prime_factor_filters_small(n):
    # Small numbers or primes should fail
    assert prime_factor_filters(7) is False
    assert prime_factor_filters(945) is False
    # Also test the parameterized value 'n'
    assert prime_factor_filters(n) is False


def test_explore_odd_range():
    # In range 1-100, only 13 and 25 etc pass basic, but prime_factor_filters should filter most
    results = explore_odd(1, 100, workers=2)
    # Expect no results since prime_factor_filters is strict
    assert isinstance(results, list)
    assert all(isinstance(t, tuple) for t in results)
