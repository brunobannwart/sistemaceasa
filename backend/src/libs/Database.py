import mysql.connector as mysql

class Database:
	def __init__(self):
		self.conexao = mysql.connect(host='localhost', user='ceasa', password='projeto$ceasa', database='db_ceasa', auth_plugin='mysql_native_password')
		self.cursor = self.conexao.cursor()
		self.__formarTabelas()

	def __formarTabelas(self):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS `romaneio`(`id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT, `codigo_escola` INT, `numero_romaneio` VARCHAR(100), `sequencia` INT, `data_hora` DATETIME, `codigo_produto` VARCHAR(12), `quantidade` INT, `codigo_usuario` INT) ENGINE=InnoDB")
		self.cursor.execute("CREATE TABLE IF NOT EXISTS `requisicao`(`id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT, `codigo_escola` INT, `numero_documento` INT, `data_hora` DATETIME, `tipo` VARCHAR(2), `entrada_saida` VARCHAR(1), `codigo_produto` VARCHAR(12), `quantidade` INT, `codigo_usuario` INT) ENGINE=InnoDB")

	def obterUsuario(self, cpf):
		try:
			self.cursor.execute("SELECT * FROM `usuario` WHERE cpf=%s", [cpf])
			resultado = self.cursor.fetchone()

			if resultado != None:
				usuario = {
					'id': resultado[0],
					'nome': resultado[1],
					'cpf': resultado[2],
					'email': resultado[3],
					'telefone': resultado[4],
					'senha_hash': resultado[5],
					'tipo': resultado[6],
					'escola': resultado[7]
				}

				return usuario
			else:
				return None
				
		except:
			return None
	
	def alterarSenhaUsuario(self, cpf, senha):
		try:
			self.cursor.execute("UPDATE `usuario` SET `senha_hash`=%s WHERE `cpf`=%s", [senha, cpf])
			self.conexao.commit()
			return True

		except:
			return False

	def obterRomaneiosUsuario(self, usuarioID):
		try:
			romaneios = []

			self.cursor.execute("SELECT * FROM `romaneio` WHERE `codigo_usuario`=%s", [usuarioID])
			resultados = self.cursor.fetchall()

			for resultado in resultados:
				self.cursor.execute("SELECT * FROM `escola` WHERE `id`=%s", resultado[1])
				escola = self.cursor.fetchone()

				self.cursor.execute("SELECT * FROM `produto` WHERE `codigo`=%s", resultado[4])
				produto = self.cursor.fetchone()

				if escola != None and produto != None:
					romaneio = {
						'id': resultado[0],
						'escola': escola[1],
						'numero_romaneio': resultado[2],
						'data_hora': resultado[3],
						'produto': produto[2],
						'quantidade': resultado[5],
						'codigo_usuario': resultado[6]
					}

					romaneios.append(romaneio)

			return romaneios
			
		except:
			return []

	def obterRequisiçõesUsuario(self, usuarioID):
		try:
			requisições = []

			self.cursor.execute("SELECT * FROM `requisicao` WHERE `codigo_usuario`=%s", [usuarioID])
			resultados = self.cursor.fetchall()

			for resultado in resultados:
				self.cursor.execute("SELECT * FROM `escola` WHERE `id`=%s", resultado[1])
				escola = self.cursor.fetchone()

				self.cursor.execute("SELECT * FROM `produto` WHERE `codigo`=%s", resultado[4])
				produto = self.cursor.fetchone()

				if escola != None and produto != None:
					requisição = {
						'id': resultado[0],
						'escola': escola[1],
						'numero_documento': resultado[2],
						'data_hora': resultado[3],
						'produto': produto[2],
						'quantidade': resultado[5],
						'codigo_usuario': resultado[6]
					}

					requisições.append(requisição)

			return requisições

		except:
			return []

	def obterProduto(self, codigoProduto):
		try:
			self.cursor.execute("SELECT * FROM `produto` WHERE `codigo`=%s", [codigoProduto])
			resultado = self.cursor.fetchone()

			if resultado != None:
				produto = {
					'id': resultado[0],
					'codigo': resultado[1],
					'descricao': resultado[2],
				}

				return produto

			else:
				return None

		except:
			return None

	def obterEstoque(self, escolaID, produtoID):
		try:
			self.cursor.execute("SELECT * FROM `estoque` WHERE `escola_id`=%s AND `produto_id`=%s", [escolaID, produtoID])
			resultado = self.cursor.fetchone()

			if resultado != None:
				estoque = {
					'id': resultado[0],
					'escola': resultado[1],
					'produto': resultado[2],
					'quantidade': resultado[3],
					'minimo': resultado[4],
				}

				return estoque
			
			else:
				return None

		except:
			return None

	def atualizarEstoque(self, estoqueID, quantidade):
		try:
			self.cursor.execute("UPDATE `estoque` SET `quantidade`=%s WHERE `id`=%s", [quantidade, estoqueID])
			self.conexao.commit()
			return True

		except:
			return False

	def cadastrarRomaneio(self, codigoEscola, numeroRomaneio, sequencia, dataHora, codigoProduto, quantidade, codigoUsuario):
		try:
			self.cursor.execute("INSERT INTO `romaneio` (`codigo_escola`, `numero_romaneio`, `sequencia`, `data_hora, `codigo_produto`, `quantidade`, `codigo_usuario`) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
				[codigoEscola, numeroRomaneio, sequencia, dataHora, codigoProduto, quantidade, codigoUsuario])
			self.conexao.commit()
			return True

		except:
			return False

	def cadastrarRequisição(self, codigoEscola, numeroDocumento, dataHora, tipo, eS, codigoProduto, quantidade, codigoUsuario):
		try:
			self.cursor.execute("INSERT INTO `requisicao` (`codigo_escola`, `numero_documento`, `data_hora, `tipo`, `entrada_saida`, `codigo_produto`, `quantidade`, `codigo_usuario`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
				[codigoEscola, numeroDocumento, dataHora, tipo, eS, codigoProduto, quantidade, codigoUsuario])
			self.conexao.commit()
			return True

		except:
			return False

	def cadastrarExtrato(self, escolaID, numeroDocumento, dataHora, tipo, eS, produtoID, quantidade, saldo):
		try:
			self.cursor.execute("INSERT INTO `extrato` (`escola_id`, `numero_documento`, `data_hora, `tipo_mov`, `entrada_saida`, `produto_id`, `quantidade`, `saldo`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
				[escolaID, numeroDocumento, dataHora, tipo, eS, produtoID, quantidade, saldo])
			self.conexao.commit()
			return True

		except:
			return False