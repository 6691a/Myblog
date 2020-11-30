from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'body']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-title'}
            ),
            'category': forms.Select(
                attrs={'class': 'from-categoty'}
            ),
            'body': forms.CharField(
                widget=CKEditorUploadingWidget(
                    attrs={'class': 'from-body'}
                )
            )
        }
