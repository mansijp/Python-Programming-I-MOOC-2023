def read_fruits():
    d = {}
    with open("src/fruits.csv") as fruits:
        print(fruits)
        for line in fruits:
            line = line.replace("\n","")
            temp = line.split(";")
            d[temp[0]] = float(temp[1])
    return(d)

def main():
    print(read_fruits)
