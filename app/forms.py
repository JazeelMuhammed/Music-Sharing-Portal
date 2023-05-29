from django import forms
from .models import Song


class MusicUploadForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'author', 'file', 'is_private', 'is_public', 'is_protected']


