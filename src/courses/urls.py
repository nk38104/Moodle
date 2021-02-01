from django.urls import path
from . import views


# Set your urls here.

urlpatterns = [
    path('courses/', views.view_courses, name='courses'),
    path('create_course/', views.create_course, name='create_course'),
    path('edit_course/<int:course_id>', views.edit_course, name='edit_course'),
    path('delete_course/<int:course_id>', views.delete_course, name='delete_course'),
]


