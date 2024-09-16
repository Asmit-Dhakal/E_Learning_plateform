from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status
from .models import Course, Booking
from .serializers import CourseSerializer, BookingSerializer


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class BookCourseView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def post(self, request, *args, **kwargs):
        course_id = request.data.get('course')
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'detail': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

        if Booking.objects.filter(student=request.user, course=course).exists():
            return Response({'detail': 'Already booked for this course.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)

class BookedCoursesView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(student=self.request.user)

class BookingDetailView(generics.RetrieveAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(student=self.request.user)

class DeleteBookingView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        course_id = self.kwargs.get('course_id')
        try:
            booking = Booking.objects.get(student=self.request.user, course_id=course_id)
        except Booking.DoesNotExist:
            raise Http404
        return booking