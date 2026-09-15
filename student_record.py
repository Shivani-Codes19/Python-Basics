students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records:")

        for student in students:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("----------------")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
