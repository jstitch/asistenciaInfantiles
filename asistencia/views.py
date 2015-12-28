from django.shortcuts import render

def participantes_list(request):
    return render(request, 'asistencia/participantes_list.html', {})
