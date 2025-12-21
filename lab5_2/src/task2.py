def find_unique(elements):
    count = {}
    for element in elements:
        count[element] = count.get(element, 0) + 1
    return [element for element in elements if count[element] == 1]