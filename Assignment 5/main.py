def hapax(filename):
    result = []
    flat_list = []
    f = open(filename, 'r', encoding = 'utf-8')
    for word in f.read().split():
        flat_list.append(word)
    word_dict = {}
    for word in flat_list:
        if word.casefold() not in word_dict:
            word_dict[word.lower()] = 1
        else:
            word_dict[word.lower()] += 1
    for (key,value) in word_dict.items():
        if value == 1:
            result.append(key)
    return result

print(hapax("file.txt"))