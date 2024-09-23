from rest_framework import serializers
from .models import Course, Booking, Chapter, Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_file', 'upload_date']

class ChapterSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = ['id', 'title', 'description', 'short_clip', 'videos']

class CourseSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'teacher', 'title', 'description', 'thumbnail', 'validation_date', 'price', 'chapters']
        read_only_fields = ['teacher']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'student', 'course', 'booked_on']
        read_only_fields = ['student', 'booked_on']
