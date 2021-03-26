from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

# Create your models here.
class NewManager(BaseUserManager):

    def get_by_natural_key(self,email):
        return self.get(email=email)
    
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( email, password, **extra_fields)
    
    def create_teacher(self,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_teacher', True)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user( email, password, **extra_fields)
    


class NewUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(
        _("email_field"), 
        max_length=254,
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        }
    )
    mob_no=models.CharField(_("Mobile Number"), max_length=50)
    is_teacher=models.BooleanField(_("Is teacher"),default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects=NewManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELD=['mob_no']

    def __str__(self):
        return self.email.split('@')[0]

    def natural_key(self):
        return self.email
    
