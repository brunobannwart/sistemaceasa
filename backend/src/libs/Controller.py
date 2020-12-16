from .Database import Database
from .Utils import criarHashSenha, criarSenhaAleatoria
import os

class Controller:
	def __init__(self, templates_dir):
		self.db = Database()
		self.templates = templates_dir

	def efetuarLogin(self, cpf, senha):
		usuario = self.db.obterUsuario(cpf)
		hashSenha = criarHashSenha(senha)
		
		if usuario != None:
			if usuario['senha_hash'] == hashSenha:
				if usuario['tipo'] == 'E':
					return usuario
				else:
					return None
			else:
				return None
		else:
			return None

	def alterarSenha(self, cpf, senha):
		hashSenha = criarHashSenha(senha)
		return self.db.alterarSenhaUsuario(cpf, hashSenha)

	def redefinirSenha(self, cpf):
		usuario = self.db.obterUsuario(cpf)

		if usuario != None:
			contexto = {
				'nome': usuario['nome'].upper(),
				'senha': criarSenhaAleatoria('0123456789', 6)
			}

			resultado = enviarEmail('Esqueci minha senha', os.path.join(self.templates, 'email.html'), 
							contexto, 'CEASA <noreply@gmail.com>', usuario['email']
						)

			if resultado:
				return self.alterarSenha(cpf, criarHashSenha(contexto['senha']))
			else:
				return None
		else:
			return None

	def historicoUsuario(self, usuarioID):
		romaneios = self.db.obterRomaneiosUsuario(usuarioID)
		requisições = self.db.obterRequisiçõesUsuario(usuarioID)

		return romaneios, requisições