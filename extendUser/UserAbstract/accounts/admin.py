from django.contrib import admin
from .models import AcademicUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


class NewUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ( 'isTeacher','is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'isTeacher'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'isTeacher','is_staff')
    list_filter = ('is_staff', 'is_superuser',  'isTeacher','is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'isTeacher')


admin.site.register(AcademicUser,NewUserAdmin)