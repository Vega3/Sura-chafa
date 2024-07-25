from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('medico', 'Medico'),
        ('paciente', 'Paciente'),
    )
    role = models.CharField(max_length=10, choices=ROLES)
