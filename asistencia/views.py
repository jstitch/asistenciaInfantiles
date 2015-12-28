from django.shortcuts import render
from django.utils import timezone
from .models import Participante

def participantes_list(request):
    participantes = Participante.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'asistencia/participantes_list.html', {'participantes': participantes})
