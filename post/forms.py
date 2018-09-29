from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write the title of the book...'
        }
    ),required=False)
    post = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ),required=False)
    post_para_2 = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ),required=False)
    post_para_3 = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ),required=False)
    captions = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ),required=False)
    captions_para_2 = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ),required=False)
    captions_para_3 = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the post'
        }
    ),required=False)
    quote = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mention about the subject...'
        }
    ),required=False)
    quote_by = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mention about the subject...'
        }
    ),required=False)

    related_post_1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the title of related post'
        }
    ),required=False)
    related_link_1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the link of related post'
        }
    ),required=False)
    related_post_2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the title of related post'
        }
    ),required=False)
    related_link_2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the link of related post'
        }
    ),required=False)
    related_post_3 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'write the title of related post'
        }
    ),required=False)
    related_link_3 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the link of related post'
        }
    ),required=False)

    # rating = forms.IntegerField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Enter the rating'
    #     }
    # ),required=False)
    class Meta:
        model = Post
        fields = ('category', 'title','post', 'post_para_2','post_para_3','captions',
                  'captions_para_2','captions_para_3', 'quote','quote_by',
                  'image','related_post_1', 'related_link_1','related_post_2',
                  'related_link_2', 'related_post_3', 'related_link_3', 'rating')