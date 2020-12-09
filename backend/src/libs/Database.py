import mysql.connector as mysql

class Database:
	def __init__(self):
		self.connection = mysql.connect(host='localhost', user='ceasa', password='projeto$ceasa', database='db_ceasa', auth_plugin='mysql_native_password')
		self.cursor = self.connection.cursor()
		self.__formarTabelas()

	def __formarTabelas(self):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS `romaneio`(`id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT, `codigo_escola` INTEGER, `numero_romaneio` VARCHAR(100), `codigo_produto` VARCHAR(12), `quantidade` INTEGER, `codigo_usuario` INTEGER) ENGINE=InnoDB")
		self.cursor.execute("CREATE TABLE IF NOT EXISTS `requisicao`(`id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT, `codigo_escola` INTEGER, `numero_requisicao` VARCHAR(100), `codigo_produto` VARCHAR(12), `quantidade` INTEGER, `codigo_usuario` INTEGER) ENGINE=InnoDB")

	def obterUsuario(self, cpf):
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
			 