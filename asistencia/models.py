from django.db import models
from django.utils import timezone

class Participante(models.Model):
    nombre       = models.CharField(max_length=60)
    creator      = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
