def merge_dicts(a, b):
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_dicts(a[key], b[key])
            elif isinstance(a[key], list) and isinstance(b[key], list):
                a[key].extend(b[key])
            elif isinstance(a[key], set) and isinstance(b[key], set):
                a[key].update(b[key])
            elif isinstance(a[key], tuple) and isinstance(b[key], tuple):
                a[key] = a[key] + b[key]
            else:
                a[key] = b[key]
        else:
            a[key] = b[key]


dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

print("before merge:")
print("dict_a =", dict_a)
print("dict_b =", dict_b)

merge_dicts(dict_a, dict_b)

print("\nafter merge:")
print("dict_a =", dict_a)