def largest():
    with open("src/numbers.txt") as newFile:
        n = int(newFile.readline())
        for line in newFile:
            if int(line) > n:
                n = int(line)
    return (n)

def main():
    print(largest())
