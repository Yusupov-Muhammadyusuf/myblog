from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'e.g. AI, Politics, Technology...'}),
            'title': forms.TextInput(attrs={'class': 'form-control title-input', 'placeholder': 'Title of your article...'}),
        }