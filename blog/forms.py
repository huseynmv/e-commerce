from django import forms
from .models import Blog, Comment
from django.db.models import fields

class BlogCommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body',)
    
    # class Meta:
    #     model = Blog
    #     fields = ('name','body',)
    #     widgets = {
    #         'name': forms.TextInput(
    #             attrs={'class': 'form-control', 'placeholder': 'Your Name...'}),
    #         'body': forms.Textarea(
    #             attrs={'class': 'form-control', 'placeholder': 'Your Message...'})
    #     }
