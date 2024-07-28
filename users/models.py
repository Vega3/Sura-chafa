from django.contrib.auth.models import AbstractUser
from django.db import models

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Consulta(models.Model):
    HORARIOS = [
        ('M', 'Mañana'),
        ('T', 'Tarde'),
        ('N', 'Noche')
    ]

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField()
    horario = models.CharField(max_length=1, choices=HORARIOS)

    def __str__(self):
        return f"{self.medico} - {self.dia} - {self.get_horario_display()}"

class Usuario(AbstractUser):
    ROLES = (
        ('medico', 'Medico'),
        ('paciente', 'Paciente'),
    )
    role = models.CharField(max_length=10, choices=ROLES)
