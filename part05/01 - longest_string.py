def longest(strings: list):
    longest = ""
    for i in strings:
        if len(i) > len(longest):
            longest = i
    return longest

if __name__ == "__main__":
    longest(["hi", "hiya", "hello", "howdydoody", "hi there"])