from flask import Flask, json, Response, request
from libs.Controller import Controller
import hashlib

app = Flask(__name__)
app.config.from_object('config.Config')
app.controller = Controller()

def tratar_sucesso(saida, status=200, mimetype='application/json'):
	return Response(output=saida, status=status, mimetype=mimetype)

def tratar_erro(saida, status=500, mimetype='application/json'):
	return Response(output=saida, status=status, mimetype=mimetype)

@app.route('/login', methods=['POST'])
def efetuar_login():
	cpf 		= request.form['cpf']
	senha 		= request.form['senha']
	senha_hash 	= hashlib.sha256(senha.encode()).hexdigest()

	usuario = app.controller.efetuarLogin(cpf, senha_hash)

	if usuario != None:
		saida = json.dumps({ 'id': usuario['id'], 'cpf': usuario['cpf'], 'escola_id': usuario['escola'] })
		return tratar_sucesso(saida)

	else:
		return tratar_erro('Não foi possível efetuar login')

@app.route('/alterar', methods=['POST'])
def alterar_senha():
	cpf	= request.form['cpf']
	nova_senha = request.form['nova_senha']
	senha_hash = hashlib.sha256(nova_senha.encode()).hexdigest()

	resultado = app.controller.alterarSenha(cpf, senha_hash)

	if resultado:
		saida = json.dumps({ 'mensagem': 'Alterado com sucesso '})
		return tratar_sucesso(saida)
		
	else:
		return tratar_erro('Não foi possível alterar')

app.run(host=app.config['FLASK_RUN_HOST'], port=app.config['FLASK_RUN_PORT'])