def merge_dicts(dict_a, dict_b):
    for key in dict_b:
        if key not in dict_a:
            dict_a[key] = dict_b[key]
        else:
            merge_values(dict_a, key, dict_b[key])

def merge_values(dict_a, key, value_b):
    value_a = dict_a[key]
    
    if type(value_a) == type({}) and type(value_b) == type({}):
        merge_dicts(value_a, value_b)
    elif type(value_a) == type([]) and type(value_b) == type([]):
        for item in value_b:
            value_a.append(item)
    elif type(value_a) == type(set()) and type(value_b) == type(set()):
        for item in value_b:
            value_a.add(item)
    elif type(value_a) == type(()) and type(value_b) == type(()):
        dict_a[key] = value_a + value_b
    else:
        dict_a[key] = value_b


dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

print("before merge:")
print("dict_a =", dict_a)
print("dict_b =", dict_b)

merge_dicts(dict_a, dict_b)

print("\nafter merge:")
print("dict_a =", dict_a)