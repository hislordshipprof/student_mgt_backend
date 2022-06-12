from email.policy import default
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

# implementation done
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
 

# implementation done
@api_view(['POST'])
def add_staff_save(request):
    if request.method == "POST":
        serializer = user_creation_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            
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


# implementation done
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


# implementation done
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

# implementation done
@api_view(['GET'])
def add_subject(request):
    courses=CoursesSerializer( Courses.objects.all(),  many=True)
    staffs=serialize(Staffs.objects.all())
    
    return Response({"courses":courses.data,"staffs":staffs})


@api_view(['POST'])
def add_subject_save(request):
    if request.method == 'POST':
        course_id = request.data.get("course_id")
        course = Courses.objects.filter(id=course_id).first()
        # staff_id=request.data.get('staffs')
        subject=Subjects.objects.create(
            subject_name=request.data.get("subject_name"),
            course_id=course,
            # staff_id=staff_id
            
        )
        serializer = SubjectsSerializer(subject,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)




@api_view(['GET'])
def manage_staff(request):
    staffs=StaffsSerializer(Staffs.objects.filter(),many=True)
    return Response({"staffs":staffs.data})

@api_view(['GET'])
def manage_student(request):
    students=StudentsSerializer(Students.objects.all(),many=True)
    return Response({"students":students.data})

@api_view(['GET'])
def manage_course(request):
    courses=CoursesSerializer(Courses.objects.all(),many=True)
    return Response({"courses":courses.data})


@api_view(['GET'])
def manage_subject(request):
    subjects=SubjectsSerializer(Subjects.objects.all(),many=True)
    return Response({"subjects":subjects.data})


@api_view(['GET'])    
def edit_staff(request,staff_id):
    staff=StaffsSerializer(Staffs.objects.get(user=staff_id))
    return Response({"staff":staff.data})

api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)

    data = request.data

    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['isAdmin']

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)

# api_view(['PUT'])
# def edit_staff_save(request,pk):
#     if request.method!='PUT':
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         staff_id=request.POST.get("staff_id")
#         first_name=request.POST.get("first_name")
#         last_name=request.POST.get("last_name")
#         email=request.POST.get("email")
#         username=request.POST.get("username")
#         address=request.POST.get("address")

#         try:
#             user=CustomUser.objects.get(id=staff_id)
#             user.first_name=first_name
#             user.last_name=last_name
#             user.email=email
#             user.username=username
#             user.save()

#             staff_model=Staffs.objects.get(admin=staff_id)
#             staff_model.address=address
#             staff_model.save()
#             messages.success(request,"Successfully Edited Staff")
#             return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))
#         except:
#             messages.error(request,"Failed to Edit Staff")
#             return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))



@api_view(['PUT'])
def edit_subject(request,subject_id):
    data=request.data
    subject=Subjects.objects.get(id=subject_id)
    subject.subject_name=data['subject_name']
    subject.staff_id=data['staff_id']
    subject.save()
    # serializer=CoursesSerializer(Courses.objects.all(),many=True)
    # serializer=User.objects.filter(is_staff=True)
    serializer=SubjectsSerializer(subject,many=False)
    # if serializer.is_valid():
    #         serializer.save()
    # courses=CoursesSerializer(Courses.objects.all(),many=True)
    # staffs=User.objects.filter(is_staff=True)
    # data={}
    # data['subject']=subject
    # data['courses']=courses
    # data['staffs']=staffs
  
    return Response(serializer.data)


def edit_subject_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_id=request.POST.get("subject_id")
        subject_name=request.POST.get("subject_name")
        staff_id=request.POST.get("staff")
        course_id=request.POST.get("course")

        try:
            subject=Subjects.objects.get(id=subject_id)
            subject.subject_name=subject_name
            staff=CustomUser.objects.get(id=staff_id)
            subject.staff_id=staff
            course=Courses.objects.get(id=course_id)
            subject.course_id=course
            subject.save()

            messages.success(request,"Successfully Edited Subject")
            return HttpResponseRedirect(reverse("edit_subject",kwargs={"subject_id":subject_id}))
        except:
            messages.error(request,"Failed to Edit Subject")
            return HttpResponseRedirect(reverse("edit_subject",kwargs={"subject_id":subject_id}))


def edit_course(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,"hod_template/edit_course_template.html",{"course":course,"id":course_id})

def edit_course_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_id=request.POST.get("course_id")
        course_name=request.POST.get("course")

        try:
            course=Courses.objects.get(id=course_id)
            print(Courses.course_name)
            course.course_name=course_name
            course.save()
            messages.success(request,"Successfully Edited Course")
            return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id":course_id}))
        except:
            messages.error(request,"Failed to Edit Course")
            return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id":course_id}))


def manage_session(request):
    return render(request,"hod_template/manage_session_template.html")

