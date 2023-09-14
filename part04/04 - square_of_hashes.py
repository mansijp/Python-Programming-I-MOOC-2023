def line(n, text):
    if len(text) >=1:
        print(text[0]*n)
    else:
        print("*"*n)

def square_of_hashes(size):
    for i in range(size):
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
