from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Booking, Chapter, Video
from .serializers import CourseSerializer, BookingSerializer, ChapterSerializer, VideoSerializer

# ----------------------------------------
# Course Management
# ----------------------------------------

class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_teacher:
            raise PermissionDenied("Only teachers can create courses.")
        serializer.save(teacher=self.request.user)


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        course = self.get_object()
        if self.request.user != course.teacher:
            raise PermissionDenied("Only the teacher who created the course can update it.")
        serializer.save()

# ----------------------------------------
# Chapter Management
# ----------------------------------------

class ChapterCreateView(generics.CreateAPIView):
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        if self.request.user != course.teacher:
            raise PermissionDenied("Only the teacher who created the course can add chapters.")
        serializer.save(course=course)


class ChapterListView(generics.ListAPIView):
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        course = get_object_or_404(Course, id=self.kwargs.get('course_id'))
        return Chapter.objects.filter(course=course)

# ----------------------------------------
# Video Management
# ----------------------------------------

class VideoCreateView(generics.CreateAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        chapter = get_object_or_404(Chapter, id=self.kwargs.get('chapter_id'))
        if self.request.user != chapter.course.teacher:
            raise PermissionDenied("Only the teacher who created the course can add videos.")
        serializer.save(chapter=chapter)


class VideoListView(generics.ListAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        chapter = get_object_or_404(Chapter, id=self.kwargs.get('chapter_id'))
        return Video.objects.filter(chapter=chapter)

# ----------------------------------------
# Booking Management
# ----------------------------------------

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

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BookingDetailView(generics.RetrieveAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(student=self.request.user)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


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
