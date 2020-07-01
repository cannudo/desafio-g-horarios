from django.db import models
from SalaDeAula.models import SalaDeAula
from Disciplina.models import Disciplina
from Professor.models import Professor
from Turma.models import Turma 

class SlotDeHorario(models.Model):
    posicao = models.IntegerField(unique = True)
    sala_de_aula = models.ForeignKey(SalaDeAula, on_delete = models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete = models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete = models.CASCADE)
    def __str__(self):
        return "Slot #%d" % int(self.posicao)

    class Meta:
        verbose_name_plural = "Slots de horario"
