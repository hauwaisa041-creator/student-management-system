import json

STUDENT_FILE = "students.json"

def load_students():
    try:
        with open(STUDENT_FILE, "r")as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

    except json.JSONDecodeError:
        print("saved student file has an error. starting with no student.")
        return[]

def save_student(student_list):
    with open(STUDENT_FILE, "w")as file:
        json.dump(student_list, file, indent= 4)

students = load_students()

def print_menu():
    print("\n==============================")
    print("STUDENT MANAGEMENT SYSTEN")
    print("==============================")
    print("1. add a student")
    print("2. view all student")
    print("3. search by ID or name")
    print("4. update a student")
    print("5. delete a student")
    print("6. view statistics")
    print("7. exit")

def add_student():
    student_id = input("enter student ID: ")
    name = input("Full name: ")
    age = input("enter age: ")
    gender = input("Gender: ")
    student_class = input("Class: ")
    score = input("enter score: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "gender": gender,
        "class": student_class,
        "score": score
    }

    students.append(student)
    save_student(students)
    
    print("student added successfully!")

def view_students():
    if len(students) == 0:
        print("no students have been added yet.")
        return

    print("\nALL STUDENTS")

    for student in students:
        print("\n-------------------------")
        print("student ID:", student["id"])
        print("name:", student["name"])
        print("age:", student["age"])
        print("gender:", student["gender"])
        print("class:", student["class"])
        print("score:", student["score"])

def search_student():
    search_name = input("enter student ID or name to search: ").lower()

    found = False

    for student in students:
        student_id = student["id"].lower()
        student_name = student["name"].lower()

        if search_name == student_id or search_name in student_name:
            print("\n----------------------")
            print("student ID:", student["id"])
            print("name:", student["name"])
            print("age:", student["age"])
            print("gender:", student["gender"])
            print("class:", student["class"])
            print("score:", student["score"])

            found = True

    if found == False:
        print("no student was found.")

def update_student():
    student_id = input("Enter student ID to update: ")

    for student in students:
        if student["id"].lower() == student_id.lower():

            print("\nCurrent student information")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Gender:", student["gender"])
            print("Class:", student["class"])
            print("Score:", student["score"])

            print("\nEnter the new information")
            student["name"] = input("New name: ")
            student["age"] = input("New age: ")
            student["gender"] = input("New gender: ")
            student["class"] = input("New class: ")
            student["score"] = input("New score: ")

            save_student(students)

            print("Student updated successfully!")
            return

def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"].lower() == student_id.lower():
            confirmation = input(
                f"Delete {student['name']}? Type yes to confirm: "
            ).lower()

            if confirmation == "yes":
                students.remove(student)
                save_student(students)
                print("Student deleted successfully!")

            else:
                print("Deletion cancelled.")
            return

def show_statistics():
    if len(students) == 0:
        print("No students have been added yet.")
        return

    scores = []

    for student in students:
            try:
                score = float(student["score"])
                scores.append(score)
    
            except ValueError:
                print(f"Skipped invalid score for {student['name']}.")
    
    if len(scores) == 0:
            print("There are no valid scores to calculate.")
            return
    
    total_students = len(students)
    average_score = sum(scores) / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    print("\nSTUDENT STATISTICS")
    print("Total students:", total_students)
    print(f"Average score: {average_score:.2f}")
    print(f"Highest score: {highest_score:.2f}")
    print(f"Lowest score: {lowest_score:.2f}")

while True:
    print_menu()

    choice = input("choose an option(1-7): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        show_statistics()
    elif choice == "7":
        print("goodbye!")
        break
    else:
        print("that option is not ready yet.")
