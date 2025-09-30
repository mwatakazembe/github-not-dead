str = input("Enter string: ")
checking = "aeiou"
res = ""

for char in str:
    if char.lower() not in checking:
        res += char

print(res)