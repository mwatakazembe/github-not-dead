input = input("input your strong to compress: ")

current = None
count = 0
parts = []

for i in input:
    if i == current:
        count += 1
    else:
        if current is not None:
            parts.append(current + str(count))
        current = i
        count = 1

if current is not None:
    parts.append(current + str(count))

compressed = "".join(parts)
print(f"the string: {compressed}")