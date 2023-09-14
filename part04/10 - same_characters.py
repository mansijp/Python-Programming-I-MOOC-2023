
def same_chars(text, i, j):
    if i > (len(text) - 1) or j > (len(text) - 1):
        return False
    if (text[i] == text[j]):
        return True
    else:
        return False

if __name__ == "__main__":
    print(same_chars("coder", 1, 2))