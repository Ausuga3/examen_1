from django.db import models

# Create your models here.

class Tareas(models.Model):
    nombre = models.CharField(max_length=254, verbose_name="Nombre de la tarea")
    ESTADOS=(
        (0,"Nuevas"),
        (1,"Terminadas"),
        (2,"Eliminadas"),
    )
    estado = models.IntegerField(choices=ESTADOS, default=0, blank=True)

    def __str__(self):
        return self.get_estado_display()
    