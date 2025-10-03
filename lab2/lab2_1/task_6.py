input = input("enter list items separated by spaces: ")

input_list = input.split()

result = []
for item in input_list:
    if item not in result:
        result.append(item)

print("no duplicates list:", result)