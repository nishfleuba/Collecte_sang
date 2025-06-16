from django import forms
from .models import *

class loginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class DonneurForm(forms.ModelForm):
    class Meta:
        model = Donneur
        fields = ['nom', 'prenom', 'date_naissance', 'groupe_sanguin', 'adresse', 'tel']
        
class ReceveurForm(forms.ModelForm):
    class Meta :
        
        model = Receveur
        fields = ['nom','prenom','date_naissance','groupe_sanguin']
           
    