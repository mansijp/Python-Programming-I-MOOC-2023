
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "src/students1.csv"
    exercise_data = "src/exercises1.csv"

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
        e[parts[0]] = (int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]), int(parts[6]), int(parts[7]))

for k in s:
    print(s[k], sum(e[k]))