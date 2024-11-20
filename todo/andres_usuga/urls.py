from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('crear_tarea',views.crear_tarea,name="crear_tarea")
    
]