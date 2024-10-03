from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView
from django.conf.urls import url

import teacher

urlpatterns = [
path('change_password_teacher',views.change_password_teacher,name='change_password_teacher'),
url(r'^password/$', views.change_password_teacher, name='change_password_teacher'),
#csv 
path('teacher-csv-question/', views.teacher_csv_question, name='teacher-csv-question'),
path('teacher-csv-exam/', views.teacher_csv_course, name='teacher-csv-exam'),

#all other urls
path('teacherclick', views.teacherclick_view),
path('teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'),name='teacherlogin'),
path('teachersignup', views.teacher_signup_view,name='teachersignup'),
path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),
path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),


path('teacher-question', views.teacher_question_view,name='teacher-question'),
path('teacher-add-question', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
]