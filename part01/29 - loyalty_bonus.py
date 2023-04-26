pts = int(input("How many points are on your card? "))

if(pts >= 100):
    print("Your bonus is 15%")
    print(f"You now have {pts*1.15} points")
elif pts < 100:
    print("Your bonus is 10%")
    print(f"You now have {pts*1.1} points")