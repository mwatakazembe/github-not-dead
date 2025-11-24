def count_words(sentence):
    words = sentence.split()
    return len(words)

def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("") == 0
    assert count_words("   ") == 0
    assert count_words("one") == 1
    assert count_words("  multiple   spaces   between   words  ") == 4
    assert count_words("trailing space ") == 2
    assert count_words(" leading space") == 2
    assert count_words("mixed   spacing   and\nnewlines") == 4