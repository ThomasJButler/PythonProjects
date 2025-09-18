import pytest
# Revert to direct import from src
from src.even import generate_perfect, validate_perfect


def test_generate_perfect_small():
    perfects = generate_perfect(5)
    exponents = [p for p, _ in perfects]
    values = [v for _, v in perfects]
    assert (2 in exponents) and (6 in values)
    assert (3 in exponents) and (28 in values)
    assert (5 in exponents) and (496 in values)


def test_validate_perfect_true():
    for _, n in generate_perfect(5):
        assert validate_perfect(n) is True


def test_validate_perfect_false():
    assert validate_perfect(7) is False
    assert validate_perfect(1) is False
