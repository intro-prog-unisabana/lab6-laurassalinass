def student_averages(my_dict):
    result = {}
    for student_id, assignments in my_dict.items():
        grades = list(assignments.values())
        result[student_id] = round(sum(grades) / len(grades))
    return result
 
 
def assignment_averages(my_dict):
    assignment_totals = {}
    assignment_counts = {}
 
    for assignments in my_dict.values():
        for assignment, grade in assignments.items():
            assignment_totals[assignment] = assignment_totals.get(assignment, 0) + grade
            assignment_counts[assignment] = assignment_counts.get(assignment, 0) + 1
 
    result = {}
    for assignment in assignment_totals:
        result[assignment] = round(assignment_totals[assignment] / assignment_counts[assignment])
 
    return result