from school.models import Student

student = Student.objects.first()
print(student.teachers.all())