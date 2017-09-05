from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import CustomUser
from .forms import UserChangeForm, UserCreationForm

class UsersUserAdmin(UserAdmin):
    fieldsets = (
                (None, {'fields': ('email','first_name','last_name', 'password', 'account_type')}),
                (_('Personal info'), {'fields': ('first_name','last_name','phone_number','speciality','grad','image','cv')}),
                (_('Permissions'), {'fields': ('groups',)}),
                # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            )
    add_fieldsets = (
                (None, {
                    'classes': ('wide',),
                    'fields': ('email', 'password1', 'password2','phone_number')}
                ),
                (_('Profile'), {'fields': ('first_name','last_name','phone_number','speciality','grad','image','cv')}),
                 (_('Permissions'), {'fields': ('account_type','groups',)}),
            )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('get_full_name','email', 'is_staff','is_superuser')
    list_display_links = ('email', 'get_full_name')
    search_fields = ('email', 'get_full_name')
    ordering = ('email',)



admin.site.register(CustomUser , UsersUserAdmin)
