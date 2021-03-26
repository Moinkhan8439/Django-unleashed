from django.db import models
from django.contrib.auth.models import (AbstractUser)
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    pass

class Teacher(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telephone=models.CharField(max_length=13)
    class Meta:
        verbose_name = ("Teacher")
        verbose_name_plural = ("Teachers")

    def __str__(self):
        return self.user.username

    def natural_key(self):
        return self.user.email