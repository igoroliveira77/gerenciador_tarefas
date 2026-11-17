
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Tarefa, Historico


@receiver(pre_save, sender=Tarefa)
def verificar_status_anterior(sender, instance, **kwargs):

    if instance.pk:
        try:
            tarefa_antiga = Tarefa.objects.get(pk=instance.pk)
            instance.status_anterior = tarefa_antiga.status
        except Tarefa.DoesNotExist:
            instance.status_anterior = None


@receiver(post_save, sender=Tarefa)
def registrar_historico_tarefa(sender, instance, created, **kwargs):

    if created:
        Historico.objects.create(
            tarefa=instance,
            descricao=f"Tarefa '{instance.titulo}' cadastrada."
        )

    elif (
        getattr(instance, 'status_anterior', None) == 'PENDENTE'
        and instance.status == 'CONCLUIDA'
    ):
        Historico.objects.create(
            tarefa=instance,
            descricao=f"Tarefa '{instance.titulo}' foi concluída."
        )
