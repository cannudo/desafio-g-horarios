from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from Disciplina.api.viewsets import DisciplinaViewSet
from Professor.api.viewsets import ProfessorViewSet
from SalaDeAula.api.viewsets import SalaDeAulaViewSet
from SlotDeHorario.api.viewsets import SlotDeHorarioViewSet
from Turma.api.viewsets import TurmaViewSet

rotas = routers.DefaultRouter()
rotas.register(r'disciplinas', DisciplinaViewSet)
rotas.register(r'professores', ProfessorViewSet)
rotas.register(r'salas', SalaDeAulaViewSet)
rotas.register(r'turmas', TurmaViewSet)
rotas.register(r'slots', SlotDeHorarioViewSet) 

urlpatterns = [
    path('', include(rotas.urls)),
    path('admin/', admin.site.urls),
]
