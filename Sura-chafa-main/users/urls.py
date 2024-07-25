from django.urls import path
from .views import registro

urlpatterns = [
    path('register/', register, name='register'),
]
