from django import forms
from .models import Article, Categorie, Images
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    body = forms.CharField(max_length=245, label= _("Item Description."))

    class Meta:
        model = Article
        fields = ('title', 'body', )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('image', )

class SearchForm(forms.Form):
    query = forms.CharField()
