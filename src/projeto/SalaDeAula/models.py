from django.db import models

class SalaDeAula(models.Model):
    nome = models.CharField(max_length = 40)
    tipos = (
        ("Sala regular", "Sala regular"),
        ("Laboratório", "Laboratório"),
        ("Audiovisual", "Audiovisual"),
        ("Auditório", "Auditório"),
        ("Miniauditório", "Miniauditório"),
    )
    tipo = models.CharField(max_length = 15, choices = tipos)
    numero = models.IntegerField()
    def __str__(self):
        return "Sala de aula #%d: %s" % (int(self.id), self.nome)

    class Meta:
        verbose_name_plural = "Salas de aula"
