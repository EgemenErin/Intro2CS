# My Personal Details
name = "Egemen"
age = 23.5
height = 1.80
student_now = True
city = "Poznan"

print(name, "is", age, "years old")
print(type(name), type(age))
print(type(height), type(student_now))

#pizza
slices_per_student = 4
students = 19
enrolled_students = students + 3
present_students = enrolled_students - 2
total_slices_needed = present_students * slices_per_student
cost_per_student = 500 / present_students
boxes_to_order = total_slices_needed // 8
leftover_slices = (boxes_to_order*8) % present_students

print("There are" , present_students, "students present today" " and we need", total_slices_needed, "slices of pizza to feed everyone.")
print('boxes to order:', boxes_to_order, 'cost per student:', cost_per_student, "zloty.")
print('leftover slices:', leftover_slices)