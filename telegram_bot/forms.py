from django import forms
from .import models

class CreateArticles(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ["title","slug","body","thumb"]
