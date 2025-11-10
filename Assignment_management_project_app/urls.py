"""
URL configuration for Assignment_management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from Assignment_management_project_app import views, adminViews, studentViews, teacherViews

urlpatterns = [
    path('',views.index,name="index"),
    path('index1',views.index1,name="index1"),
    path('adminIndex',views.admin_Basepage,name="adminIndex"),
    path('studentIndex',views.Student_Basepage,name="studentIndex"),
    path('teacherIndex',views.Teacher_Basepage,name="teacherIndex"),
    # path('LoginPage',views.Loginpage,name="LoginPage"),
    path('teacherAdd',views.teacher_add,name="teacherAdd"),
    path('studentAdd',views.student_add,name="studentAdd"),
    path('Loginview',views.login_view,name="Loginview"),
    path('logout_user',views.logout_user,name="logout_user"),


    path('Department',adminViews.department,name="Department"),
    path('departmentview',adminViews.departmentview,name="departmentview"),
    path('departmentupdate/<int:id>/',adminViews.department_update,name="departmentupdate"),
    path('departmentdelete/<int:id>/',adminViews.department_delete,name="departmentdelete"),

    path('teacherview',adminViews.teacher_view,name="teacherview"),
    path('teacherupdate/<int:id>/',adminViews.teacher_update,name="teacherupdate"),
    path('teacherdelete/<int:id>/',adminViews.teacher_delete,name="teacherdelete"),

    path('studentview',adminViews.student_view,name="studentview"),
    path('studentupdate/<int:id>/',adminViews.student_update,name="studentupdate"),
    path('studentdelete/<int:id>/',adminViews.student_delete,name="studentdelete"),



    path('viewteacher',studentViews.view_teacher,name="viewteacher"),
    path('viewassignment/<int:id>/',studentViews.view_assignments,name="viewassignment"),
    path('profile',studentViews.profile,name="profile"),
    path('profileedit/<int:id>/',studentViews.profile_edit,name="profileedit"),
    path('submitassignment/<int:id>/',studentViews.submit_assignment,name="submitassignment"),
    path('viewsubmittedassignment',studentViews.view_submitted_assignment,name="viewsubmittedassignment"),
    path('updatesubmitassignment/<int:id>/',studentViews.update_submit_assignment,name="updatesubmitassignment"),
    path('pendingassignment',studentViews.view_pending_assignment,name="pendingassignment"),


    path('profileteacher',teacherViews.profile,name="profileteacher"),
    path('profileteacheredit/<int:id>/',teacherViews.profile_edit,name="profileteacheredit"),
    path('viewstudent',teacherViews.department_student,name="viewstudent"),
    path('filterstudent/<int:id>/',teacherViews.filter_student,name="filterstudent"),
    path('submittedassignment/<int:id>/',teacherViews.view_submitted_assignment,name="submittedassignment"),
    path('addassignment',teacherViews.add_assignment,name="addassignment"),
    path('viewassignment',teacherViews.view_assignment,name="viewassignment"),
    path('updateassignment/<int:id>/',teacherViews.update_assignment,name="updateassignment"),
    path('deleteassignment/<int:id>/',teacherViews.delete_assignment,name="deleteassignment")
]
