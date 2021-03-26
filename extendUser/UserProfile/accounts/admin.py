from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Teacher

admin.site.register(User, UserAdmin)

admin.site.register(Teacher)