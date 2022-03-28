from django.urls import path
from  .import views

urlpatterns = [
#==========signup users ================================================
    path('HODsignup/',views.admin_registration),   
    path('studentsignup/',views.student_registration),   
    path('staffsignup/',views.staff_registration),  

#====================admin login=========================================
    path('admin_login/',views.admin_login), 
    path('profile/',views.profile), 
    path('profiles/',views.profiles), 
]
