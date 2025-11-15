

import django_filters
from django import forms

from Assignment_management_project_app.models import Department, Student, Teacher, Assignment, Submission


class departmentFilter(django_filters.FilterSet):
    Department_name=django_filters.CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'search Department','class':'form-control'}))

    class Meta:
        model=Department
        fields=('Department_name',)

class studentFilter(django_filters.FilterSet):
    Student_name=django_filters.CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'search student','class':'form-control'}))
    class Meta:
        model=Student
        fields=('Student_name','Student_department')

class StudentFilter(django_filters.FilterSet):
    Student_name=django_filters.CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'search student','class':'form-control'}))

    class Meta:
        model=Student
        fields=("Student_name",)

class teacherFilter(django_filters.FilterSet):
    Teacher_name=django_filters.CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'search teacher','class':'form-control'}))

    class Meta:
        model=Teacher
        fields=('Teacher_name',)

class assignmentFilter(django_filters.FilterSet):
    assignment_title=django_filters.CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'search ','class':'form-control'}))

    class Meta:
        model=Assignment
        fields=("assignment_title",)

class AssignmentFilter(django_filters.FilterSet):
    teacher__Teacher_name=  django_filters.CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'search ','class':'form-control'}))

    class Meta:
        model=Assignment
        fields=("teacher__Teacher_name",)

class submittedFilter(django_filters.FilterSet):
    assignment__assignment_title=django_filters.CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'search ','class':'form-control'}))

    class Meta:
        model=Submission
        fields=("assignment__assignment_title",)

class SubmittedFilter(django_filters.FilterSet):
    student__Student_name=django_filters.CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'search ','class':'form-control'}))

    class Meta:
        model=Submission
        fields=("student__Student_name",)