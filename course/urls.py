from django.urls import path
from .views import CourseCreateView, CourseListView, CourseDetailView, BookCourseView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', CourseCreateView.as_view(), name='course_create'),
    path('courses/book/', BookCourseView.as_view(), name='course_book'),
]
