from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length = 25)
    codigo = models.CharField(max_length = 25)
    carga_horaria_total = models.IntegerField()
    def __str__(self):
        return "Disciplina #%d: %s" % (int(self.id), self.nome)

    class Meta:
        verbose_name_plural = "disciplinas"
