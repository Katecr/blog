from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.user.models import User


class UserAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'username','password'
    #         ),
    #     }),
    #     ('Información personal', {
    #         'fields': (
    #             'first_name','last_name','email'
    #         ),
    #     }),
    #     ('Permisos', {
    #         'fields': (
    #             'is_active','is_staff','is_superuser','groups','user_permissions'
    #         ),
    #     }),
    # )
    pass
    
admin.site.register(User, UserAdmin)