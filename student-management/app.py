students = []


# -----------------------------
# Functions
# -----------------------------

def load_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                students.append(line.strip())
        print("Students loaded successfully.")
    except FileNotFoundError:
        print("students.txt not found. Starting with an empty list.")


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


def search_student(name):
    if name in students:
        print(f"{name} found.")
    else:
        print(f"{name} not found.")


def update_student(old_name, new_name):
    if old_name in students:
        index = students.index(old_name)
        students[index] = new_name
        print(f"{old_name} updated to {new_name}")
    else:
        print(f"{old_name} not found")


def delete_student(name):
    if name in students:
        students.remove(name)
        print(f"{name} deleted successfully")
    else:
        print(f"{name} not found")


def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(student + "\n")
    print("Students saved successfully.")


# -----------------------------
# Main Program
# -----------------------------

load_students()

add_student("Alice")
add_student("Bob")

print("Student Management System - V1")
view_students()

search_student("Alice")
search_student("John")

update_student("Bob", "Robert")

print("\nUpdated Student List")
view_students()

delete_student("Alice")

print("\nFinal Student List")
view_students()

save_students()
