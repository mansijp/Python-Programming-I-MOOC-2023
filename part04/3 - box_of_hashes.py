def line(n, text):
    if len(text) >=1:
        print(text[0]*n)
    else:
        print("*"*n)

def box_of_hashes(height):
    for i in range(height):
        line(10, "#")

if __name__ == "__main__":
    box_of_hashes(5)
