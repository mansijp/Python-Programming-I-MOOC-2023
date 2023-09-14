
def first_word(text):
    arr = text.split(" ")
    return arr[0]

def second_word(text):
    arr = text.split(" ")
    return arr[1]

def last_word(text):
    arr = text.split(" ")
    return arr[-1]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))