from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import Courses
from enrollments.models import Enrollments


# Create your views here.
# --------- TODO ----------
#
# 1. Edit success and error handling for forms (e.g. deleting, editing, ...)

@login_required(login_url='login')
def view_courses(request):
    all_courses = Courses.objects.all()
    return render(request,'courses.html', {'courses':all_courses})


@login_required(login_url='login')
def create_course(request):
    if (request.method == 'POST'):
        course_form = CourseForm(request.POST)
        
        if (course_form.is_valid()):
            course_form.save()
            return redirect('courses')
        else:
            return HttpResponseNotAllowed(request.method)
            #return redirect('create_course')
    
    course_form = CourseForm()
    return render(request, 'create_course.html', {'course_form': course_form})


@login_required(login_url='login')
def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)

    if (request.method == 'POST'):
        course_data = CourseForm(request.POST, instance=course)
        
        if (course_data.is_valid()):
            course_data.save()
            return redirect('courses')
        else:
            return HttpResponseNotAllowed(request.method)
            # return redirect('edit_course')

    course_data = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'course_form':course_data})


@login_required(login_url='login')
def delete_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    
    if(course is not None):
        course.delete()
        
    return redirect('courses')


