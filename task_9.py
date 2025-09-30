IP = input("enter IP: ")
parts = IP.split(".")

correct = True
if len(parts) == 4:
    for part in parts:
        num = int(part)
        if num < 0 or num > 255:
            correct = False
            break
else:
    correct = False

print("correct" if correct else "incorrect")