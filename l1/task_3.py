password = input("enter the password: ")
if len(password) > 16:
    if password.isalpha() or password.isdigit():
        print("weak")
    else:
        print("strong")
else:
    print("too short")