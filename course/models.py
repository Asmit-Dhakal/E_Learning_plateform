

# Create your models here.

from django.db import models
from django.conf import settings

class Course(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_teacher': True})
    title = models.CharField(max_length=255)
    description = models.TextField()
    validation_date = models.DateField()
    video = models.FileField(upload_to='course_videos/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Booking(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='bookings')  # Add related_name
    booked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.username} booked {self.course.title}"
