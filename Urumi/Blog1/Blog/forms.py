from django import forms

from Blog.models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label="Your Name")
    email = forms.EmailField(label="Your Email")
    to = forms.EmailField(label="To Email")
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
