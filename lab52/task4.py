import pytest
def are_anagrams(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    
    if len(word1) != len(word2):
        return False
        
    count = {}
    
    for char in word1:
        count[char] = count.get(char, 0) + 1
            
    for char in word2:
        if char not in count:
            return False
        count[char] -= 1
            
    return all(value == 0 for value in count.values())


word1 = input("first word: ").strip()
word2 = input("second word: ").strip()
print(are_anagrams(word1, word2))

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