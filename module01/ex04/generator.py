import random

def shuffle(my_list):
    random.seed()
    list_len = len(my_list)
    list_indexes = [i for i in range(0, list_len)]
    new_list = []
    while len(new_list) != list_len:
        n = random.randint(0, list_len - 1)
        if n in list_indexes:
            new_list.append(my_list[n])
            list_indexes.remove(n)
    return new_list

def unique(my_list):
    new_list = []
    for e in my_list:
        if e not in new_list:
            new_list.append(e)
    return new_list

def ordered(my_list):
    new_list = my_list
    new_list.sort()
    return new_list

def generator(text, sep=" ", option=None):
    if type(text) != str or (type(option) != str and option != None):
        print("ERROR")
    else:
        options = ['shuffle', 'unique', 'ordered']
        if option in options:
            fctArray = [shuffle, unique, ordered]
            return fctArray[options.index(option)](text.split(sep))
        else:
            return text.split(sep)

if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."
    print("Sans option: ")
    for word in generator(text):
        print(word)
    print("Shuffle: ")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print("Ordered: ")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print("Unique: ")
    for word in generator(text, sep=" ", option="unique"):
        print(word)
