from django.db import models
from cliente.models.cliente import Cliente

TIPO = [("C", "Comercial"), ("P", "Pessoal")]


class Contato(models.Model):
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False)
    telefone = models.CharField(max_length=9, blank=True, null=True)
    dd = models.CharField(max_length=3, blank=True, null=True)
    email = models.EmailField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo

    class Meta:
        ordering = ["cliente"]
