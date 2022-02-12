from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from allauth.account.models import EmailAddress
from rest_framework.authtoken.models import TokenProxy

from .models import User


class UserAdmin(BaseUserAdmin):

    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Personal info', {'fields': ('surname', 'first_name', 'last_name', 'email',)}),
    #     ('User Type', {'fields': ('is_school_staff', 'is_student', 'is_alumni', 'is_parent',)}),
    #     ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser', 'groups', 'user_permissions',)}),
    #     ('Important Dates', {'fields': ('last_login', 'date_joined',)})
    # )
   
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialApp)
admin.site.unregister(TokenProxy)
admin.site.unregister(EmailAddress)

