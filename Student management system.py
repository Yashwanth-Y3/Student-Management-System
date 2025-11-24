

def deco_line(char='*', length=60):
    return char * length

def header(title):
    print(deco_line('*'))
    print(title.center(60))
    print(deco_line('*'))

def sub_deco():
    print(" ".join(["~"] * 30))

def pause(msg="Press Enter to return to main menu..."):
    input(msg)

def print_table(students):
    if not students:
        print("(No students to display)")
        return
    rows = []
    for roll, info in students.items():
        rows.append((str(roll), info["name"], info["class"], str(info["marks"])))
    # minimal column widths
    col_w = [6, 15, 6, 5]
    for r in rows:
        col_w[0] = max(col_w[0], len(r[0]))
        col_w[1] = max(col_w[1], len(r[1]))
        col_w[2] = max(col_w[2], len(r[2]))
        col_w[3] = max(col_w[3], len(r[3]))
    sep = "+{}+{}+{}+{}+".format('-'*(col_w[0]+2), '-'*(col_w[1]+2), '-'*(col_w[2]+2), '-'*(col_w[3]+2))
    header_row = "| {r:<{w0}} | {n:<{w1}} | {c:<{w2}} | {m:<{w3}} |".format(
        r="RollNo", n="Name", c="Class", m="Marks", w0=col_w[0], w1=col_w[1], w2=col_w[2], w3=col_w[3]
    )
    print(sep)
    print(header_row)
    print(sep)
    for r in rows:
        print("| {r:<{w0}} | {n:<{w1}} | {c:<{w2}} | {m:<{w3}} |".format(
            r=r[0], n=r[1], c=r[2], m=r[3], w0=col_w[0], w1=col_w[1], w2=col_w[2], w3=col_w[3]
        ))
    print(sep)

def add_student(students):
    print()
    print("--- Add New Student ---")
    while True:
        name = input("Enter Name         : ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
        roll = input("Enter Roll Number  : ").strip()
        if not roll:
            print("Roll number cannot be empty. Please try again.")
            continue
        if roll in students:
            print(f"Roll number {roll} already exists. Use update option instead.")
            cont = input("Do you want to try another roll number? (y/n): ").strip().lower()
            if cont != 'y':
                return
            else:
                continue
        sclass = input("Enter Class        : ").strip() or "N/A"
        while True:
            marks_input = input("Enter Marks (0-100): ").strip()
            try:
                marks = int(marks_input)
                if not (0 <= marks <= 100):
                    raise ValueError
                break
            except Exception:
                print("Please enter valid marks between 0 and 100.")
        students[roll] = {"name": name, "class": sclass, "marks": marks}
        print()
        print("Student added successfully!")
        again = input("Do you want to add another student? (y/n): ").strip().lower()
        if again != 'y':
            break

def display_all(students):
    print()
    print("--- All Students ---")
    print_table(students)
    print()
    print(f"Total students: {len(students)}")
    pause()

def search_student(students):
    print()
    print("--- Search Student ---")
    roll = input("Enter Roll Number to search: ").strip()
    print()
    info = students.get(roll)
    if info:
        print("Student found:")
        print(f"Roll No : {roll}")
        print(f"Name    : {info['name']}")
        print(f"Class   : {info['class']}")
        print(f"Marks   : {info['marks']}")
    else:
        print(f"No student found with roll number {roll}.")
    pause()

def update_student(students):
    print()
    print("--- Update Student ---")
    roll = input("Enter Roll Number to update: ").strip()
    info = students.get(roll)
    if not info:
        print(f"No student found with roll number {roll}.")
        pause()
        return
    print()
    print("Current details:")
    print(f"Name  : {info['name']}")
    print(f"Class : {info['class']}")
    print(f"Marks : {info['marks']}")
    print()
    new_name = input("Update Name (leave blank to keep): ").strip()
    new_class = input("Update Class (leave blank to keep): ").strip()
    new_marks_input = input("Update Marks (leave blank to keep): ").strip()
    if new_name:
        info['name'] = new_name
    if new_class:
        info['class'] = new_class
    if new_marks_input:
        try:
            new_marks = int(new_marks_input)
            if 0 <= new_marks <= 100:
                info['marks'] = new_marks
            else:
                print("Invalid marks entered. Keeping previous marks.")
        except Exception:
            print("Invalid marks entered. Keeping previous marks.")
    students[roll] = info
    print()
    print("Student updated successfully!")
    print("Updated details:")
    print(f"Roll No : {roll}")
    print(f"Name    : {info['name']}")
    print(f"Class   : {info['class']}")
    print(f"Marks   : {info['marks']}")
    pause()

def delete_student(students):
    print()
    print("--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ").strip()
    info = students.get(roll)
    if not info:
        print(f"No student found with roll number {roll}.")
        pause()
        return
    confirm = input(f"Are you sure you want to delete student {roll} ({info['name']})? (y/n): ").strip().lower()
    if confirm == 'y':
        del students[roll]
        print()
        print(f"Student {roll} deleted successfully.")
    else:
        print("Delete cancelled.")
    pause()

def main():
    students = {}  # in-memory storage only
    name = "STUDENT MANAGEMENT SYSTEM"
    keep_running = True

    while keep_running:
        header(name)
        sub_deco()
        print()
        print("Hello! I'm Registrar — How can I help you today?\n")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Roll No.")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit (data will NOT be saved)\n")
        sub_deco()
        print()
        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            print()
            print("Exiting. Goodbye... ")
            keep_running = False
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        if keep_running:
            print()
            print("-" * 60)
            print()

if __name__ == "__main__":
    main()

