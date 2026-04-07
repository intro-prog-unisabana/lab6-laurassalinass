def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}


def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}

    name = input("Enter student name: ").strip().title()

    subjects = {}

    while True:
        entry = input("Enter subject and grade (or 'exit' to finish):")
        
        if entry.lower() == "exit":
            break

        subject, grade = entry.split(",")
        subject = subject.strip().title()
        grade = float(grade.strip())

        subjects[subject] = grade

    student_grades[name] = subjects

    print(f"Student {name} successfully added to the grades management system.")

    return student_grades


def get_students(student_grades, keys):
    result = {}

    # crear mapa en minúsculas para búsqueda case-insensitive
    lower_map = {k.lower(): k for k in student_grades}

    for name in keys:
        name_clean = name.strip().lower()

        if name_clean in lower_map:
            real_name = lower_map[name_clean]
            result[real_name] = student_grades[real_name]
        else:
            print(f"{name.strip().title()} not found!")

    return result


def avg_by_student(student_grades, keys=None):
    if keys is None:
        data = student_grades
    else:
        data = get_students(student_grades, keys)

    for student, subjects in data.items():
        avg = sum(subjects.values()) / len(subjects)
        print(f"{student}: {avg:.1f}")
 
 
def get_students(student_grades, keys):
    result = {}
    lower_map = {k.lower(): k for k in student_grades}
 
    for key in keys:
        canonical = lower_map.get(key.lower())
        if canonical is None:
            print(f"{key.title()} not found!")
        else:
            result[canonical] = student_grades[canonical]
 
    return result
 
 
def avg_by_student(student_grades, keys=None):
    if keys is None:
        target = student_grades
    else:
        target = get_students(student_grades, keys)
 
    for name, subjects in target.items():
        grades = list(subjects.values())
        if grades:
            avg = sum(grades) / len(grades)
        else:
            avg = 0.0
        print(f"{name}: {avg:.1f}")