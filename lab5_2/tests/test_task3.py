from src.task3 import is_palindrome

def test_palindrome_number_positive():
    assert is_palindrome(121) == True

def test_palindrome_number_negative():
    assert is_palindrome(-121) == False

def test_palindrome_string_positive():
    assert is_palindrome("aba") == True

def test_palindrome_string_negative():
    assert is_palindrome("abc") == False

def test_palindrome_empty_string():
    assert is_palindrome("") == True

def test_palindrome_single_char():
    assert is_palindrome("a") == True

def test_palindrome_mixed_case():
    assert is_palindrome("Anna") == False