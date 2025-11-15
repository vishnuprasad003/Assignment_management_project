from django.contrib.auth.decorators import login_required
from django.utils import timezone


from django.shortcuts import render, redirect
from django.contrib import messages

from Assignment_management_project_app.filters import teacherFilter, assignmentFilter, submittedFilter
from Assignment_management_project_app.foms import student_form, submission_form
from Assignment_management_project_app.models import Teacher, Student, Assignment, Submission

@login_required(login_url="Loginview")
def view_teacher(request):
    data=Teacher.objects.all()
    teacher_filter=teacherFilter(request.GET,queryset=data)
    data1=teacher_filter.qs
    context={
        "data":data1,
        "teacher_filter":teacher_filter
    }
    return render(request,"student/view_teacher.html",context)

@login_required(login_url="Loginview")
def view_assignments(request, id):
    student = Student.objects.get(user=request.user)
    teacher = Teacher.objects.get(id=id)
    assignments = Assignment.objects.filter(department=student.Student_department, teacher=teacher)

    today = timezone.now().date()



    return render(request, "student/view_assignment.html", {"assignments": assignments,"teacher": teacher,"today":today})

@login_required(login_url="Loginview")
def profile(request):
    user_data=request.user
    student=Student.objects.get(user=user_data)
    return render(request,"student/profile_student.html",{"data":student})
@login_required(login_url="Loginview")
def profile_edit(request,id):
    student=Student.objects.get(id=id)
    form=student_form(instance=student)
    if request.method =="POST":
        form1=student_form(request.POST,request.FILES,instance=student)
        if form1.is_valid():
            form1.save()
            return redirect("profile")
    return render(request,"student/pofile_student_edit.html",{"data":form})

@login_required(login_url="Loginview")
def submit_assignment(request,id):
    user_data=request.user
    student=Student.objects.get(user=user_data)
    assignment=Assignment.objects.get(id=id)
    form = submission_form()
    if timezone.now().date() > assignment.assignment_due_date:
        messages.info(request ,"Due date is passed ")

    student_submission= Submission.objects.filter(student=student)
    submitted_assignment=[]
    for submission in student_submission:
        submitted_assignment.append(submission.assignment.id)
    if assignment.id in submitted_assignment:
        messages.info(request,"You already submitted ")
        return redirect("viewsubmittedassignment")
    if request.method == "POST":
        form1=submission_form(request.POST,request.FILES)
        if form1.is_valid():
            submit=form1.save(commit=False)
            submit.student=student
            submit.assignment=assignment
            submit.save()
            return redirect("viewsubmittedassignment")
    return render(request,"student/submit_assignment.html",{"form":form})
@login_required(login_url="Loginview")
def view_submitted_assignment(request):
    user_data=request.user
    data=Student.objects.get(user=user_data)
    filtersubmitdata=Submission.objects.filter(student=data)
    assignment_filter=submittedFilter(request.GET,queryset=filtersubmitdata)
    data1=assignment_filter.qs
    context={
        "data":data1,
        "assignment_filter":assignment_filter
    }
    return render(request,"student/view_submitted_assignment.html",context)

@login_required(login_url="Loginview")
def update_submit_assignment(request,id):
    submit=Submission.objects.get(id=id)
    form=submission_form(instance=submit)
    if request.method =="POST":
        form1=submission_form(request.POST,request.FILES,instance=submit)
        if form1.is_valid():
            form1.save()
            return redirect("viewsubmittedassignment")
    return render(request,"student/update_submit_assignment.html",{"update":form})

@login_required(login_url="Loginview")
# def view_pending_assignment(request):
#         student = Student.objects.get(user=request.user)
#
#         department_assignments = Assignment.objects.filter(department=student.Student_department)
#         student_submissions = Submission.objects.filter(student=student)
#         submitted_assignments = []
#         for submission in student_submissions:
#             submitted_assignments.append(submission.assignment.id)
#         today = timezone.now().date()
#         pending = []
#
#         for assignment in department_assignments:
#             if assignment.id not in submitted_assignments and assignment.assignment_due_date > today:
#                 pending.append(assignment)
#
#         assignment_filter=assignmentFilter(request.GET,queryset=pending)
#         pending_search=assignment_filter.qs
#         context={
#             "pending_assignments":pending_search,
#             "assignment_filter":assignment_filter
#
#         }
#         print("assignment_filter",assignment_filter)
#         print("pending_search",pending_search)
#         return render(request, "student/pending_assignments.html", context)


def view_pending_assignment(request):
    student = Student.objects.get(user=request.user)

    # Assignments in same department
    department_assignments = Assignment.objects.filter(
        department=student.Student_department
    )

    # Submitted assignment IDs
    submitted_ids = Submission.objects.filter(
        student=student
    ).values_list("assignment_id", flat=True)

    today = timezone.now().date()

    # Pending queryset
    pending = department_assignments.exclude(
        id__in=submitted_ids
    ).filter(
        assignment_due_date__gt=today
    )

    # 🔍 Apply filter
    assignment_filter = assignmentFilter(request.GET, queryset=pending)
    pending_filtered = assignment_filter.qs

    return render(request, "student/pending_assignments.html", {
        "pending_assignments": pending_filtered,
        "assignment_filter": assignment_filter
    })
