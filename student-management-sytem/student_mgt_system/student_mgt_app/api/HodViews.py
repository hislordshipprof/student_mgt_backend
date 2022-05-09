import json

# import requests
from django.contrib import messages
from Accounts.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from student_mgt_app.models import Students,Staffs,Courses,Subjects,Attendance,AttendanceReport
from student_mgt_app.api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Accounts.Api.serializers import user_creation_serializer

@api_view (['GET', ])
def admin_home(request):
    student_count1=Students.objects.all().count()
    staff_count=Staffs.objects.all().count()
    subject_count=Subjects.objects.all().count()
    course_count=Courses.objects.all().count()
    subjects=serialize(Subjects.objects.all())
    courses=serialize(Courses.objects.all())
    all_students=serialize(Students.objects.all()) 
    all_staff=serialize(Staffs.objects.all()) 
    all_attendance_report=serialize(AttendanceReport.objects.all())
    all_attendance=serialize(Attendance.objects.all())
    LeaveReportStudents=serialize(LeaveReportStudent.objects.all())
   
    data={}
    data['student_count1']=student_count1
    data['staff_count']=staff_count
    data['subject_count']=subject_count
    data['course_count']=course_count
 
    data['courses']=courses
    data['subjects']=subjects
    data['all_students']=all_students
    data['all_attendance_report']=all_attendance_report
    data['all_attendance']=all_attendance
    data['LeaveReportStudents']=LeaveReportStudents
   
    data['all_staff']=all_staff

    return Response(data)
 


@api_view(['POST'])
def add_staff_save(request):
    if request.method == "POST":
        serializer = user_creation_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            print('ffeddd')
            account = serializer.save()
            account.is_staff = True
            account.save()
            staff = Staffs (
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                address = request.data.get("address"),
               
        )
         
        
            staff.user = account
            staff.save()
            serializer = StaffsSerializer(staff)
            token = Token.objects.get(user=account).key
            data['token'] = token
            data["data"] = serializer.data
        else:
            data = serializer.errors
        return Response(data)



@api_view(['POST'])
def add_course_save(request):
    if request.method == 'POST':
        course=Courses.objects.create(
            course_name="name"
        )
        serializer = CoursesSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)


@api_view(['POST'])
def add_student_save(request):
    if request.method == "POST":
        serializer = user_creation_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            account.is_student = True
            account.save()
            student = Students (
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                gender=request.data.get("gender"),
                address = request.data.get("address"),
                session_year_id = request.data.get("session_year"),
                course_id =request.data.get("course"),
                profile_pic=request.data.get("profile_pic"),
               
        )
         
            student.user = account
            student.save()
            serializer = StudentsSerializer(student)
            
            token = Token.objects.get(user=account).key
            data['token'] = token
            data["data"] = serializer.data
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET'])
def add_subject(request):
    courses=CoursesSerializer( Courses.objects.all(), many=True)
    staffs=StaffsSerializer(Staffs.objects.all(),many=True)
    return Response({"courses":courses.data,"staffs":staffs.data})

@api_view(['POST'])
def add_subject_save(request):
    if request.method == 'POST':
        subject=Subjects(
            subject_name=request.data.get("subject_name"),
            course_id=request.data.get("course_id"),
        
            staff_id=request.data.get("staff_id"),
            # staff=Staffs.objects.get(id=request.data.get("staff")),

        )
        serializer = SubjectsSerializer(subject,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)