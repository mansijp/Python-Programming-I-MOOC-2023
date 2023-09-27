answer = ""
examPts = []
exercises = []
exercisePts = []
fails = 0
grades = [0] * 6

while True:
    answer = input("Exam points and exercises completed: ")
    if answer == "":
        break
    examPts.append(int((answer.split())[0]))
    exercises.append(int((answer.split())[1]))
    exercisePts.append((exercises[-1] - (exercises[-1] % 10)) / 10)
    totalPts = exercisePts[-1] + examPts[-1]    

    if examPts[-1] < 10:
            grades[0] += 1
    else:
        if totalPts <= 14 and totalPts >= 0:
            grades[0] += 1
        elif totalPts <= 17:
            grades[1] += 1
        elif totalPts <= 20:
            grades[2] += 1
        elif totalPts <= 23:
            grades[3] += 1
        elif totalPts <= 27:
            grades[4] += 1
        elif totalPts <= 30:
            grades[5] += 1

average = (sum(exercisePts) + sum(examPts)) / len(examPts)

print("Statistics:")
print(f"Points average: {average:.1f}")
print(f"Pass percentage: {100 - (grades[0]/len(examPts)*100):.1f}")
print("Grade distribution:")
output = ""
for i in range(5, -1, -1):
    output = (f"  {i}: ") + "*" * grades[i]
    print(output)

