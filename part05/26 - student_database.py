#---------------- ADD STUDENT ----------------
def add_student(students: dict, name: str):
    students[name] = []

#---------------- PRINT STUDENT ----------------
def print_student(students: dict, name: str):
    for i in students:
        if i == name:
            print(f"{i}: ")
            if students[name] == []:
                print(" no completed courses")
            else:
                print(f" {len(students[name])} completed courses:")
                grade = 0
                for i in students[name]:
                    print(" ", i[0], i[1])
                    grade += i[1]
                print(f" average grade {grade/len(students[name])}")
            return
    print(f"{name}: no such person in the database")

#---------------- ADD COURSE ----------------
def add_course(students: dict, name: str, course: tuple):
    # course is a tuple: (course name, grade)
  
    for i in students[name]:
        if i[0] == course[0]:
            if course[1] > i[1]:
                students[name].remove(i)
                students[name].append((course[0], course[1]))
                return
            else:
                return

    if course[1] == 0:
        return
    else:        
        students[name].append(course)

#---------------- SUMMARY ----------------
def summary(students: dict):
    avgGrade = {}
    mostCourses = {}
    grade = 0
    for i in students:
        for j in students[i]:
            grade += j[1]
        avgGrade[grade/len(students[i])] = i
        mostCourses[len(students[i])] = i
        grade = 0

    print(f"students {len(students)}")
    print(f"most courses completed {max(mostCourses)} {mostCourses[max(mostCourses)]}")
    print(f"best average grade {max(avgGrade)} {avgGrade[max(avgGrade)]}")

#------------------------ MAIN ------------------------
def main():
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)


