from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Tareas)
class TareasAdmin(admin.ModelAdmin):
    list_display = ['nombre','estado']
    search_fields = ['nombre','estado']


