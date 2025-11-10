from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Assignment_management_project_app.foms import teacher_form, assignment_form
from Assignment_management_project_app.models import Teacher, Department, Student, Assignment, Submission

@login_required(login_url="Loginview")
def profile(request):
    user_data=request.user
    teacher=Teacher.objects.get(user=user_data)
    return render(request,"teacher/profile_teacher.html",{"data":teacher})
@login_required(login_url="Loginview")
def profile_edit(request,id):
    teacher=Teacher.objects.get(id=id)
    form=teacher_form(instance=teacher)
    if request.method =="POST":
        form1=teacher_form(request.POST,request.FILES,instance=teacher)
        if form1.is_valid():
            form1.save()
            return redirect("profileteacher")
    return render(request,"teacher/profile_teacher_edit.html",{"data":form})
@login_required(login_url="Loginview")
def department_student(request):
    data=Department.objects.all()
    return render(request,"teacher/view_student.html",{"data":data})
@login_required(login_url="Loginview")
def filter_student(request,id):
    data=Student.objects.filter(Student_department=id)
    return render(request,"teacher/view_filter_student.html",{"data":data})
@login_required(login_url="Loginview")
def add_assignment(request):
    teacher=Teacher.objects.get(user=request.user)
    print("teacher",)
    form1=assignment_form()
    if request.method =="POST":
        form=assignment_form(request.POST,request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.teacher = teacher
            assignment.save()
            return redirect("viewassignment")
    return render(request,"teacher/Add_assignment_department.html",{"data":form1})

@login_required(login_url="Loginview")
def view_assignment(request):
    user_data=request.user
    data=Teacher.objects.get(user=user_data)
    filterData=Assignment.objects.filter(teacher=data)
    # data=Assignment.objects.all()
    return render(request,"teacher/view_assignment.html",{"data":filterData})
@login_required(login_url="Loginview")
def update_assignment(request,id):
    data=Assignment.objects.get(id=id)
    form=assignment_form(instance=data)
    if request.method=="POST":
        form1=assignment_form(request.POST,instance=data)
        if form1.is_valid():
            form1.save()

            return redirect("viewassignment")
    return render(request,"teacher/update_assignment.html",{"data":form})
@login_required(login_url="Loginview")
def delete_assignment(request,id):
    data=Assignment.objects.get(id=id)
    data.delete()
    return redirect("viewassignment")
@login_required(login_url="Loginview")
def view_submitted_assignment(request,id):
    teacher=Teacher.objects.get(user=request.user)
    department=Department.objects.get(id=id)
    assignments=Assignment.objects.filter(teacher=teacher,department=department)
    submission=[]
    for assignment in assignments:
        data=Submission.objects.filter(assignment=assignment)
        submission.extend(data)
    return render(request,"teacher/view_submitted_assignment.html",{"submission":submission,"department":department})




