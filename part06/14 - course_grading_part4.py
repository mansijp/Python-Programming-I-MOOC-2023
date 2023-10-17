if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
    course_name = input("Course information:")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"
    course_name = "course1.txt"

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

with open(course_name) as courseFile:
    head = []
    for line in courseFile:
        line = line.strip()
        head.append(line.split(': ')[1])

    with open("results.txt", "w") as file:
        header = f"{head[0]}, {head[1]} credits\n"
        file.write(header)
        file.write("="*(len(header)-1) + "\n")
        file.write(f"{str('name'):30}{str('exec_nbr'):10}{str('exec_pts.'):10}{str('exm_pts.'):10}{str('tot_pts.'):10}{str('grade'):10}\n")
        
        with open("results.csv", "w") as csvFile:

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

                file.write(f"{s[k]:30}{e[k][0]:<10}{e[k][1]:<10}{pts[k]:<10}{(pts[k]+e[k][1]):<10}{grade:<10}\n")
                csvFile.write(f"{k};{s[k]};{grade}\n")
