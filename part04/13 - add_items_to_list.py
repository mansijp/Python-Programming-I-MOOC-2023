n = int(input("How many items: "))
arr = []

for i in range(1, n+1):
    arr.append(int(input(f"Item {i}: ")))

print(arr)