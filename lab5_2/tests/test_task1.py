from src.task1 import count_words

def test_task1():
    assert count_words("hello world") == 2
    assert count_words("") == 0
    assert count_words("   ") == 0
    assert count_words("one") == 1
    assert count_words("  multiple   spaces   between   words  ") == 4
    assert count_words("trailing space ") == 2
    assert count_words(" leading space") == 2
    assert count_words("mixed   spacing   and\nnewlines") == 4