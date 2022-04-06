from django.urls import path
from student_mgt_app.api import StudentView

urlpatterns = [
#==========signup users ================================================
    path('studentview/',StudentView.student_home),   
   
]
