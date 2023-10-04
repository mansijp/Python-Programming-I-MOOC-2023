# deleting key value pair
    # del dictionary[key]
    # deleted = dictionary.pop(key)
    # dictionary.clear()

def invert(dictionary: dict):
    value = []
    key = []
    for i in dictionary:
        value.append(dictionary[i])
        key.append(i)
    dictionary.clear()
    for i in range(len(key)):
        dictionary[value[i]] = key[i]
    print(dictionary)

def main():
    invert({1: "first", 2: "second", 3: "third", 4: "fourth"})