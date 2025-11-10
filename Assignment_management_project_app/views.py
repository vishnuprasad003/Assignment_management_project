from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.shortcuts import render, redirect

from Assignment_management_project_app.foms import LoginRegistration, teacher_form, student_form
from Assignment_management_project_app.models import Teacher


# Create your views here.
def index (request):
    return render(request,"index.html")
@login_required(login_url="Loginview")
def index1(request):
    return render(request,'index1.html')
@login_required(login_url="Loginview")
def admin_Basepage (request):
    return render(request,"admin/admin_Basepage.html")
@login_required(login_url="Loginview")
def Student_Basepage(request):
    return render(request,"student/Student_Basepage.html")
@login_required(login_url="Loginview")
def Teacher_Basepage(request):
    return render(request,"teacher/Teacher_Basepage.html")
# def Loginpage(request):
#     return render(request,"login.html")


def teacher_add(request):
    form1=LoginRegistration()
    form2=teacher_form()
    if request.method =="POST":
        form3=LoginRegistration(request.POST)
        form4=teacher_form(request.POST,request.FILES)
        if form3.is_valid() and form4.is_valid():
            data=form3.save(commit=False)
            data.is_teacher=True
            data.save()

            data1=form4.save(commit=False)
            data1.user=data
            data1.save()
            return redirect("Loginview")
    return render(request,"login1.html",{"form1":form1,"form2":form2})


def student_add(request):
    form1=LoginRegistration()
    form2=student_form()
    if request.method =='POST':
        form3=LoginRegistration(request.POST)
        form4=student_form(request.POST,request.FILES)
        if form3.is_valid() and form4.is_valid():
            data=form3.save(commit=False)
            data.is_student=True
            data.save()

            data1= form4.save(commit=False)
            data1.user=data
            data1.save()
            return redirect("Loginview")
    return render(request,"login2.html",{"form1":form1,"form2":form2})



def login_view(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        print("username",username)
        password=request.POST.get('pass')
        print("password",password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                print("hi")
                return redirect("adminIndex")
            elif user.is_student:
                print("hello")
                return redirect("studentIndex")
            elif user.is_teacher:

                return redirect("teacherIndex")

    return render(request,"login.html")


def logout_user(request):
    logout(request)
    return redirect("index")