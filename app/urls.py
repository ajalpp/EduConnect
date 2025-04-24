"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.logi_n),
    path('login/', views.a_login),
    path('admin/',views.admin_home),
    path('manage_subject',views.manage_subject),
    path('subject_deletion/<id>',views.subject_deletion),
    path('manage_course',views.manage_course),
    path('course_deletion/<id>',views.course_deletion),
    path('manage_teacher/',views.teacher_registration),
    path('teacher_deletion/<id>',views.teacher_deletion),
    path('edit_teacher/<id>',views.edit_teacher),
    path('send_notification',views.notifications),
    path('noti_update/<id>',views.noti_update),
    path('view_teachers',views.viewteachers),
    path('view_students',views.viewstudents),
    path('view_parents',views.viewparents),
    path('view_courssub',views.view_courssub),




#2 
    path('teacher',views.teacher_home),
    path('manage_student',views.manage_student),
    path('viewstudent',views.view_student),
    path('delete_student/<id>',views.delete_student),
    path('edit_student/<id>',views.edit_student),

    path('view_notification',views.view_notification),
    path('view_pass_request',views.view_passrequest),
    path('pass_accept/<id>',views.pass_accept),
    path('pass_reject/<id>',views.pass_reject),
    path('teacher_view_students_to_add_score/<set_id>',views.teacher_view_students_to_add_score),
    path('manage_parent/<id>',views.manage_parent),
    path('replycomplaint/<complaint_id>',views.replycomplaint),
    path('lecture_note',views.lecture_note),
    path('assign_ment',views.assign_ment),
    path('assignsubmiss',views.assign_submission),
    path('view_complaints',views.view_complaint),
    path('assess_ment',views.assess_ment),
    path('teacher_add_results',views.teacher_add_results),
    path('teacher_mark_attendance',views.teacher_mark_attendance),
    path('mark_present/<student_id>/<course_id>',views.mark_attendance),
    path('mark_absent/<student_id>/<course_id>',views.mark_absent),
    path('teacher_add_score/<int:student_id>/<int:set_id>/', views.teacher_add_score, name='teacher_add_score'),



#3
    path('student',views.student_home),
    path('teachers',views.view_teachers),
    path('lecture',views.view_lecture),
    path('notification',views.viewnotification),
    path('assignment',views.assignmment),
    path('assignsub/<id>',views.assign_sub),
    path('pass_request',views.passreq),
    path('passreq',views.view_passreq),
    path('complaint',views.give_complaint),
    path('student_view_attendance',views.student_view_attendance),

    path('chat_bot/', views.chat_bot, name='chat_bot'),
    path('chat_response/', views.chat_response, name='chat_response'),




    path('parent_login',views.parent_login),
    path('parent_student',views.parent_student),
    path('parent_view_notifications',views.parent_view_notifications),
    path('parent_view_student_attendance',views.parent_view_student_attendance),
    path('parent_view_student_assessment',views.parent_view_student_assessment),


]
