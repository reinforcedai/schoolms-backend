from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User


GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    )

STATUS = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    )

TERM = (
    ('1', 'First Term'),
    ('2', 'Second Term'),
    ('3', 'Third Term'),
    )

SEMESTER = (
    ('1', 'First Semester'),
    ('2', 'Second Semester'),
    )

LEVEL = (
    ('1', 'First Year'),
    ('2', 'Second Year'),
    ('3', 'Third Year'),
    ('4', 'Fourth Year'),
    ('5', 'Fifth Year'),
    )

ATTENDANCE = (
		('P', 'Present'),
		('A', 'Absence'),
	)

GRADE = (
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D'),
		('F', 'F'),
	)

REMARK = (
		('PASS', 'PASS'),
		('FAIL', 'FAIL'),
	)

RELATIONSHIP = (
    ('F', 'Father'),
    ('M', 'Mother'),
    ('B', 'Brother'),
    ('S', 'Sister'),
    ('G', 'Guardian'),
    ('SP', 'Sponsor'),
    ('O', 'Others'),
)

class Student(models.Model):
    student = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='student',
        on_delete=models.CASCADE,
        )
    admission_number = models.CharField(max_length=256, null=True, blank=True)
    pin = models.CharField(max_length=256, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    date_of_birth = models.DateTimeField('Date of birth', null=True, blank=True)
    photo = models.ImageField(upload_to='', blank=True, help_text='upload profile photo')
    status = models.CharField(max_length=32, choices=STATUS)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, help_text='last modified date',)


    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name}'

    
    class Meta:
        verbose_name_plural = 'Students'


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_arm = models.CharField('Class arm', max_length=32, null=True, blank=True)
    term = models.CharField(choices=TERM, max_length=32, null=True, blank=True)
    session = models.CharField('Academic session', max_length=32, null=True, blank=True)
    continuous_assessment = models.FloatField('Continuous assessment score', max_length=32, default=0, null=True, blank=True)
    test_score = models.FloatField('Test score', max_length=32, default=0, null=True, blank=True)
    exam_score = models.FloatField('Exam score', max_length=32, default=0, null=True, blank=True)
    total_score = models.FloatField('Total score', max_length=32, default=0, null=True, blank=True)
    average_score = models.FloatField('Average score', max_length=32, default=0, null=True, blank=True)
    grade = models.CharField(choices=GRADE, max_length=32, null=True, blank=True)
    class_highest_score = models.FloatField('Class highest score', max_length=32, default=0, null=True, blank=True)
    class_lowest_score = models.FloatField('Class lowest score', max_length=32, default=0, null=True, blank=True)
    class_average_score = models.FloatField('Class average score', max_length=32, default=0, null=True, blank=True)
    class_position = models.CharField('Position in class', max_length=32, null=True, blank=True)
    total_students_number = models.IntegerField('Total number of students in class', default=0, null=True, blank=True)
    result_in_pdf = models.FileField(upload_to='', blank=True, help_text='upload result in PDF format')
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, help_text='last modified date',)


    def total_score(self):
        return self.test_score + self.exam_score

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance = models.CharField(choices=ATTENDANCE, max_length=32, null=True, blank=True)

# class Transcript(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)

# class NominalRoll(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
#     class Meta:
#         verbose_name_plural = 'Nominal Rolls'

class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Hostel(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    hostel = models.CharField(max_length=225, null=True, blank=True)
    room = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=225, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Hostel Allocations'

class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField('Parent or Guardian', max_length=32, null=True, blank=True)
    relationship = models.CharField(choices=RELATIONSHIP, max_length=32, null=True, blank=True)
    phone_number = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField('email address', max_length=255, unique=True,)

    class Meta:
        verbose_name_plural = 'Parents'

class Remark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.CharField(choices=TERM, max_length=32, null=True, blank=True)
    remark = models.CharField(choices=REMARK, max_length=32, null=True, blank=True)
    name = models.CharField('Instructor\'s name', max_length=32, null=True, blank=True)
    signature = models.FileField(upload_to='', blank=True, help_text='upload signature of the instructor')
    remark_in_pdf = models.FileField(upload_to='', blank=True, help_text='upload remark in PDF format')

    class Meta:
        verbose_name_plural = 'Remark on the student'

class Subject(models.Model):
    title = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Subjects'

class Performance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Performances'

class Newsletter(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    content = models.TextField(max_length=1024, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Newsletters'

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(student=instance)
