ip = input("input IP: ")
parts = ip.split('.')

if len(parts) != 4:
    print("correct")
else:
    correct = True
    
    if not parts[0].isdigit() or int(parts[0]) < 0 or int(parts[0]) > 255 or (len(parts[0]) > 1 and parts[0][0] == '0'):
        correct = False
    
    elif not parts[1].isdigit() or int(parts[1]) < 0 or int(parts[1]) > 255 or (len(parts[1]) > 1 and parts[1][0] == '0'):
        correct = False
    
    elif not parts[2].isdigit() or int(parts[2]) < 0 or int(parts[2]) > 255 or (len(parts[2]) > 1 and parts[2][0] == '0'):
        correct = False
    
    elif not parts[3].isdigit() or int(parts[3]) < 0 or int(parts[3]) > 255 or (len(parts[3]) > 1 and parts[3][0] == '0'):
        correct = False
    
    print("correct" if correct else "incorrect")