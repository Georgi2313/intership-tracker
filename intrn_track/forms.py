from django import forms
from .models import Card, Direction

class PostForm(forms.ModelForm):
    class Meta:
        model=Card
        fields=('title','text','status','section',)

class Process(forms.ModelForm):
    class Meta:
        model=Direction
        fields=('search',)