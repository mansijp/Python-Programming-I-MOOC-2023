# Write your solution here

divider = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
money = float(input("How much money do you spend on groceries in a week? "))

print("Average god expenditure:")
print("Daily: " + str((divider*price + money)/7) + " euros")
print("Weekly: " + str(divider*price + money) + " euros")