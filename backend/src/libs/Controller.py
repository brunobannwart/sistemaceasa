from .Database import Database

class Controller:
	def __init__(self):
		self.db = Database()

	def efetuarLogin(self, cpf, senha):
		usuario = self.db.obterUsuario(cpf)
		
		if usuario != None:
			if usuario['senha_hash'] == senha:
				if usuario['tipo'] == 'E':
					return usuario

				else:
					return None
			else:
				return None
		else:
			return None

	def alterarSenha(self, cpf, senha):
		return self.db.alterarSenhaUsuario(cpf, senha)