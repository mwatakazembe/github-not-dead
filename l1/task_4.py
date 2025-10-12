sum = int(input("amount of money: "))

banknote100 = sum // 100
remain = sum % 100

banknote50 = remain // 50
remain = remain % 50

banknote10 = remain // 10
remain = remain % 10

banknote5 = remain // 5
remain = remain % 5

banknote2 = remain // 2
banknote1 = remain % 2

print("you'll need banknotes of:")
print(f"100: {banknote100}")
print(f"50: {banknote50}")
print(f"10: {banknote10}")
print(f"5: {banknote5}")
print(f"2: {banknote2}")
print(f"1: {banknote1}")