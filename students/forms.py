from django import forms
from .models import Student
from django.contrib.auth.forms import AuthenticationForm

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['nombre', 'apellido', 'dni', 'carrera']

class LoginForm(AuthenticationForm):
    pass
