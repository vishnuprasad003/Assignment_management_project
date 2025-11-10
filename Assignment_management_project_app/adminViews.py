from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Assignment_management_project_app.foms import Department_form, teacher_form, student_form
from Assignment_management_project_app.models import Department, Teacher, Student

@login_required(login_url="Loginview")
def department(request):
    form=Department_form()
    if request.method=='POST':
        form2=Department_form(request.POST)
        if form2.is_valid():
            form2.save()
    return render(request,"admin/Department.html",{"data":form})
@login_required(login_url="Loginview")
def departmentview(request):
    data=Department.objects.all()

    return render(request,"admin/department_view.html",{"data":data})
@login_required(login_url="Loginview")
def department_update(request,id):
    data=Department.objects.get(id=id)
    form=Department_form(instance=data)
    if request.method=='POST':
        form1=Department_form(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect("departmentview")

    return render(request,"admin/department_update.html",{"update":form})
@login_required(login_url="Loginview")
def department_delete(request,id):
    data=Department.objects.get(id=id)
    data.delete()
    return redirect("departmentview")
@login_required(login_url="Loginview")
def teacher_view(request):
    data=Teacher.objects.all()
    return render(request,"admin/teacher_view.html",{"data":data})
@login_required(login_url="Loginview")
def teacher_update(request,id):
    data=Teacher.objects.get(id=id)
    form=teacher_form(instance=data)
    if request.method =='POST':
        form1=teacher_form(request.POST,request.FILES,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect("teacherview")
    return render(request,"admin/teacher_update.html",{"update":form})
@login_required(login_url="Loginview")
def teacher_delete(request,id):
    data=Teacher.objects.get(id=id)
    data.delete()
    return redirect("teacherview")

@login_required(login_url="Loginview")
def student_view(request):
    data=Student.objects.all()
    return render(request,"admin/student_view.html",{"data":data})
@login_required(login_url="Loginview")
def student_update(request,id):
    data=Student.objects.get(id=id)
    form=student_form(instance=data)
    if request.method=='POST':
        form1=student_form(request.POST,request.FILES,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect("studentview")
    return render(request,"admin/student_update.html",{"update":form})
@login_required(login_url="Loginview")
def student_delete(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect("studentview")
