f = open("Assignment 6/text.txt", "r")
n = open("Assignment 6/new.txt","w+")
counts = 1
for x in f.readlines():
    n.write(str(counts) + " " + x)
    counts += 1