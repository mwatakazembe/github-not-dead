n = int(input("enter num: "))

if n % 7 == 0:
    print("magick number!")
else:
    sum = sum(int(d) for d in str(abs(n)))
    print(f"sum of numbers = {sum}")