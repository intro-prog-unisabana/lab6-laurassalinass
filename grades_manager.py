def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}
 
 
def add_student(student_grades={}):
    name = input("Enter student name: ").strip().title()
 
    subjects = {}
    while True:
        entry = input("Enter subject and grade (or 'exit' to finish): ").strip()
        if entry.lower() == "exit":
            break
        subject, grade = entry.split(",")
        subjects[subject.strip().title()] = float(grade.strip())
 
    student_grades[name] = subjects
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades
 
 
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