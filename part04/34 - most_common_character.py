# my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
# print(my_string.count("ch"))
    # output: 5

# new_string = "Hi there"".replace("Hi", "Hey")
    # output: Hey there

def most_common_character(myString : str):
    occurrence = 0
    resultChar = ""
    for i in myString:
        if myString.count(i) > occurrence:
            occurrence = myString.count(i)
            resultChar = i
    return (resultChar)
