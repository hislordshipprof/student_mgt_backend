import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from Accounts.Api.serializers import *
from student_mgt_app.api.serializers import *
from student_mgt_app.models import *
from rest_framework.decorators import api_view
from Accounts.models import User

@api_view(['POST'])
def student_home(request):
    serializer=StudentsSerializer(Students.objects.get(user=request.user.id)).data
    return Response(serializer.data)

    # attendance_total=AttendanceReport.objects.filter(student_id=student_obj).count()
    # attendance_present=AttendanceReport.objects.filter(student_id=student_obj,status=True).count()
    # attendance_absent=AttendanceReport.objects.filter(student_id=student_obj,status=False).count()
    # course=Courses.objects.get(id=student_obj.course_id.id)
    # subjects=Subjects.objects.filter(course_id=course).count()
    # subjects_data=Subjects.objects.filter(course_id=course)
    # session_obj=SessionYearModel.object.get(id=student_obj.session_year_id.id)
    # class_room=OnlineClassRoom.objects.filter(subject__in=subjects_data,is_active=True,session_years=session_obj)

    # subject_name=[]
    # data_present=[]
    # data_absent=[]
    # subject_data=Subjects.objects.filter(course_id=student_obj.course_id)
    # for subject in subject_data:
    #     attendance=Attendance.objects.filter(subject_id=subject.id)
    #     attendance_present_count=AttendanceReport.objects.filter(attendance_id__in=attendance,status=True,student_id=student_obj.id).count()
    #     attendance_absent_count=AttendanceReport.objects.filter(attendance_id__in=attendance,status=False,student_id=student_obj.id).count()
    #     subject_name.append(subject.subject_name)
    #     data_present.append(attendance_present_count)
    #     data_absent.append(attendance_absent_count)

    # return render(request,"student_template/student_home_template.html",{"total_attendance":attendance_total,"attendance_absent":attendance_absent,"attendance_present":attendance_present,"subjects":subjects,"data_name":subject_name,"data1":data_present,"data2":data_absent,"class_room":class_room})
