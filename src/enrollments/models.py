from django.db import models
from users.models import CustomUsers
from courses.models import Courses


# Create your models here.

class Enrollments(models.Model):
    student     = models.ForeignKey(CustomUsers, on_delete=models.CASCADE, null=False)
    course      = models.ForeignKey(Courses, on_delete=models.CASCADE, null=False)
    status      = models.CharField(max_length=64, null=False)
    
    def __str__(self):
        return f'{self.student} {self.course} {self.status}'
    
    
    