from django.db import models

# Create your models here.
class Escola(models.Model):
	nome 		= 	models.CharField(verbose_name='Nome', max_length=100)
	rua 		= 	models.CharField(verbose_name='Rua', max_length=100)
	numero 		=	models.CharField(verbose_name='Número', max_length=10)
	bairro 		= 	models.CharField(verbose_name='Bairro', max_length=100)
	cidade 		= 	models.CharField(verbose_name='Cidade', max_length=100)
	estado 		= 	models.CharField(verbose_name='Estado', max_length=2)
	cep 		= 	models.CharField(verbose_name='CEP', max_length=10)
	diretor 	= 	models.CharField(verbose_name='Diretor(a)', max_length=100)
	created_at	=	models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
	updated_at	=	models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

	def __str__(self):
		return self.nome

	class Meta:
		db_table = 'escola'
		verbose_name = 'Escola'
		verbose_name_plural = 'Escolas'
		ordering = ['nome']