from grades_manager import add_student, avg_by_student
 
 
def main():
    print("Welcome to the Student Grades Manager!")
    my_grades = {}
 
    while True:
        print("\nSelect an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit")
 
        option = input().strip()
 
        if option == "1":
            my_grades = add_student(my_grades)
 
        elif option == "2":
            print("\nSelect an option:")
            print("a. Display all students")
            print("b. Display selected students")
 
            sub_option = input().strip().lower()
 
            if sub_option == "a":
                avg_by_student(my_grades)
            elif sub_option == "b":
                names_input = input("Enter student names (comma-separated): ").strip()
                names = [n.strip() for n in names_input.split(",")]
                avg_by_student(my_grades, names)
            else:
                print("Invalid option selected!")
 
        elif option == "3":
            print("Goodbye!")
            break
 
        else:
            print("Invalid option selected!")
 
 
if _name_ == "_main_":
    main()