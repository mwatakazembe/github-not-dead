text = input("input text: ").lower()

words = []
current_word = []
in_word = False

for i in text:
    if i == ' ' or i == '\n':
        if in_word:
            words.append(''.join(current_word))
            current_word = []
            in_word = False
    else:
        current_word.append(i)
        in_word = True

if in_word:
    words.append(''.join(current_word))

word_count = {}
for word in words:
    if word:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

unique_count = len(word_count)

print("frequency dict:")
for word, count in word_count.items():
    print(f"{word}: {count}")

print(f"\nnum of unique words: {unique_count}")