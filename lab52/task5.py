def combine_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            if isinstance(result[key], list) and isinstance(value, list):
                result[key].extend(value)
            elif isinstance(result[key], list):
                result[key].append(value)
            elif isinstance(value, list):
                result[key] = [result[key]] + value
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value
    return result

def test_combine_dicts_no_overlap():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    assert combine_dicts(dict1, dict2) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def test_combine_dicts_with_overlap():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    assert combine_dicts(dict1, dict2) == {'a': 1, 'b': [2, 3], 'c': 4}

def test_combine_dicts_empty_first():
    dict1 = {}
    dict2 = {'a': 1, 'b': 2}
    assert combine_dicts(dict1, dict2) == {'a': 1, 'b': 2}

def test_combine_dicts_empty_second():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {}
    assert combine_dicts(dict1, dict2) == {'a': 1, 'b': 2}

def test_combine_dicts_both_empty():
    dict1 = {}
    dict2 = {}
    assert combine_dicts(dict1, dict2) == {}

def test_combine_dicts_multiple_overlap():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'a': 4, 'b': 5, 'd': 6}
    assert combine_dicts(dict1, dict2) == {'a': [1, 4], 'b': [2, 5], 'c': 3, 'd': 6}

def test_combine_dicts_with_lists():
    dict1 = {'a': [1, 2], 'b': 3}
    dict2 = {'a': [4, 5], 'b': [6, 7]}
    assert combine_dicts(dict1, dict2) == {'a': [1, 2, 4, 5], 'b': [3, 6, 7]}

def test_combine_dicts_nested_structures():
    dict1 = {'a': {'x': 1}, 'b': 2}
    dict2 = {'a': {'y': 3}, 'b': 4}
    assert combine_dicts(dict1, dict2) == {'a': [{'x': 1}, {'y': 3}], 'b': [2, 4]}