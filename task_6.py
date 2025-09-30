R = 8.31
p = int(input("pressure: "))
V = int(input("volume: "))
T = int(input("temperature: "))

nu = (p * V) / (R * T)
print(f"amount of gas = {nu}")