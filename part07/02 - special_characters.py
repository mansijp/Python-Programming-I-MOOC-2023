# use dir(math) to see all the methods in the library

import string

def separate_characters(my_string: str):
    a = ''
    b = ''
    c = ''
    for i in my_string:
        if (i in string.ascii_letters):
            a += i
        elif (i in string.punctuation):
            b += i
        else:
            c += i
    return((a, b, c))


def main():
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
