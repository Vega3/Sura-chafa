from django.urls import path
from . import views
from .views import login, patient_home

urlpatterns = [
    path('login/', login, name='login'),
    path('patient_home/', patient_home, name='patient_home'),
    path('reserva_cita/', views.reserva_cita, name='reserva_cita'),
]
