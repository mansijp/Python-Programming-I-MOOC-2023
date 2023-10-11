if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    # hard-coded input
    student_info = "src/students1.csv"
    exercise_data = "src/exercises1.csv"
    exam_points = "src/exam_points1.csv"

s = {}
with open(student_info) as stds:
    next(stds)
    for line in stds:
        line = line.strip()
        parts = line.split(";")
        s[parts[0]] = f"{parts[1]} {parts[2]}"

e = {}
with open(exercise_data) as exc:
    next(exc)
    for line in exc:
        line = line.strip()
        parts = line.split(";")
        temp = [int(i) for i in parts[1:]]
        e[parts[0]] = sum(temp)//4

pts = {}
with open(exam_points) as exm:
    next(exm)
    for line in exm:
        line = line.strip()
        parts = line.split(";")
        temp = [int(i) for i in parts[1:]]
        pts[parts[0]] = sum(temp)

for k in s:
    if (pts[k] + e[k]) >= 0 and (pts[k] + e[k]) <= 14:
        print(s[k], 0)
    elif (pts[k] + e[k]) >= 15 and (pts[k] + e[k]) <= 17:
        print(s[k], 1) 
    elif (pts[k] + e[k]) >= 18 and (pts[k] + e[k]) <= 20:
        print(s[k], 2)
    elif (pts[k] + e[k]) >= 21 and (pts[k] + e[k]) <= 23:
        print(s[k], 3)
    elif (pts[k] + e[k]) >= 24 and (pts[k] + e[k]) <= 27:
        print(s[k], 4)
    elif (pts[k] + e[k]) >= 28:
        print(s[k], 5)