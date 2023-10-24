import string
from random import randint, choice

def generate_strong_password(length : int, numbers : bool, specialChar : bool):  
    res = ''
    lower = False
    num = False
    special = False
    selection = string.ascii_lowercase
    
    if (numbers):
        selection += string.digits
    if (specialChar):
        selection += '!?=+-()#'

    for i in range(length):
        c = choice(selection)
        if (c in string.ascii_lowercase):
            lower = True
        elif c in string.digits:
            num = True
        elif c in '!?=+-()#':
            special = True
        res += c
    
    res = list(res)
    if not lower:
        res[randint(0, len(res)-1)] = choice(string.ascii_lowercase)
    if not num and numbers:
        res[randint(0, len(res)-1)] = choice(string.digits)
    if not special and specialChar:
        res[randint(0, len(res)-1)] = choice('!?=+-()#')
    res = ''.join(res)

    return(res)
    
def main():
    for i in range(5):
        print(generate_strong_password(2, False, False))
