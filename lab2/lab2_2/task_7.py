def merge_sorted_list(list1, list2):

    result = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    while i < len(list1):
        result.append(list1[i])
        i += 1
    
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result

input1 = input("enter the elements of the first sorted list separated by spaces: ").split()
list1 = [int(i) for i in input1]

input2 = input("Enter the elements of the second sorted list separated by spaces:").split()
list2 = [int(i) for i in input2]

print(f"\nfirst list: {list1}")
print(f"second list: {list2}")

merged = merge_sorted_list(list1, list2)
print(f"\nmerged list: {merged}")