def add_session_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("manage_session"))
    else:
        session_start_year=request.POST.get("session_start")
        session_end_year=request.POST.get("session_end")

        try:
            sessionyear=SessionYearModel(session_start_year=session_start_year,session_end_year=session_end_year)
            sessionyear.save()
            messages.success(request, "Successfully Added Session")
            return HttpResponseRedirect(reverse("manage_session"))
        except:
            messages.error(request, "Failed to Add Session")
            return HttpResponseRedirect(reverse("manage_session"))

@csrf_exempt
def check_email_exist(request):
    email=request.POST.get("email")
    user_obj=CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    user_obj=CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def staff_feedback_message(request):
    feedbacks=FeedBackStaffs.objects.all()
    return render(request,"hod_template/staff_feedback_template.html",{"feedbacks":feedbacks})

def student_feedback_message(request):
    feedbacks=FeedBackStudent.objects.all()
    return render(request,"hod_template/student_feedback_template.html",{"feedbacks":feedbacks})

@csrf_exempt
def student_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStudent.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

@csrf_exempt
def staff_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStaffs.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def staff_leave_view(request):
    leaves=LeaveReportStaff.objects.all()
    return render(request,"hod_template/staff_leave_view.html",{"leaves":leaves})

def student_leave_view(request):
    leaves=LeaveReportStudent.objects.all()
    return render(request,"hod_template/student_leave_view.html",{"leaves":leaves})

def student_approve_leave(request,leave_id):
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("student_leave_view"))

def student_disapprove_leave(request,leave_id):
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("student_leave_view"))


def staff_approve_leave(request,leave_id):
    leave=LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("staff_leave_view"))

def staff_disapprove_leave(request,leave_id):
    leave=LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("staff_leave_view"))

def admin_view_attendance(request):
    subjects=Subjects.objects.all()
    session_year_id=SessionYearModel.object.all()
    return render(request,"hod_template/admin_view_attendance.html",{"subjects":subjects,"session_year_id":session_year_id})

@csrf_exempt
def admin_get_attendance_dates(request):
    subject=request.POST.get("subject")
    session_year_id=request.POST.get("session_year_id")
    subject_obj=Subjects.objects.get(id=subject)
    session_year_obj=SessionYearModel.object.get(id=session_year_id)
    attendance=Attendance.objects.filter(subject_id=subject_obj,session_year_id=session_year_obj)
    attendance_obj=[]
    for attendance_single in attendance:
        data={"id":attendance_single.id,"attendance_date":str(attendance_single.attendance_date),"session_year_id":attendance_single.session_year_id.id}
        attendance_obj.append(data)

    return JsonResponse(json.dumps(attendance_obj),safe=False)


@csrf_exempt
def admin_get_attendance_student(request):
    attendance_date=request.POST.get("attendance_date")
    attendance=Attendance.objects.get(id=attendance_date)

    attendance_data=AttendanceReport.objects.filter(attendance_id=attendance)
    list_data=[]

    for student in attendance_data:
        data_small={"id":student.student_id.admin.id,"name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name,"status":student.status}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

def admin_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request,"hod_template/admin_profile.html",{"user":user})

def admin_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("admin_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            # if password!=None and password!="":
            #     customuser.set_password(password)
            customuser.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("admin_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("admin_profile"))

def admin_send_notification_student(request):
    students=Students.objects.all()
    return render(request,"hod_template/student_notification.html",{"students":students})

def admin_send_notification_staff(request):
    staffs=Staffs.objects.all()
    return render(request,"hod_template/staff_notification.html",{"staffs":staffs})

@csrf_exempt
def send_student_notification(request):
    id=request.POST.get("id")
    message=request.POST.get("message")
    student=Students.objects.get(admin=id)
    token=student.fcm_token
    url="https://fcm.googleapis.com/fcm/send"
    body={
        "notification":{
            "title":"Student Management System",
            "body":message,
            "click_action": "https://studentmanagementsystem22.herokuapp.com/student_all_notification",
            "icon": "http://studentmanagementsystem22.herokuapp.com/static/dist/img/user2-160x160.jpg"
        },
        "to":token
    }
    headers={"Content-Type":"application/json","Authorization":"key=SERVER_KEY_HERE"}
    data=requests.post(url,data=json.dumps(body),headers=headers)
    notification=NotificationStudent(student_id=student,message=message)
    notification.save()
    print(data.text)
    return HttpResponse("True")

@csrf_exempt
def send_staff_notification(request):
    id=request.POST.get("id")
    message=request.POST.get("message")
    staff=Staffs.objects.get(admin=id)
    token=staff.fcm_token
    url="https://fcm.googleapis.com/fcm/send"
    body={
        "notification":{
            "title":"Student Management System",
            "body":message,
            "click_action":"https://studentmanagementsystem22.herokuapp.com/staff_all_notification",
            "icon":"http://studentmanagementsystem22.herokuapp.com/static/dist/img/user2-160x160.jpg"
        },
        "to":token
    }
    headers={"Content-Type":"application/json","Authorization":"key=SERVER_KEY_HERE"}
    data=requests.post(url,data=json.dumps(body),headers=headers)
    notification=NotificationStaffs(staff_id=staff,message=message)
    notification.save()
    print(data.text)
    return HttpResponse("True")

