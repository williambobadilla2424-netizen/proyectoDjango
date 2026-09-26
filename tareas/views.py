from django.shortcuts import get_object_or_404, redirect, render
from .models import Tareas

def Inicio(request):
    tareas = Tareas.objects.all()
    return render(request, "inicio.html",{'tareas':tareas})

def crearTarea(request):
    if request.method == 'GET':
        return render(request, "crear_tarea.html")
    else:
        print(request.POST)
        try:
            print(request.POST)
            tareas = Tareas(
                titulo = request.POST.get('titulo'),
                descripciom = request.POST.get('descripcion',''),   
                fecha = request.POST.get('fecha',"2026-01-01")
            )
            tareas.save()
            return redirect('crearTarea')
        except ValueError as e:
            return render(request, "crear_tarea.html",{
                "error" : e
            })

def detalleTarea(request, tarea_id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tareas,pk = tarea_id)
        return render(request,'detalle_tarea.html',{
            'tarea':tarea
        })
    else:
        tarea = get_object_or_404(Tareas,pk= tarea_id)
        tarea.titulo = request.POST.get('titulo')
        tarea.descripciom = request.POST.get('descripciom')
        tarea.fecha = request.POST.get('fecha')
        tarea.save()
        return redirect('inicio')

def eliminarTarea(request,tarea_id):
    tarea = get_object_or_404(Tareas,pk=tarea_id)
    tarea.delete()
    return redirect('inicio')