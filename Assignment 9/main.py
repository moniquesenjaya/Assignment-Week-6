f = open("file.txt", "r", encoding = 'utf-8')
words = f.read().split()
counter = -1
for word in words:
    counter += 1
    if "?" in word or "!" in word:
        if counter+1 < len(words):
            words[counter+1] = "\n" + words[counter+1]
    if word[-1] == ".":
        if word == "Mr." or word == "Mrs." or word == "Dr." or word == "Jr." or word == "Ms.":
            pass
        elif counter+1 < len(words):
            if words[counter+1][0].isupper():
                words[counter+1] = "\n" + words[counter+1]
        else:
            pass
print(" ".join(words))

