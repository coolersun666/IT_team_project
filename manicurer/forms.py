from django import forms
from django.contrib.auth.models import User


from manicurer.models import UserProfile, Picture, Comment


class UploadForm(forms.Form):
    picturefile = forms.ImageField(
        label='Select a picture',
    )
    name=forms.CharField(label='Put a name')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class CommmentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Comment
        fields = ('content')


