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
        tup = (sum(temp), sum(temp)//4)
        e[parts[0]] = tup

pts = {}
with open(exam_points) as exm:
    next(exm)
    for line in exm:
        line = line.strip()
        parts = line.split(";")
        temp = [int(i) for i in parts[1:]]
        pts[parts[0]] = sum(temp)

print(f"{str('name'):30}{str('exec_nbr'):10}{str('exec_pts.'):10}{str('exm_pts.'):10}{str('tot_pts.'):10}{str('grade'):10}")

for k in s:
    grade = 0
    if (pts[k] + e[k][1]) >= 0 and (pts[k] + e[k][1]) <= 14:
        grade = 0
    elif (pts[k] + e[k][1]) >= 15 and (pts[k] + e[k][1]) <= 17:
        grade = 1
    elif (pts[k] + e[k][1]) >= 18 and (pts[k] + e[k][1]) <= 20:
        grade = 2
    elif (pts[k] + e[k][1]) >= 21 and (pts[k] + e[k][1]) <= 23:
        grade = 3
    elif (pts[k] + e[k][1]) >= 24 and (pts[k] + e[k][1]) <= 27:
        grade = 4
    elif (pts[k] + e[k][1]) >= 28:
        grade = 5

    print(f"{s[k]:30}{e[k][0]:<10}{e[k][1]:<10}{pts[k]:<10}{(pts[k]+e[k][1]):<10}{grade:<10}")