from django.urls import path
from .views import normal_user_register,login,TeacherView


urlpatterns = [
    path('login/',login),
    path('teacher-register/',TeacherView.as_view(),name='teacher_register'),
    path('normal-user-register/',normal_user_register,name='normal_user_register'),
]
