from rest_framework import serializers
from .models import Course, Booking

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'teacher', 'title', 'description', 'validation_date', 'price']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'student', 'course', 'booked_on']
