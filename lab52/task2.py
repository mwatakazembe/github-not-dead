def find_unique(elements):
    count = {}
    for element in elements:
        count[element] = count.get(element, 0) + 1
    return [element for element in elements if count[element] == 1]

def test_empty_list():
    assert find_unique([]) == []

def test_single_element():
    assert find_unique([5]) == [5]

def test_all_duplicates():
    assert find_unique([1, 1, 2, 2, 3, 3]) == []

def test_mixed_elements():
    assert find_unique([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]

def test_strings():
    assert find_unique(['a', 'b', 'a', 'c', 'd', 'd']) == ['b', 'c']

def test_mixed_types():
    assert find_unique([1, 'a', 1, 'b', 'a']) == ['b']