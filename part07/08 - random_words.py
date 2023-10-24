from random import randint, choice

def words(n: int, beginning: str):
    temp = []
    counter = n
    res = []
    with open('words.txt') as file:
        for line in file:
            line = line.strip('\n')
            if (line.startswith(beginning)):
                temp.append(line)

        if len(temp) < n:
            raise(ValueError)
        
        for i in range(n):
            res.append(choice(temp))

        return(res)

def main():
    print(words(5, 'car'))


