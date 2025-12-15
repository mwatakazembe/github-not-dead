import numpy as np

expenses = np.array([float(input(f"enter expenses for month {i+1}: ")) for i in range(12)])

winter_months = [11, 0, 1]
summer_months = [5, 6, 7]

winter_total = np.sum(expenses[winter_months])
summer_total = np.sum(expenses[summer_months])

if winter_total > summer_total:
    print("more money spent in winter")
elif summer_total > winter_total:
    print("more money spent in summer")
else:
    print("winter and summer expenses are equal")

max_expense = np.max(expenses)
max_months = np.where(expenses == max_expense)[0] + 1

print("months with highest expenses:", ' '.join(map(str, max_months)))