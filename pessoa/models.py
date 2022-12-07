from django.db import models
from django.utils import timezone

TIPOS = [
    ("F", "Fisica"),
    ("J", "Juridica"),
]


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    cpf_cnpj = models.CharField(max_length=16, blank=False, unique=True)
    tipo = models.CharField(max_length=1, blank=False, choices=TIPOS, default="F")
    dt_criacao = models.DateTimeField(verbose_name="Data de criação", auto_now=True)
    dt_alteracao = models.DateTimeField(
        verbose_name="Data de alteração", auto_now_add=True
    )

    def __str__(self):
        return self.nome
