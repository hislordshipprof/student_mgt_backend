import profile
from re import T
from django.conf import settings
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict

from Accounts.models import User
from rest_framework.authtoken.models import Token
from utils.utils import serialize
# Create your models here.
class SessionYearModel(models.Model):
    id=models.AutoField(primary_key=True)
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    object=models.Manager()


class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return self.user.username

class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,blank=True, null=True)
    last_name = models.CharField(max_length=50,blank=True, null=True)
    address=models.TextField(null=True,blank=True,)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    objects=models.Manager()

    def __str__(self):
        return self.user.username
    def to_json(self):
        data={'id':self.id,**model_to_dict(self), 
        "subject_id":serialize(Subjects.objects.filter(staff_id=self.user.id)),
        "staff_atte_present_list":Attendance.objects.filter(subject_id=self.id).count(),
        "staff_absent_list":LeaveReportStaff.objects.filter(staff_id=self.id).count(),
        # "staff_name_list":User.objects.filter(user=self.id)
        }
         
        return data
   

class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    # objects=models.Manager()
    def __str__(self):
        return self.course_name


    def to_json(self):
        return {"id":self.id, **model_to_dict(self),
        "subjects_in_course_count":Subjects.objects.filter(course_id=self.id).count(),
        "students_with_course_count":Students.objects.filter(course_id=self.id).count(),
        
        }
        


class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255,null=True,blank=True)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE,default=1,blank=True, null=True)
    staff_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return self.subject_name

    def to_json(self):
        data={'id':self.id,**model_to_dict(self), 
        # "courses":serialize(Courses.objects.filter(id=self.course_id.id)),
        }
        
        return data

class Students(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,blank=True, null=True)
    last_name = models.CharField(max_length=50,blank=True, null=True)
    gender=models.CharField(max_length=255,null=True,blank=True,)
    profile_pic=models.FileField(null=True,blank=True,default='/placeholder.png')
    address=models.TextField(null=True,blank=True,)
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING,null=True,blank=True,)
    session_year_id=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE,null=True,blank=True,)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    objects = models.Manager()

    def __str__(self):
        return self.user.username

    def to_json(self):
        data= {"id":self.id, **model_to_dict(self,exclude=['profile_pic']),
        
        "course_of_student":serialize(Courses.objects.filter(id=self.course_id.id)),
        
      "attendance_present_list":AttendanceReport.objects.filter(student_id=self.id,status=True).count(),
      "absent_list":AttendanceReport.objects.filter(student_id=self.id,status=False).count(),
      "leaves":LeaveReportStudent.objects.filter(student_id=self.id,).count(),
     
        }
        data['profile_pic'] = self.profile_pic.url if self.profile_pic else ""
        return data
    

class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    session_year_id=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
    def to_json(self):
        data={'id':self.id,**model_to_dict(self), 
      
        }
        
        return data

class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def to_json(self):
        data={'id':self.id,**model_to_dict(self), 
      
        }
        
        return data

class LeaveReportStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_message=models.TextField()
    leave_status=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def to_json(self):
        data={'id':self.id,**model_to_dict(self), 
    
        }
        
        return data

class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class StudentResult(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    subject_exam_marks=models.FloatField(default=0)
    subject_assignment_marks=models.FloatField(default=0)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()

class OnlineClassRoom(models.Model):
    id=models.AutoField(primary_key=True)
    room_name=models.CharField(max_length=255)
    room_pwd=models.CharField(max_length=255)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    session_years=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    started_by=models.ForeignKey(Staffs,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return self.room_name

# @receiver(post_save,sender=CustomUser)
# def create_user_profile(sender,instance,created,**kwargs):
#     if created:
#         if instance.user_type==1:
#             AdminHOD.objects.create(admin=instance)
#         if instance.user_type==2:
#             Staffs.objects.create(admin=instance,address="")
#         if instance.user_type==3:
#             Students.objects.create(admin=instance,course_id=Courses.objects.get(id=1),session_year_id=SessionYearModel.object.get(id=1),address="",profile_pic="",gender="")

# @receiver(post_save,sender=CustomUser)
# def save_user_profile(sender,instance,**kwargs):
#     if instance.user_type==1:
#         instance.adminhod.save()
#     if instance.user_type==2:
#         instance.staffs.save()
#     if instance.user_type==3:
#         instance.students.save()

