from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser , StaffUser , ScientificUser
from .forms import CustomUserChangeForm, CustomUserCreationForm , StaffUserCreationForm , StaffUserChangeForm

# class CustomUserAdmin(UserAdmin):
#             # The forms to add and change user instances

#             # The fields to be used in displaying the User model.
#             # These override the definitions on the base UserAdmin
#             # that reference the removed 'username' field
#     fieldsets = (
#                 (None, {'fields': ('email', 'password')}),
#                 (_('Personal info'), {'fields': ('phone_number',)}),
#                 (_('Permissions'), {'fields': ('is_staff',)}),
#                 # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#             )
#     add_fieldsets = (
#                 (None, {
#                     'classes': ('wide',),
#                     'fields': ('email', 'password1', 'password2')}
#                 ),
#             )
#     form = CustomUserChangeForm
#     add_form = CustomUserCreationForm
#     list_display = ('email', 'is_staff','is_superuser')
#     search_fields = ('email', )
#     ordering = ('email',)

# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(ScientificUser)
class staffUserAdmin(UserAdmin):
            # The forms to add and change user instances

            # The fields to be used in displaying the User model.
            # These override the definitions on the base UserAdmin
            # that reference the removed 'username' field
    
    
    fieldsets = (
                (None, {'fields': ('email','first_name','last_name')}),
                (_('Personal info'), {'fields': ('phone_number',)}),
                (_('Permissions'), {'fields': ('groups','password')}),
                # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            )
    add_fieldsets = (
                (None, {'classes': ('wide',),
                        'fields': ('email', 'password1', 'password2' ,'first_name','last_name','phone_number')}
                ),
                (_('Permissions'), {'fields': ('groups',)}),
                
            )
    form = StaffUserChangeForm
    add_form = StaffUserCreationForm 
    list_display = ('email', 'is_staff','is_superuser','is_member')
    search_fields = ('email', )
    ordering = ('email',)

admin.site.register(StaffUser , staffUserAdmin)



class ScientificUserAdmin(UserAdmin):
    fieldsets = (
                (None, {'fields': ('email','first_name','last_name')}),
                (_('Personal info'), {'fields': ('phone_number',)}),
                (_('Permissions'), {'fields': ('groups',)}),
                # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
            )
    add_fieldsets = (
                (None, {
                    'classes': ('wide',),
                    'fields': ('email', 'password1', 'password2' ,'first_name','last_name','phone_number','speciality','grad','image','cv')}
                ),
                 (_('Permissions'), {'fields': ('groups',)}),
            )
    form = StaffUserChangeForm
    add_form = StaffUserCreationForm 
    list_display = ('email', 'is_staff','is_superuser' ,'is_member')
    search_fields = ('email', )
    ordering = ('email',)



admin.site.register(ScientificUser , ScientificUserAdmin)