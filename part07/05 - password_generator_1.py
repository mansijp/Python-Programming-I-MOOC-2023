import string
from random import randint

def generate_password(length : int):
    res = ''
    for i in range(length):
        res += string.ascii_letters[randint(0, 25)]
    return(res)

def main():
    for i in range(10):
        print(generate_password(8))
