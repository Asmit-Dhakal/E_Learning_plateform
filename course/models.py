from django.db import models
from django.conf import settings

class Course(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_teacher': True})
    title = models.CharField(max_length=255)
    description = models.TextField()
    validation_date = models.DateField()
    thumbnail = models.FileField(upload_to='thumbnailphoto/', null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.title

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=255)
    description = models.TextField()
    short_clip = models.FileField(upload_to='short_clips/', null=True, blank=True)  # Preview clip for the chapter

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Video(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='course_videos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chapter.title} - {self.title}"

class Booking(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='bookings')
    booked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.username} booked {self.course.title}"
