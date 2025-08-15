from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'What\'s happening?'}),
        }