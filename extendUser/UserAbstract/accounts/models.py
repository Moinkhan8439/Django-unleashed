from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager


# Create your models here.
class AcademicUser(AbstractUser):
    isTeacher=models.BooleanField(default=False)

    objects=UserManager()
    
    @property
    def is_teacher(self):
        return isTeacher    

class AcademicUserManager(UserManager):

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('isTeacher', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('isTeacher', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', False)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)
