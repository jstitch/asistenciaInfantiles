from django.contrib import admin
from .models import Ciclo, Equipo, Participante, Encuentro, Asistencia

admin.site.register(Ciclo)
admin.site.register(Equipo)
admin.site.register(Participante)
admin.site.register(Encuentro)
admin.site.register(Asistencia)
