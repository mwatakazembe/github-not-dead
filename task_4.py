sum = int(input("amount of money: "))
for i in [100, 50, 20, 10, 5, 2, 1]:
    count = sum // i
    print(f"{i}: {count}")
    sum %= i