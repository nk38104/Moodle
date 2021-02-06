from django.shortcuts import render
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from .models import CustomUsers
from enrollments.models import Enrollments
from users.enums import StatusChoices


# Create your views here.

@login_required(login_url='login')
def view_users(request):
    students = CustomUsers.objects.filter(role="STUDENT")
    professors = CustomUsers.objects.filter(role="PROFESSOR")
        
    return render(request, 'users.html', {'students':students, 'professors':professors})

@login_required(login_url='login')
def user_profile(request):
    user = get_user(request)
    user_courses = Enrollments.objects.filter(student_id=user.id)
    user.status = StatusChoices[user.status].value
    
    return render(request, 'user_profile.html', {'user':user, 'user_courses':user_courses})


