from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
import uuid


# USER_TYPE = (
#     ('student', 'Student'),
#     ('staff', 'Staff'),
#     ('parent', 'Parent'),
#     ('alumni', 'Alumni'),
#     )

    
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        extra_fields.setdefault('is_superuser', False)

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    username = models.CharField(verbose_name='username', max_length=150, unique=True, null=True, blank=True)
    surname = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nin = models.CharField(max_length=256, null=True, blank=True)
    # user_type = models.CharField(max_length=150, choices=USER_TYPE, blank=True, help_text='type of user account')
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    is_school_staff = models.BooleanField('school staff status', default=False)
    is_student = models.BooleanField('student status', default=False)
    is_alumni = models.BooleanField('alumni status', default=False)
    is_parent = models.BooleanField('parent status', default=False)
    is_active = models.BooleanField('active status', default=True)
    is_admin = models.BooleanField('admin status', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin