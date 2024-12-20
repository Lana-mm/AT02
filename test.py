import pytest
from main import count_vowels

def test_only_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0

def test_mixed_string():
    assert count_vowels("Hello, World!") == 3
    assert count_vowels("FdsGfaah") == 2
    assert count_vowels("AEIOUaeiou") == 10
    assert count_vowels("12345!@#$%^&*()") == 0