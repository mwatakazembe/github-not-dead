from src.task4 import are_anagrams

def test_anagrams_basic():
    assert are_anagrams("listen", "silent") == True

def test_anagrams_different_case():
    assert are_anagrams("Listen", "Silent") == True

def test_not_anagrams():
    assert are_anagrams("hello", "world") == False

def test_different_length():
    assert are_anagrams("cat", "taco") == False

def test_empty_strings():
    assert are_anagrams("", "") == True

def test_special_characters():
    assert are_anagrams("a!b", "b!a") == True