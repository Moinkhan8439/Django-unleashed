from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm,UserCreationForm


class NewUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email' , 'password', 'mob_no' , 'is_staff','is_active' ,'is_superuser')
    list_filter = ('is_superuser','is_teacher')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ( 'mob_no','is_teacher', 'is_staff', 'is_superuser')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2','mob_no')}),
        ('Personal info', {'fields': ('is_teacher','is_staff', 'is_superuser',)}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email','mob_no')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(NewUser, NewUserAdmin)
