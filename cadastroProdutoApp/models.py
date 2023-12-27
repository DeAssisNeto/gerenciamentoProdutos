from django.db import models

from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    descricao = models.TextField(max_length=500)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(db_default=True)

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'