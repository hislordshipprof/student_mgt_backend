
from dataclasses import field
from rest_framework import serializers
from student_mgt_app.models import *

class SessionYearModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=SessionYearModel
        fields="__all__"

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'

class StudentsSerializer(serializers.ModelSerializer):
    course_id=CoursesSerializer(many=False,read_only=True)
 
    class Meta:
        model =Students
        fields='__all__'


class AdminHodSerializer(serializers.ModelSerializer):
     class Meta:
         model=AdminHOD
         fields='__all__'       

class StaffsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Staffs
        fields='__all__'

class SubjectsSerializer(serializers.ModelSerializer):
    course_id=CoursesSerializer()
    class Meta:
        model=Subjects
        fields='__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'    

class AttendanceReportSerializer(serializers.ModelSerializer):
    attendance_id=AttendanceSerializer(many=False,read_only=True)
    class Meta:
        model=AttendanceReport
        fields='__all__'

class LeaveReportStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=LeaveReportStudent
        fields='__all__'        

class LeaveReportStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=LeaveReportStaff
        fields='__all__'

class FeedBackStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBackStudent
        fields='__all__'


class FeedBackStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBackStaff
        fields='__all__'       


class NotificationStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotificationStudent
        fields='__all__'

class NotificationStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotificationStaff
        fields='__all__'

class OnlineClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=OnlineClassRoom
        fields='__all__'