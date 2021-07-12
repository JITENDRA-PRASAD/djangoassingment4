from django.forms import fields
from django import forms
from .models import Comment, Post, Author


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = "__all__"



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"


"""
class LogInForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = "__all__"



class SingUpForm(forms.ModelForm):

    class Meta:
        model = Author
        fields= "__all__"

"""