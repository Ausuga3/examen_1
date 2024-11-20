from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    q = Tareas.objects.all()
    return render(request,"index.html" ,{"dato":q})

def crear_tarea(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        ESTADOS = request.POST.get('estado')
        try:
            q= Tareas(
                nombre = nombre,
                estado = ESTADOS
            )
            q.save()
            messages.success(request, "La tarea se ha guardado correctamente!!")
        except Exception as e:
            messages.error(request, f"Error {e}!")
        return redirect("index")    
    else:
        return render(request,"crud/crear_tarea.html")

