from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class StudentProfile(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Student Profile"

class TeacherProfile(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_teacher': True})
    expertise = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Teacher Profile"
