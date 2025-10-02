def unique_elements(nested_list):

    def flatten(lst):
        result = []
        for item in lst:
            if type(item) is list:
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    flat_list = flatten(nested_list)
    print(f"flatted list: {flat_list}")
    
    seen = set()
    unique_list = []
    for i in flat_list:
        if i not in seen:
            unique_list.append(i)
            seen.add(i)
    
    return unique_list

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
print(f"source: {list_a}")
result = unique_elements(list_a)
print(f"unique elments: {result}")