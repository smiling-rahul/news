from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write the title of the book...'
        }
    ))
    post = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ))
    post_para_2 = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ))
    post_para_3 = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ))
    captions = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ))
    captions_para_2 = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ))
    captions_para_3 = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ))
    quote = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mention about the subject...'
        }
    ))
    quote_by = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mention about the subject...'
        }
    ))

    related_post_1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the title of related post'
        }
    ))
    related_link_1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the link of related post'
        }
    ))
    related_post_2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the title of related post'
        }
    ))
    related_link_2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the link of related post'
        }
    ))
    related_post_3 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the title of related post'
        }
    ))
    related_link_3 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the link of related post'
        }
    ))

    rating = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the rating'
        }
    ))
    class Meta:
        model = Post
        fields = ('category', 'title','post', 'post_para_2','post_para_3','captions',
                  'captions_para_2','captions_para_3', 'quote','quote_by',
                  'image','related_post_1', 'related_link_1','related_post_2',
                  'related_link_2', 'related_post_3', 'related_link_3', 'rating')