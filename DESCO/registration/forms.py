from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(help_text="Requerido 254 caracteres como máximo y debe ser válido", required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    #Validación de que el email sea único
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email