from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    Nombre = forms.CharField(max_length=30, required=False, help_text='Optional')
    Apellido = forms.CharField(max_length=30, required=False, help_text='Optional')
    Email = forms.EmailField(max_length=254,help_text='Ingrese un mail valido')

    class Meta:
        model = User
        
        fields = [
            'username', 
            'Nombre', 
            'Apellido', 
            'Email', 
            'password1', 
            'password2', 
        ]