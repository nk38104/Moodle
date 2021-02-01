from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUsers


# Register your models here.

class CustomUsersAdmin(UserAdmin):
    list_display = ('email', 'date_joined',  'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('id', 'date_joined', 'last_login')
    ordering = ('email', 'last_name')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CustomUsers, CustomUsersAdmin)


