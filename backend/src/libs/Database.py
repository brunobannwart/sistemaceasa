import mysql.connector as mysql

class Database:
	def __init__(self):
		self.connection = mysql.connect(host='localhost', user='ceasa', password='projeto$ceasa', database='db_ceasa', auth_plugin='mysql_native_password')
		self.cursor = self.connection.cursor()
		self.__formarTabelas()

	def __formarTabelas(self):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS `romaneio`(`id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT, `codigo_escola` INTEGER, `numero_romaneio` VARCHAR(100), `data_hora` DATETIME, `codigo_produto` VARCHAR(12), `quantidade` INTEGER, `codigo_usuario` INTEGER) ENGINE=InnoDB")
		self.cursor.execute("CREATE TABLE IF NOT EXISTS `requisicao`(`id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT, `codigo_escola` INTEGER, `numero_documento` VARCHAR(100), `data_hora` DATETIME, `tipo` VARCHAR(2), `E/S` VARCHAR(1), `codigo_produto` VARCHAR(12), `quantidade` INTEGER, `codigo_usuario` INTEGER) ENGINE=InnoDB")

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
