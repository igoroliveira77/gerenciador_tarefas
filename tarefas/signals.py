from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Tarefa, Historico


@receiver(post_save, sender=Tarefa)
def registrar_criacao_tarefa(sender, instance, created, **kwargs):

    if created:
        Historico.objects.create(
            tarefa=instance,
            descricao=f"Tarefa '{instance.titulo}' cadastrada."
        )