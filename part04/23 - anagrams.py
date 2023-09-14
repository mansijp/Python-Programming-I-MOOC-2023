def anagrams(strA, strB):
    if sorted(strA) == sorted(strB):
        return True
    else:
        return False