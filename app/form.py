from django import forms
from app.models import MyAdmin,User

class LogForm(forms.ModelForm):
    class Meta:
        model = MyAdmin
        fields = ('nickname', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }


class SkForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('imie', 'nazwisko','opis')
        widgets = {
            'opis': forms.Textarea(attrs={'rows': 10, 'cols': 40})
        }