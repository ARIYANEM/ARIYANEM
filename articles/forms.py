from django import forms
from . import models

class ArticleCreate(forms.ModelForm):
    class Meta:
        model = models.Article
        fields =['title','body','image']
