from django.urls import path
from .views import StudentProfileView, TeacherProfileView

urlpatterns = [
    path('student/profile/', StudentProfileView.as_view(), name='student_profile'),
    path('teacher/profile/', TeacherProfileView.as_view(), name='teacher_profile'),
]
