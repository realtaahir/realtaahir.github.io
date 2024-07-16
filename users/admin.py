from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'username', 'email', 'phone_number', 'city', 'premium', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'premium', 'city', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'city', 'premium')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active', 'is_staff', 'premium')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('-date_joined',)  # Order by date_joined in descending order to show recent users on top

admin.site.register(CustomUser, CustomUserAdmin)
