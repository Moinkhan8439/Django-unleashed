from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager

# Create your models here.

class NewUser(User):

    objects=UserManager()
    class Meta:
        proxy=True

    def get_email_name(self):
        return self.email.split('@')[0]