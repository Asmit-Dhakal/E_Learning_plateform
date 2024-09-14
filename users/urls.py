from django.urls import path
from .views import TeacherRegisterView, StudentRegisterView, TeacherLoginView, StudentLoginView, TeacherDashboardView, StudentDashboardView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/teacher/', TeacherRegisterView.as_view(), name='register_teacher'),
    path('register/student/', StudentRegisterView.as_view(), name='register_student'),
    path('login/teacher/', TeacherLoginView.as_view(), name='login_teacher'),
    path('login/student/', StudentLoginView.as_view(), name='login_student'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('teacher-dashboard/', TeacherDashboardView.as_view(), name='teacher_dashboard'),
    path('student-dashboard/', StudentDashboardView.as_view(), name='student_dashboard'),
]
