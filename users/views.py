from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm  

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Obtiene el usuario del formulario
            auth_login(request, user)  # Inicia sesión al usuario
            return redirect('patient_home')  # Redirige a la vista patient_home después del login
    else:
        form = AuthenticationForm()  # Muestra un formulario vacío para GET
    return render(request, 'login.html', {'form': form})

def patient_home(request):
    return render(request, 'patient_home.html')