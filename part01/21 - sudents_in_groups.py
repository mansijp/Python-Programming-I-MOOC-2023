# Write your solution here
stds = int(input("How many students on the course? "))
size = int(input("Desired group size? "))

print("Number of groups formed: " + str((stds + size - 1) // size))
