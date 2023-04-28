lim = int(input("Limit: "))
sum = 0
count = 0

while sum < lim:
    sum += count
    count += 1 

string = ""
i = 1
while i < (count-1):
    string = string + str(i) + " + "    
    i += 1

string = string + str(i) + " = "
print("The consecutive sum: " + string + str(sum))