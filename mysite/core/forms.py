from django import forms

from .models import Fil


class FilForm(forms.ModelForm):
    class Meta:
        model = Fil
        fields = ('title', 'author', 'pdf', 'cover')
