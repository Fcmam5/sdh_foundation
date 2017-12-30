from django import forms
from .models import SEF_data, Slogo
from django.utils.translation import ugettext_lazy as _

class DataForm(forms.ModelForm):
    foundation_name = forms.CharField(max_length=128)
    description = forms.CharField(max_length=245, label= _("Item Description."))

    class Meta:
        model = SEF_data
        fields = ('title', 'body', )


class SponsorForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Slogo
        fields = ('image', )

class SearchForm(forms.Form):
    query = forms.CharField()
