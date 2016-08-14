from django.db import models
from django.utils import timezone


class Equipo(models.Model):
    nombre = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre


class Ciclo(models.Model):
    nombre = models.CharField(max_length=10, unique=True)
    inicio = models.DateField()
    fin    = models.DateField()

    def __str__(self):
        return self.nombre


class Participante(models.Model):
    nombre       = models.CharField(max_length=60)
    creator      = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre


class Encuentro(models.Model):
    nombre        = models.CharField(max_length=20)
    fecha         = models.DateField(unique=True)
    duracion      = models.IntegerField(default=2)
    ciclo         = models.ForeignKey(Ciclo, null=True, related_name='encuentros')
    participantes = models.ManyToManyField(Participante, through='Asistencia')

    def __str__(self):
        return self.nombre + " " + self.fecha.strftime("%Y")


class Asistencia(models.Model):
    participante = models.ForeignKey(Participante, related_name='asistencias')
    encuentro    = models.ForeignKey(Encuentro, related_name='asistencias')
    equipo       = models.ForeignKey(Equipo, related_name='asistencias')
    telefono     = models.CharField(max_length=15)

    def __str__(self):
        return str(self.participante) + ", " + str(self.encuentro) + ", " + str(self.equipo) + ", " + self.telefono

    class Meta:
        unique_together = (("participante", "encuentro", "equipo"), )
