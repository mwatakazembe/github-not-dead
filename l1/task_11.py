day = int(input("enter day: "))
month = int(input("enter month: "))

if month == 1:
    if day <= 19:
        print("capricorn")
    else:
        print("aquarius")
elif month == 2:
    if day <= 18:
        print("aquarius")
    else:
        print("pisces")
elif month == 3:
    if day <= 20:
        print("pisces")
    else:
        print("aries")
elif month == 4:
    if day <= 19:
        print("aries")
    else:
        print("taurus")
elif month == 5:
    if day <= 20:
        print("taurus")
    else:
        print("gemini")
elif month == 6:
    if day <= 21:
        print("gemini")
    else:
        print("cancer")
elif month == 7:
    if day <= 22:
        print("cancer")
    else:
        print("leo")
elif month == 8:
    if day <= 22:
        print("leo")
    else:
        print("virgo")
elif month == 9:
    if day <= 22:
        print("virgo")
    else:
        print("libra")
elif month == 10:
    if day <= 22:
        print("libra")
    else:
        print("scorpio")
elif month == 11:
    if day <= 21:
        print("scorpio")
    else:
        print("sagittarius")
elif month == 12:
    if day <= 21:
        print("sagittarius")
    else:
        print("capricorn")