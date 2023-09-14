def palindromes(input : str):    
    if(input[::-1] == input):
        return True
    else:
        return False
    

while True:
    testPalindrome = input("Please type in a palindrome: ")
    if palindromes(testPalindrome):
        print(f"{testPalindrome} is a palindrome!")
        break
    print("that wasn't a palindrome")