def flatted_list(lst):
    i = 0
    while i < len(lst):
        if type(lst[i]) is list:
            flatted_list(lst[i])
            sublist = lst[i]
            del lst[i]
            for j in range(len(sublist)):
                lst.insert(i + j, sublist[j])
            i += len(sublist)
        else:
            i += 1

list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print("source list:")
print(list_a)

flatted_list(list_a)

print("\nflatted list:")
print(list_a)