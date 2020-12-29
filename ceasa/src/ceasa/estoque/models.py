from django.db import models

# Create your models here.
class Estoque(models.Model):
	escola	     		=	models.ForeignKey('escola.Escola', verbose_name='Escola', on_delete=models.CASCADE)
	produto 			=	models.ForeignKey('produto.Produto', verbose_name='Produto', on_delete=models.CASCADE)
	quantidade			=	models.IntegerField(verbose_name='Quantidade em estoque')
	minimo				=	models.IntegerField(verbose_name='Estoque mínimo')
	created_at			=	models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
	updated_at   		=	models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

	def __str__(self):
		return str(self.id)

	class Meta:
		db_table = 'estoque'
		verbose_name = 'Estoque'
		verbose_name_plural = 'Estoques'
		ordering = ['escola_id']