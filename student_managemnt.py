class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def __str__(self):
        return f"{self.roll_no},{self.name},{self.course}"  # CSV format


class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def add_student(self, name, roll_no, course):
        with open(self.filename, "a") as file:
            file.write(f"{roll_no},{name},{course}\n")
        print(f"\n Student '{name}' added successfully!")

    def display_students(self):
        try:
            with open(self.filename, "r") as file:
                students = file.readlines()
                if not students:
                    print("\n No students found!")
                    return
                print("\n Student List:")
                for student in students:
                    roll_no, name, course = student.strip().split(",")
                    print(f"{roll_no} | {name} | {course}")
        except FileNotFoundError:
            print("\n No student records found!")

    def search_student(self, roll_no):
        try:
            with open(self.filename, "r") as file:
                for student in file:
                    student_data = student.strip().split(",")
                    if student_data[0] == roll_no:
                        print(f"\n Student Found: {student_data[0]} | {student_data[1]} | {student_data[2]}")
                        return
            print("\n Student not found!")
        except FileNotFoundError:
            print("\n No student records found!")

    def update_student(self, roll_no, new_name=None, new_course=None):
        try:
            updated_students = []
            found = False

            with open(self.filename, "r") as file:
                students = file.readlines()

            for student in students:
                student_data = student.strip().split(",")
                if student_data[0] == roll_no:
                    if new_name:
                        student_data[1] = new_name
                    if new_course:
                        student_data[2] = new_course
                    found = True
                updated_students.append(",".join(student_data))

            if not found:
                print("\n Student not found!")
                return

            with open(self.filename, "w") as file:
                file.write("\n".join(updated_students) + "\n")

            print("\n Student details updated!")

        except FileNotFoundError:
            print("\n No student records found!")

    def delete_student(self, roll_no):
        try:
            students = []
            found = False

            with open(self.filename, "r") as file:
                for student in file:
                    if student.startswith(roll_no + ","):
                        found = True
                        continue  # Skip the student to delete
                    students.append(student.strip())

            if not found:
                print("\n Student not found!")
                return

            with open(self.filename, "w") as file:
                file.write("\n".join(students) + "\n")

            print("\n Student deleted successfully!")

        except FileNotFoundError:
            print("\n No student records found!")


def main():
    manager = StudentManager()

    while True:
        print("\n STUDENT MANAGEMENT SYSTEM")
        print("1️ Add Student")
        print("2️ Display Students")
        print("3️ Search Student")
        print("4 Update Student")
        print("5 Delete Student")
        print("6️ Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            roll_no = input("Enter Roll No: ")
            course = input("Enter Course: ")
            manager.add_student(name, roll_no, course)

        elif choice == "2":
            manager.display_students()

        elif choice == "3":
            roll_no = input("Enter Roll No: ")
            manager.search_student(roll_no)

        elif choice == "4":
            roll_no = input("Enter Roll No: ")
            name = input("Enter New Name (Leave blank if no change): ")
            course = input("Enter New Course (Leave blank if no change): ")
            manager.update_student(roll_no, name if name else None, course if course else None)

        elif choice == "5":
            roll_no = input("Enter Roll No to Delete: ")
            manager.delete_student(roll_no)

        elif choice == "6":
            print("\n Exiting... Have a great day!")
            break

        else:
            print("\n Invalid choice! Try again.")


if __name__ == "__main__":
    main()
