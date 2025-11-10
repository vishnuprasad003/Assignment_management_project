from django import forms
from django.contrib.auth.forms import UserCreationForm

from Assignment_management_project_app.models import Department, Login, Teacher, Student, Assignment, Submission


class LoginRegistration(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="conformPassword", widget=forms.PasswordInput)

    class Meta:
        model =Login
        fields =('username','password1','password2')


class Department_form(forms.ModelForm):
    class Meta:
        model=Department
        fields="__all__"


class teacher_form(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('Teacher_image','Teacher_name','Teacher_Phone_number','Teacher_Email')

class student_form(forms.ModelForm):
    class Meta:
        model=Student
        fields=('Student_image','Student_name','Student_Email','Student_Phone_number','Student_department')

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class assignment_form(forms.ModelForm):
    assignment_due_date=forms.DateTimeField(widget=DateTimeInput)
    class Meta:
        model=Assignment
        fields=('assignment_title','assignment_description','assignment_file','assignment_due_date','department')


class submission_form(forms.ModelForm):
    class Meta:
        model=Submission
        fields=('submit_file','text')