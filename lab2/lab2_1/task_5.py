word1 = input("input the first word: ").lower()
word2 = input("input the second word: ").lower()

if len(word1) != len(word2):
    print(False)
else:
    count = {}
    
    for i in word1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    for i in word2:
        if i in count:
            count[i] -= 1
        else:
            print(False)
            break
    else:
        for i in count.values():
            if i != 0:
                print(False)
                break
        else:
            print(True)