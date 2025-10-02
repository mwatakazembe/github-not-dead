input1 = input("enter the first set of numbers (separated by a space): ").split()
input2 = input("enter the second set of numbers (separated by a space): ").split()

set1 = {float(i) for i in input1}
set2 = {float(i) for i in input2}

common = set1 & set2
first_only = set1 - set2
second_only = set2 - set1
common_except = set1 ^ set2

print("common nums:", common)
print(f"first only nums: {first_only}\nsecond only nums: {second_only}")
print("common except nums:", common_except)