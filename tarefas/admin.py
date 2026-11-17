
from django.contrib import admin
from .models import Tarefa, Historico


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'data_criacao')
    list_filter = ('status',)
    search_fields = ('titulo',)
    ordering = ('-data_criacao',)


@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'tarefa', 'data_registro')
    list_filter = ('data_registro',)
    search_fields = ('descricao', 'tarefa__titulo')
    ordering = ('-data_registro',)
    readonly_fields = ('tarefa', 'descricao', 'data_registro')
