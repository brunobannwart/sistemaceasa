from django.contrib.auth.backends import BaseBackend
from usuario.models import Usuario

class LoginBackend(BaseBackend):
	def authenticate(request, cpf=None, senha_hash=None):
		try:
			usuario = Usuario.objects.get(cpf=cpf)

			if usuario.senha_hash == senha_hash:
				return usuario
			else:
				return False
		except:
			return None

	def get_user(self, id):
		try:
			usuario = Usuario.objects.get(id=id)
			return usuario
		except:
			return None