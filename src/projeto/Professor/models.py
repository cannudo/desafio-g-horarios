from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length = 45)
    telefone = models.CharField(max_length = 15)
    email = models.CharField(max_length = 90)
    matricula = models.CharField(max_length = 15)
    def __str__(self):
        return "Professor #%d: %s" % (int(self.id), self.nome)

    class Meta:
        verbose_name_plural = "professores"
