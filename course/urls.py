from django.urls import path
from .views import CourseCreateView, CourseListView, CourseDetailView, BookCourseView, BookedCoursesView, \
    BookingDetailView, DeleteBookingView

urlpatterns = [
    path('course/', CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/book/', BookCourseView.as_view(), name='course_book'),
    path('course/booked/', BookedCoursesView.as_view(), name='booked_courses'),
    path('course/book/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('course/book/delete/<int:course_id>/', DeleteBookingView.as_view(), name='delete_booking'),
]
