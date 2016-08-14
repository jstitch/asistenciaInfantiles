from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Participante, Asistencia
from .forms import ParticipanteForm

def asistencia(request, cicloini, ciclofin):
    asistence = Asistencia.objects.filter(Asistencia.encuentro.ciclo.inicio==cicloini).filter(Asistencia.encuentro.ciclo.fin==ciclofin)
    return render(request, 'asistencia/asistencia.html', {'cicloini' : cicloini, 'ciclofin' : ciclofin})

def participantes_list(request):
    participantes = Participante.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'asistencia/participantes_list.html', {'participantes': participantes})

def participante_detail(request, pk):
    participante = get_object_or_404(Participante, pk=pk)
    return render(request, 'asistencia/participante_detail.html', {'participante': participante})

def participante_new(request):
    if request.method == "POST":
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save(commit=False)
            participante.creator = request.user
            participante.save()
            return redirect('participante_detail', pk=participante.pk)
    else:
        form = ParticipanteForm()
    return render(request, 'asistencia/participante_edit.html', {'form': form})

def participante_edit(request, pk):
    participante = get_object_or_404(Participante, pk=pk)
    if request.method == "POST":
        form = ParticipanteForm(request.POST, instance=participante)
        if form.is_valid():
            participante = form.save(commit=False)
            participante.author = request.user
            participante.save()
            return redirect('participante_detail', pk=participante.pk)
    else:
        form = ParticipanteForm(instance=participante)
    return render(request, 'asistencia/participante_edit.html', {'form': form})
