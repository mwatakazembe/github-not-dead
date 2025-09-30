from random import randint

num = randint(1, 100)
inputNum = None

while inputNum != num:
    inputNum = int(input("input the number: "))
    
    if inputNum > num:
        print("try less")
    elif inputNum < num:
        print("try more.")
    else:
        print("that's it")