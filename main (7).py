class Student:

 def __init__(self, name, roll_number, cgpa):
   self.name = name
   self.roll_number = roll_number
   self.cgpa = cgpa
    
def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda x:x.cgpa,reverse=True)
    return sorted_students


students = [
  student("John","A101",3.8),
  student("smith","B102",3.6),
  student("Alex","C103",3.9),
  student("James","D104",3.7)
]

sorted_students = sort_students(students)

#print sorted list
for student in sorted_students:
  print(f"name:{student.name},Roll Number:{student.roll_number},CGPA: {student.cgpa}")

