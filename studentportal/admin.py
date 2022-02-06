from django.contrib import admin

from .models import (
    Student,
    Attendance,
    Result,
    # Transcript,
    # NominalRoll,
    Invoice,
    Hostel,
    Parent,
    Subject,
    Performance,
    )

admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Result)
# admin.site.register(Transcript)
# admin.site.register(NominalRoll)
admin.site.register(Invoice)
admin.site.register(Hostel)
admin.site.register(Parent)
admin.site.register(Subject)
admin.site.register(Performance)
# admin.site.register()
# admin.site.register()
