from django.urls import path
from .views import login, patient_home

urlpatterns = [
    path('login/', login, name='login'),
    path('patient_home/', patient_home, name='patient_home'),
]
