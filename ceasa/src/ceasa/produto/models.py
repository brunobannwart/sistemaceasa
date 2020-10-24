from django.db import models

# Create your models here.
class Produto(models.Model):
	descricao 			= 	models.CharField(verbose_name='Descrição', max_length=255)
	created_at			=	models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
	update_at   		=	models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

	def __str__(self):
		return self.descricao

	class Meta:
		db_table = 'produto'
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'
		ordering = ['descricao']