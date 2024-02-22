from django.db import models

# Create your models here.
class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()
    sobrenome = models.TextField()
    cidade = models.TextField()
    estado = models.TextField()
    email = models.TextField()
    cep = models.TextField()
    passworld = models.TextField()

class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.TextField()
    data = models.DateField()
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to="images/", blank=True, null=True)