from django.urls import path
from  .import views

urlpatterns = [
#==========signup users ================================================
    path('HODsignup/',views.admin_registration),   
    path('studentsignup/',views.student_registration),   
    path('staffsignup/',views.staff_registration),  

#====================admin login=========================================
    # path('admin_login/',views.admin_login), 
    # path('Studentprofile/',views.admin_login), 
    # path('login/',views.login_view), 

    path('Studentprofile/',views.Studentprofile), 
    # path('createStudent/',views.createStudent), 
    
]
