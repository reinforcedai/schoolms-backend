from django.db import models

# Create your models here.

class Alumni(models.Model):
    pass
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Alumni'
