from django import forms
from app.models import User

class LogForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('imie', 'nazwisko','opis')
        widgets = {
            'opis': forms.Textarea(attrs={'rows': 10, 'cols': 40})
        }