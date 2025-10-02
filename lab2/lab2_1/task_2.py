numbers = []
for i in input("enter numbers separated by spaces: ").split():
    numbers.append(float(i))


unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("unique numbers:", unique)


duplicates = []
seen = []
for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    seen.append(num)
print("duplicate numbers:", duplicates)


even = []
odd = []
for num in numbers:
    if num == int(num):
        int_num = int(num)
        if int_num % 2 == 0:
            even.append(int_num)
        else:
            odd.append(int_num)
print("even numbers:", even)
print("odd numbers:", odd)


negative = []
for num in numbers:
    if num < 0:
        negative.append(num)
print("negative numbers:", negative)


floats = []
for num in numbers:
    if num != int(num):
        floats.append(num)
print("floating point numbers:", floats)


sum_5 = 0
for num in numbers:
    if num % 5 == 0:
        sum_5 += num
print("sum of numbers divisible by 5:", sum_5)


max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("maximum number:", max_num)


min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
print("minimum number:", min_num)