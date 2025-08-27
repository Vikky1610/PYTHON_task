# dictionay_tutorial.py
# Program to manage student grades using a dictionary

students = {"vikky": "A", "kavya": "B"}  # initial data

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Show All Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"Added {name} with grade {grade}")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"Updated {name}'s grade to {grade}")
        else:
            print(" Student not found.")

    elif choice == "3":
        print("\n Student Grades:")
        for name, grade in students.items():
            print(f"{name} : {grade}")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
