from django.shortcuts import render
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from .models import CustomUsers
from enrollments.models import Enrollments


# Create your views here.

@login_required(login_url='login')
def view_users(request):
    students = CustomUsers.objects.filter(role="STUDENT")
    professors = CustomUsers.objects.filter(role="PROFESSOR")
        
    return render(request, 'users.html', {'students':students, 'professors':professors})

@login_required(login_url='login')
def my_profile(request):
    user = get_user(request)
    user_courses = Enrollments.objects.filter(student_id=user.id)
    return render(request, 'user_profile.html', {'user':user, 'user_courses':user_courses})


