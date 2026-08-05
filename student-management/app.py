students = []


def add_student(name):
    students.append(name)


def view_students():
    if not students:
        print("No students found.")
    else:
        print("\nStudent List")
        print("------------")
        for student in students:
            print(student)


add_student("Alice")
add_student("Bob")

print("Student Management System - V1")
view_students()


def search_student(name):
    if name in students:
        print(f"{name} found.")
    else:
        print(f"{name} not found.")
        search_student("Alice")


search_student("John")
