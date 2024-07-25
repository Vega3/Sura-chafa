from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from .models import Cita

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'role']


class ReservaCitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'medico']