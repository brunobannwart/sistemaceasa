from django.db import models

# Create your models here.
class Extrato(models.Model):
	escola 				=	models.ForeignKey('escola.Escola', verbose_name='Escola', on_delete=models.CASCADE)	
	data_hora			=	models.DateTimeField(verbose_name='Data/Hora')
	produto 			=	models.ForeignKey('produto.Produto', verbose_name='Produto', on_delete=models.CASCADE)
	entrada_saida		=	models.CharField(verbose_name='E/S', max_length=1)
	tipo_mov			=	models.CharField('Tipo de movimentação', max_length=2)
	numero_documento	=	models.CharField('Número do documento', max_length=255)
	quantidade			=	models.IntegerField(verbose_name='Quantidade')
	saldo				=	models.IntegerField(verbose_name='Saldo')
	created_at			=	models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
	updated_at   		=	models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

	def __str__(self):
		return self.nome

	class Meta:
		db_table = 'extrato'
		verbose_name = 'Extrato'
		verbose_name_plural = 'Extratos'
		ordering = ['escola_id']
