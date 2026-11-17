from django.contrib import admin
from .models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'data_criacao')
    list_filter = ('status',)
    search_fields = ('titulo',)