from django.urls import path
from .views import login,TeacherView,NormalUserView,all_mb


urlpatterns = [
    path('login/',login),
    path('teacher-register/',TeacherView.as_view(),name='teacher_register'),
    path('normal-user-register/',NormalUserView.as_view(),name='normal_user_register'),
    path('all-mb/',all_mb)
]