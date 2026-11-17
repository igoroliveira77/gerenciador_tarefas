
from django.contrib import admin
from django.urls import path

admin.site.site_header = 'Gerenciador de Tarefas'
admin.site.site_title = 'Painel Administrativo'
admin.site.index_title = 'Bem-vindo ao Gerenciador de Tarefas'

urlpatterns = [
    path('admin/', admin.site.urls),
]
