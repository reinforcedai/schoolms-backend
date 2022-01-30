from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.first_name