from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _
from .models import CustomUser , StaffUser , ScientificUser


class StaffUserCreationForm(UserCreationForm):
    class Meta :
        model = StaffUser
        fields = ("email",)

class StaffUserChangeForm(UserChangeForm):
    class Meta :
        model = StaffUser
        fields = ("email",)

class ScientificUserCreationForm(UserCreationForm):
    class Meta :
        model = ScientificUser
        fields = ("email",)

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """
    # def __init__(self, *args, **kargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kargs)
    #     del self.fields["username"]

    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    # def __init__(self, *args, **kargs):
    #     super(CustomUserChangeForm, self).__init__(*args, **kargs)
    #     del self.fields["username"]
    class Meta:
        model = CustomUser
        fields = ("email",)

class ContactByMailForm(forms.Form):
    """
        A form for handling Contact-Us section
    """
    name = forms.CharField(label=_('Name'), max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label=_('Subject'), max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label=_('Message'), required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

class RegistrationDemandForm(forms.Form):
    first_name = forms.CharField(label=_('First name') ,max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label=_('Last name') ,max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=_('Email') ,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    speciality = forms.CharField(label=_('Research Interests (speciality)'), help_text=_('Example: <b>Islamic architecture</b>'),max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    grade = forms.CharField(label=_('Academic rank'), help_text=_('Example: <b>Maitre Assistant</b>'), max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cv_file = forms.FileField(label=_('CV File') ,widget=forms.ClearableFileInput, help_text=_('Please upload a valid CV file (pdf, doc, docx)'))
    message = forms.CharField(label=_('Message') ,required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Tell us more about you, and why you want to create this account')}))
