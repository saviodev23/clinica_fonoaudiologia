from django.db import models
# from accounts.models import Paciente, Profissional
from django.contrib.auth.models import User
class Consulta(models.Model):
    motivo_choices = (
        ('fala', 'problema de fala'),
    )
    # paciente = models.ForeignKey(to='accounts.Profissional', on_delete=models.CASCADE)
    # profissional = models.ForeignKey(to='accounts.Profissional', on_delete=models.CASCADE)
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Paciente', blank=True, null=True)
    profissional = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Profissional', blank=True, null=True)
    data = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=6, choices=motivo_choices)
    preco = models.DecimalField(default=0.0, max_digits=8, decimal_places=2, blank=True, null=True)
    atestado = models.ImageField(upload_to='uploads/% Y/% m/% d/', blank=True, null=True)
