import numpy as np 

lengths = np.array([20, 8, 9, 18, 5, 12, 16, 16, 6, 7])
speeds = np.array([44, 70, 44, 66, 46, 38, 38, 37, 66, 67])

k = int(input("k: "))
p = int(input("p: "))

selected_lengths = lengths[k:p+1]
selected_speeds = speeds[k:p+1]

s = np.sum(selected_lengths)
t = np.sum(selected_lengths / selected_speeds)
v = s / t

print(f"S = {s:.2f} km, T = {t:.2f} hour, V = {v:.2f} km/h")