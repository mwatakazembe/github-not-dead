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