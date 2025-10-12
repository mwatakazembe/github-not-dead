R = 8.31
p = int(input("pressure (Pa): "))
V = int(input("volume (m^3): "))
T = int(input("temperature (K): "))

nu = (p * V) / (R * T)
print(f"amount of gas = {nu} mol")