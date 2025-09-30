number = int(input("enter num (under 1000): "))

if number % 7 == 0:
    print("magick number!")
else:
    n = abs(number)
    
    d1 = n // 100
    d2 = (n // 10) % 10
    d3 = n % 10

    digitSum = d1 + d2 + d3
    
    print("sum of digits: " + str(digitSum))