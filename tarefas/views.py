
from django.shortcuts import render, redirect

from .models import Tarefa


def inicio(request):
    tarefas = Tarefa.objects.all().order_by('-data_criacao')

    contexto = {
        'tarefas': tarefas,
        'total_tarefas': tarefas.count(),
        'tarefas_pendentes': tarefas.filter(status='PENDENTE').count(),
        'tarefas_concluidas': tarefas.filter(status='CONCLUIDA').count(),
    }

    return render(request, 'tarefas/inicio.html', contexto)


def nova_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        if titulo:
            Tarefa.objects.create(
                titulo=titulo,
                descricao=descricao
            )

            return redirect('inicio')

    return render(request, 'tarefas/nova_tarefa.html')
