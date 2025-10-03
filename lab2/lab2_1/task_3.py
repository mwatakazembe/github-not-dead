input = input("enter numbers separated by spaces: ")
parts = input.split()

numbers = []
for part in parts:
    numbers.append(float(part))

if len(numbers) < 2:
    print("not enough numbers to find second largest")
else:
    first = numbers[0]
    second = numbers[1]
    
    if second > first:
        t = first      
        first = second  
        second = t
    
    for i in range(2, len(numbers)):
        num = numbers[i]
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    if second == first:
        diff = False
        for num in numbers:
            if num != first:
                diff = True
                break
        
        if diff:
            second = None
            for num in numbers:
                if num != first and (second is None or num > second):
                    second = num
        else:
            second = None
    
    if second is None:
        print("second largest number does not exist")
    else:
        print("second largest number:", second)