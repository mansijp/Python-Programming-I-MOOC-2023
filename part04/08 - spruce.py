def spruce(n):
    print("a spruce!")
    counter = 1
    str = ""

    for i in range(1, n+1):
        str += " " * ((n*2 - 1 - counter)//2)
        str += "*" * (counter)
        counter += 2

        print(str)
        str = ""

    str = " "*((n*2 - 1)//2) 
    str += "*"
    print(str)

if __name__ == "__main__":
    spruce(5)