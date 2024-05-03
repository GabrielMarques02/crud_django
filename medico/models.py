from django.db import models
from django.db.models.fields.related import ForeignKey


class Especialidade(models.Model):
    especialidade = models.CharField(verbose_name='Especialidade', max_length=200)
    descricao = models.CharField(verbose_name='Descrição', max_length=1000)

    def __str__(self):
        return self.especialidade

class Medico(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=200)
    endereco = models.CharField(verbose_name='Endereço', max_length=200)
    email = models.EmailField(verbose_name='Email',)
    crm = models.CharField(verbose_name='CRM', max_length=11)
    telefone = models.CharField(verbose_name='Telefone',max_length=15 , validators=[])
    especialidade = ForeignKey(Especialidade, on_delete= models.CASCADE, blank=False, related_name='medico')
    
    def __str__(self):
        return self.nome

