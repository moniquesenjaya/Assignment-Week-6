def average_length(filename):
    length = []
    f = open(filename, 'r', encoding = 'utf-8')
    # Split the words and store its length in a list
    for word in f.read().split():
        length.append(len(word))

    # Finding out the average
    for i in length:
        avg = sum(length)/len(length)
    return avg

print(average_length('file.txt'))