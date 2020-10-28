f = open("file.txt", "r", encoding = 'utf-8')
titles = ["Mr.", "Ms.", "Dr.", "Mrs.", "Jr."]
words = f.read().split()
counter = -1
for word in words:
    counter += 1
    if "?" in word or "!" in word:
        if counter+1 < len(words):
            words[counter+1] = "\n" + words[counter+1]
    if word[-1] == ".":
        if word in titles:
            pass
        elif counter+1 < len(words):
            if words[counter+1][0].isupper():
                words[counter+1] = "\n" + words[counter+1]
print(" ".join(words))

