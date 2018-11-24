from django.shortcuts import render
from django.http import JsonResponse
from .models import Horario,Materia
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def horarios(request, idMateria=None):
    if request.method == 'GET':
        horarios = Horario.objects.filter(idMateria=idMateria).values(
            'id',
            'idMateria',
            'estado',
            'aula',
            'grupo',
            'lun',
            'mar',
            'mier',
            'jue',
            'vie',
            'sab',
            'dom',
            'modulo',
        )
        return JsonResponse(list(horarios),safe=False)
    if request.method == "POST":
        idMateria = request.POST.get("idHorario")
        print(idMateria)
        horarios = Horario.objects.filter(id=idMateria)
        horarios.update(estado=not horarios[0].estado)
        print("Horarios ",horarios)
        if len(horarios) > 0:
            materias = Materia.objects.filter(horarios[0].idMateria_id)

            materias.update(estado=True)

            print("Materias ",materias)

        return JsonResponse({"error":None})

@csrf_exempt
def materias(request):
    if request.method == 'GET':
        materias = Materia.objects.all().values(
            'id',
            'idCuatrimestre',
            'estado',
            'descripcion',
            'codigo',
            'creditos',
        )
        return JsonResponse(list(materias),safe=False)
    if request.method == "POST":
        return JsonResponse({'results': None})