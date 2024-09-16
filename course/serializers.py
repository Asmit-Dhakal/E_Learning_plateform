from rest_framework import serializers
from .models import Course, Booking

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'teacher', 'title', 'description', 'video','validation_date', 'price']
        read_only_fields = [ 'teacher']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'student', 'course', 'booked_on']
        read_only_fields = ['student','booked_on']
