BASE_PRICE = 24.99
INCL_MIN = 60
INCL_SMS = 30
INCL_MB = 1024

PRICE_PER_MIN = 0.89
PRICE_PER_SMS = 0.59
PRICE_PER_MB = 0.79

TAX_RATE = 0.02

min = int(input("amount of minutes: "))
sms = int(input("amount of sms: "))
internet = float(input("internet (MB): "))

print(f"tariff: {BASE_PRICE:.2f}")

addMin = min - INCL_MIN
addSMS = sms - INCL_SMS
addInternet = internet - INCL_MB

total = 0

if addMin > 0:
    costMin = addMin * PRICE_PER_MIN
    print(f"price for add. minutes: {costMin:.2f}")
    total += costMin

if addSMS > 0:
    costSMS = addSMS * PRICE_PER_SMS
    print(f"price for add. sms: {costSMS:.2f}")
    total += costSMS

if addInternet > 0:
    costInternet = addInternet * PRICE_PER_MB
    print(f"price for add. internet: {costInternet:.2f}")
    total += costInternet

subtotal = BASE_PRICE + total
tax = subtotal * TAX_RATE
total = subtotal + tax

print(f"tax: {tax:.2f}")
print(f"total: {total:.2f}")