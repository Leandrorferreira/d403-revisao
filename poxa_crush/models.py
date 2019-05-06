from django.db import models

# Create your models here.
class Crush(models.Model):
    signo_opcoes = [
        ('áries', 'áries'),
        ('touro', 'touro'),
        ('gêmeos', 'gêmeos'),
        ('câncer', 'câncer'),
        ('leão', 'leão'),
        ('virgem', 'virgem'),
        ('libra', 'libra'),
        ('escorpião', 'escorpião'),
        ('sagitário', 'sagitário'),
        ('capricórnio', 'capricórnio'),
        ('aquário', 'aquário'),
        ('peixes', 'peixes')
    ]

    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    data = models.DateField()
    qualidade = models.CharField(max_length=100)
    defeito = models.CharField(max_length=100, default='não está comigo')
    reciproco = models.BooleanField(default=False)
    signo = models.CharField(max_length=100, choices=signo_opcoes)
    solteiro = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return self.nome