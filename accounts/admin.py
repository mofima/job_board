from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model 

from .models import Profile, CustomUser 
from .forms import CustomUserChangeForm, CustomUserCreationForm

user = get_user_model()

class ProfileInline(admin.StackedInline):
    model = Profile 
    can_delete = False 
    verbose_name_plural = 'Plural'
    fk_name = 'user'
    raw_id_fields = ['user']


class CustomUserAdmin(UserAdmin):
    # Add the inlines to the CustomUserAdmin
    inlines = (ProfileInline,)

    # If you have custom forms, register them here
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # Customize the display fields in the admin panel
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    # For creating and editing users, specify which fields to display
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

# Register the CustomUser and the customized admin
admin.site.register(CustomUser, CustomUserAdmin)