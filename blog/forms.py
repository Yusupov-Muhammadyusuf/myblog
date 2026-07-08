from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'e.g. AI, Politics, Technology...'}),
            'title': forms.TextInput(attrs={'class': 'form-control title-input', 'placeholder': 'Title of your article...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '8', 'placeholder': 'Tell your story...', 'style': 'line-height: 1.7; resize: none;'}),
        }