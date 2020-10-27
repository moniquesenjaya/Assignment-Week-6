def hapax(filename):
    result = []
    flat_list = []
    f = open(filename, 'r', encoding = 'utf-8')
    # Split the file and store only words in a list
    for word in f.read().split():
        flat_list.append(word)
    word_dict = {}
    # Check for every word in the list, if the word is in dictionary, add 1 to the value, if not, make word as key
    # casefold and lower make sure that it is not case sensitive
    for word in flat_list:
        if word.casefold() not in word_dict:
            word_dict[word.lower()] = 1
        else:
            word_dict[word.lower()] += 1
    # Run through the dictionary to check which keys have a value of 1 and append to a list
    for (key,value) in word_dict.items():
        if value == 1:
            result.append(key)
    return result

print(hapax("file.txt"))