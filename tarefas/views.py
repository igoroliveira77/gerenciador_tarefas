
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

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


@require_POST
def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if tarefa.status == 'PENDENTE':
        tarefa.status = 'CONCLUIDA'
        tarefa.save(update_fields=['status'])

    return redirect('inicio')

@require_POST
def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()

    return redirect('inicio')