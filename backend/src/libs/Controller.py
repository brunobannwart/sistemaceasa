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

	def novoRomaneio(self, codigoEscola, numeroRomaneio, dataHora, codigoProduto, quantidade, codigoUsuario):
		produto = self.db.obterProduto(codigoProduto)

		if produto != None:
			estoque = self.db.obterEstoque(codigoEscola, produto['id'])

			if estoque != None:
				novoSaldo = quantidade + estoque['quantidade']
				atualizar = self.db.atualizarEstoque(estoque['id'], novoSaldo)

				if atualizar:
					existeRomaneio = self.db.obterSequenciaRomaneio(numeroRomaneio)

					if existeRomaneio != None:
						sequenciaRomaneio = existeRomaneio['sequencia'] + 1

					else:
						sequenciaRomaneio = 1

					romaneio = self.db.cadastrarRomaneio(codigoEscola, numeroRomaneio, sequenciaRomaneio, dataHora, codigoProduto, quantidade, codigoUsuario)

					if romaneio:
						extrato = self.db.cadastrarExtrato(codigoEscola, numeroRomaneio, dataHora, 'RO', 'E', produto['id'], quantidade, novoSaldo)

						if extrato:
							return True

						else:
							return False
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False

	def novaRequisição(self, codigoEscola, dataHora, tipo, codigoProduto, quantidade, codigoUsuario):
		produto = self.db.obterProduto(codigoProduto)

		if produto != None:
			estoque = self.db.obterEstoque(codigoEscola, produto['id'])

			if estoque != None:
				if tipo == 'DV':
					novoSaldo = quantidade + estoque['quantidade']
					ES = 'E'

				else:
					if tipo == 'AJ':
						novoSaldo = quantidade

						if quantidade >= estoque['quantidade']:
							ES = 'E'

						else:
							ES = 'S'

					else:
						novoSaldo = estoque['quantidade'] - quantidade

						if novoSaldo >= 0:
							ES = 'S'

						else:
							return False

				atualizar = self.db.atualizarEstoque(estoque['id'], novoSaldo)

				if atualizar:
					ultimaRequisição = self.db.obterUltimaRequisição(codigoEscola)

					if ultimaRequisição != None:
						novoDocumento = int(ultimaRequisição['numero_documento']) + 1

					else:
						novoDocumento = 1

					requisição = self.db.cadastrarRequisição(codigoEscola, str(novoDocumento), dataHora, tipo, ES, codigoProduto, quantidade, codigoUsuario)

					if requisição:
						extrato = self.db.cadastrarExtrato(codigoEscola, str(novoDocumento), dataHora, tipo, ES, produto['id'], quantidade, novoSaldo)

						if extrato:
							return True

						else:
							return False
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False