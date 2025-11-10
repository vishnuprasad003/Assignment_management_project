from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)

class Department(models.Model):

    Department_name=models.CharField(max_length=20)
    Department_Email=models.EmailField(unique=True)
    Department_Phone_Number=models.CharField(max_length=10)

    def __str__(self):
        return self.Department_name

class Teacher(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name="teacher")
    Teacher_name=models.CharField(max_length=25)
    Teacher_Email=models.EmailField(unique=True)
    Teacher_Phone_number=models.CharField(max_length=10)
    Teacher_image=models.FileField(upload_to='teacher_image/')

    def __str__(self):
        return self.Teacher_name

class Student(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name="student")
    Student_name=models.CharField(max_length=25)
    Student_Email=models.EmailField(unique=True)
    Student_Phone_number=models.CharField(max_length=10)
    Student_department=models.ForeignKey("Department",on_delete=models.DO_NOTHING)
    Student_image=models.FileField(upload_to='student_image/')

    def __str__(self):
        return self.Student_name

class Assignment(models.Model):
    assignment_title = models.CharField(max_length=100)
    assignment_description = models.TextField()
    assignment_file = models.FileField(upload_to='assignment_files/')
    assignment_due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey("Teacher", on_delete=models.DO_NOTHING)
    department = models.ForeignKey("Department", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.assignment_title

class Submission(models.Model):
    student=models.ForeignKey("Student",on_delete=models.DO_NOTHING)
    assignment=models.ForeignKey("Assignment",on_delete=models.DO_NOTHING)
    submit_file=models.FileField(upload_to='submit_file/')
    submit_date=models.DateTimeField(auto_now_add=True)
    text = models.TextField()
