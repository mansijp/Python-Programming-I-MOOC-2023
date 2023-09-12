def chessboard(n):
    string = ""
    for i in range(1, n+1):
        for j in range(1, n+1):
            if((i+j)%2 == 0):
                string += "1"
            else:
                string += "0"
        print(string)
        string = ""


if __name__ == "__main__":
    chessboard(6)
