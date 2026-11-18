
from django.db import models


class Tarefa(models.Model):

    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONCLUIDA', 'Concluída'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDENTE'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return self.titulo


class Historico(models.Model):

    tarefa = models.ForeignKey(
    Tarefa,
    on_delete=models.SET_NULL,
    related_name='historicos',
    null=True,
    blank=True
    )
    
    descricao = models.CharField(max_length=200)
    data_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Histórico'
        verbose_name_plural = 'Histórico'

    def __str__(self):
        return self.descricao
