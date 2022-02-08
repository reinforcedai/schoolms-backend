from distutils.command.upload import upload
from django.db import models
from django.conf import settings
from django.utils import timezone


class School(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    motto = models.CharField(max_length=128, null=True, blank=True)
    logo = models.ImageField(upload_to='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'School Details'


class SchoolAssetManager(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    quantity = models.CharField(max_length=256, null=True, blank=True)
    size = models.CharField(max_length=256, null=True, blank=True)
    date_acquired = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'School Asset Manager'

class StaffProfile(models.Model):
    staff = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='staff_profile',
        on_delete=models.CASCADE,
        )

    class Meta:
        verbose_name_plural = 'Staff Profiles'


class Calendar(models.Model):
    pass

    class Meta:
        verbose_name_plural = 'Academic Calendar'

class AdmissionForm(models.Model):
    pass

    class Meta:
        verbose_name_plural = 'Admission Form'
