import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_single_streak():
    """Tests a simple case with a single streak."""
    assert longest_positive_streak([1, 2, 3]) == 3

def test_multiple_streaks():
    """Tests that the function returns the longest of multiple streaks."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros():
    """Tests that zeros correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_with_negatives():
    """Tests that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, -5, 2, 3]) == 2

def test_all_non_positive():
    """Tests a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_all_ones():
    """Tests a list of all ones."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_long_list():
    """Tests with a longer list and a streak at the end."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4]) == 4