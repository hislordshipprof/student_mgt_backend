from django.urls import path
from student_mgt_app.api import StudentView,HodViews

urlpatterns = [
#==========signup users ================================================
    # path('studentview/',StudentView.student_home),   
    path('admin_home/',HodViews.admin_home),   
    path('add_staff_save/',HodViews.add_staff_save),  

    path('add_course_save/',HodViews.add_course_save), 

    path('add_student_save/',HodViews.add_student_save),   
    path('add_subject',HodViews.add_subject),   
    path('add_subject_save/',HodViews.add_subject_save),   
   
]
