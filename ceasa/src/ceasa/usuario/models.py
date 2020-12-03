from django.db import models
import hashlib

# Create your models here.
class Usuario(models.Model):
	nome 				= 	models.CharField(verbose_name='Nome', max_length=100)
	cpf					= 	models.CharField(verbose_name='CPF', max_length=14, unique=True)
	email				=	models.EmailField(verbose_name='Email', max_length=45, unique=True)
	telefone 			= 	models.CharField(verbose_name='Telefone', max_length=15)
	senha_hash			=	models.CharField(verbose_name='Senha', max_length=64)
	tipo				=	models.CharField(verbose_name='Tipo', max_length=1)
	escola				=	models.ForeignKey('escola.Escola', on_delete=models.CASCADE, blank=True, null=True)

	is_authenticated	=	models.BooleanField(verbose_name='Autenticado', default=False)
	last_login			=	models.DateTimeField(verbose_name='Último login', blank=True, null=True)
	created_at			=	models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
	update_at   		=	models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

	def __str__(self):
		return self.nome

	class Meta:
		db_table = 'usuario'
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'
		ordering = ['nome']
