from rest_framework import serializers
from .models import Course, Booking, Chapter, Video, Payment


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_file', 'upload_date']


class ChapterSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = ['id', 'title', 'description', 'videos']


class CourseSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'teacher', 'title', 'description', 'thumbnail', 'validation_date', 'price', 'chapters']
        read_only_fields = ['teacher']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['transaction_id', 'amount', 'status']


class BookingSerializer(serializers.ModelSerializer):
    payment_info = PaymentSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'student', 'course', 'booked_on', 'payment_info']
        read_only_fields = ['student', 'booked_on']

    def create(self, validated_data):
        payment_data = validated_data.pop('payment_info', None)
        booking = Booking.objects.create(**validated_data)

        if payment_data:
            Payment.objects.create(
                student=booking.student,
                course=booking.course,
                amount=booking.course.price,
                transaction_id=payment_data.get('transaction_id'),
                status=payment_data.get('status', 'pending')
            )

        return booking
