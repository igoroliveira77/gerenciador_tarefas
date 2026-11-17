
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

    def __str__(self):
        return self.titulo

class Historico(models.Model):

    tarefa = models.ForeignKey(
        Tarefa,
        on_delete=models.CASCADE,
        related_name='historicos'
    )
    descricao = models.CharField(max_length=200)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao
