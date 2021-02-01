from django.urls import path
from . import views


urlpatterns = [
    path('enroll/<int:course_id>/<int:student_id>', views.enroll, name='enroll'),
    path('remove_enrollment/<int:course_id>/<int:student_id>', views.remove_enrollment, name='remove_enrollment'),
    path('course_passed/<int:course_id>/<int:student_id>', views.course_passed, name='course_passed'),
    path('student_enrollments/<int:student_id>', views.student_enrollments, name='student_enrollments'),
]


