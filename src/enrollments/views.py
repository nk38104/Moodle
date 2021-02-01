from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Enrollments
from courses.models import Courses
from users.models import CustomUsers

# Create your views here.

@login_required(login_url='login')
def enrollments(request):
    all_enrollments = Enrollments.objects.all()
    return render(request, 'enrollments.html', {'enrollments':all_enrollments})


@login_required(login_url='login')
def student_enrollments(request, student_id):
    student_enrollments = Enrollments.objects.filter(student=student_id)
    enrollment_course_id_list = [ enrollment.course.id for enrollment in student_enrollments ]    
    courses = Courses.objects.filter().exclude(id__in=enrollment_course_id_list)
    student = CustomUsers.objects.get(id=student_id)
    semesters = {}
    student_semester_end = 7 if student.status == "FULL_TIME" else 9
    
    # This needs optimisation, for sure, for sure, for the love of god
    if student.status == "FULL_TIME":
        for i in range(1, student_semester_end):
            semesters[i] = student_enrollments.filter(course__full_time_semester=i)
    else:
         for i in range(1, student_semester_end):
            semesters[i] = student_enrollments.filter(course__part_time_semester=i)
    # ------ OPTIMiSATION END ------
            
    return render(request, 'student_enrollments.html', {'student': student, 'enrollments':student_enrollments, 'courses':courses, 'semesters':semesters})


@login_required(login_url='login')
def enroll(request, course_id, student_id):
    student = CustomUsers.objects.get(id=student_id)
    course = Courses.objects.get(id=course_id)
    
    check_enrollment = Enrollments.objects.filter(student=student_id, course=course_id).exists()
    
    if check_enrollment is False:
        new_enrollment = Enrollments(student=student, course=course, status="enrolled")
        
        if (new_enrollment is not None):
            new_enrollment.save()
    else:
        enrollment = Enrollments.objects.get(student=student_id, course=course_id)
        
        enrollment.status = 'enrolled'
        enrollment.save()
    
    return redirect('student_enrollments', student_id=student_id)


@login_required(login_url='login')
def remove_enrollment(request, student_id, course_id):
    enrollment = Enrollments.objects.filter(student=student_id, course=course_id)
    
    if (enrollment is not None):
        enrollment.delete()
        
    return redirect('student_enrollments', student_id=student_id)


@login_required(login_url='login')
def course_passed(request, student_id, course_id):
    enrollment = Enrollments.objects.get(student=student_id, course=course_id)
    
    if (enrollment is not None):
        enrollment.status = 'passed'
        enrollment.save()
        
    return redirect('student_enrollments', student_id=student_id)
    

