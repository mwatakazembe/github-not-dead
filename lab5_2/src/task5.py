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