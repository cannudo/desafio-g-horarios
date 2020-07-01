from django.db import models

class Turma(models.Model):
    opcoes = (
        ("Matutino", "Matutino"),
        ("Vespertino", "Vespertino"),
    )
    turno = models.CharField(max_length = 15, choices = opcoes)
    nome = models.CharField(max_length = 50)
    def __str__(self):
        return "Turma #%d: %s" % (int(self.id), self.nome)

    class Meta:
        verbose_name_plural = "turmas"
