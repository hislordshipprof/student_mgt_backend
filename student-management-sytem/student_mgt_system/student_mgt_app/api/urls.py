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
    path('manage_course/',HodViews.manage_course),   
    path('manage_staff/',HodViews.manage_staff),   
    path('manage_student/',HodViews.manage_student),   
    path('manage_subject/',HodViews.manage_subject),   

    # path('edit_staff/<str:staff_id>', HodViews.edit_staff,name="edit_staff"),
    # path('edit_staff_save', HodViews.edit_staff_save,name="edit_staff_save"),
    # path('edit_student/<str:student_id>', HodViews.edit_student,name="edit_student"),
    # path('edit_student_save', HodViews.edit_student_save,name="edit_student_save"),
    path('edit_subject/<str:subject_id>', HodViews.edit_subject,name="edit_subject"),
    path('edit_subject_save', HodViews.edit_subject_save,name="edit_subject_save"),
    path('edit_course/<str:course_id>', HodViews.edit_course,name="edit_course"),
    path('edit_course_save', HodViews.edit_course_save,name="edit_course_save"),
    path('manage_session', HodViews.manage_session,name="manage_session"),
   
]
