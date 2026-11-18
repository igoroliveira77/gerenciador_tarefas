
from django.contrib import admin
from django.urls import path

from tarefas import views

admin.site.site_header = 'Gerenciador de Tarefas'
admin.site.site_title = 'Painel Administrativo'
admin.site.index_title = 'Bem-vindo ao Gerenciador de Tarefas'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nova-tarefa/', views.nova_tarefa, name='nova_tarefa'),
    path('admin/', admin.site.urls),
    path('concluir-tarefa/<int:tarefa_id>/', views.concluir_tarefa, name='concluir_tarefa'),
    path('excluir-tarefa/<int:tarefa_id>/', views.excluir_tarefa, name='excluir_tarefa'),
]
