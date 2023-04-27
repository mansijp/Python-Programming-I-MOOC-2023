l1 = input("1st letter: ")
l2 = input("2nd letter: ")
l3 = input("3rd letter: ")

if l1 < l2 and l2 < l3:
    print("The letter in the middle is " + l2)
elif l2 < l1 and l1 < l3:
    print("The letter in the middle is " + l1)
elif l1 < l3 and l3 < l2:
    print("The letter in the middle is " + l3)
elif l3 < l1 and l1 < l2:
    print("The letter in the middle is " + l1)
elif l3 < l2 and l2 < l1:
    print("The letter in the middle is " + l2)
elif l2 < l3 and l3 < l1:
    print("The letter in the middle is " + l3)
