from django.db import models
import uuid
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser, PermissionsMixin
)


# USER_TYPE = (
#     ('student', 'Student'),
#     ('staff', 'Staff'),
#     ('parent', 'Parent'),
#     ('alumni', 'Alumni'),
#     )

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nin = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField('email address', blank=True, unique=True)
    # user_type = models.CharField(max_length=150, choices=USER_TYPE, blank=True, help_text='type of user account')
    is_school_staff = models.BooleanField('school staff status', default=False)
    is_student = models.BooleanField('student status', default=False)
    is_alumni = models.BooleanField('alumni status', default=False)
    is_parent = models.BooleanField('parent status', default=False)

    is_active = models.BooleanField('active status', default=True)
    is_admin = models.BooleanField('admin status', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
