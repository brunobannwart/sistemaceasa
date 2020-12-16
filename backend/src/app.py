from flask import Flask, json, Response, request
from flask_cors import CORS
from libs.Controller import Controller
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
templates_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__)
CORS(app)

app.config.from_object('config.Config')
app.controller = Controller(templates_dir)

def tratar_sucesso(saida, status=200, mimetype='application/json'):
	return Response(saida, status=status, mimetype=mimetype)

def tratar_erro(saida, status=500, mimetype='application/json'):
	return Response(saida, status=status, mimetype=mimetype)

@app.route('/login', methods=['POST'])
def efetuar_login():
	cpf 		= request.form['cpf']
	senha 		= request.form['senha']

	usuario = app.controller.efetuarLogin(cpf, senha)

	if usuario != None:
		saida = json.dumps({ 'id': usuario['id'], 'cpf': usuario['cpf'], 'escola_id': usuario['escola'] })
		return tratar_sucesso(saida)

	else:
		return tratar_erro('Não foi possível efetuar login')

@app.route('/alterar', methods=['POST'])
def alterar_senha():
	cpf	= request.form['cpf']
	novaSenha = request.form['nova_senha']

	resultado = app.controller.alterarSenha(cpf, novaSenha)

	if resultado:
		saida = json.dumps({ 'mensagem': 'Alterado com sucesso '})
		return tratar_sucesso(saida)
		
	else:
		return tratar_erro('Não foi possível alterar')

@app.route('/redefinir', methods=['POST'])
def redefinir_senha():
	cpf = request.form['cpf']

	resultado = app.controller.redefinirSenha(cpf)

	if resultado:
		saida = json.dumps({ 'mensagem': 'Redefinido com sucesso '})
		return tratar_sucesso(saida)

	else:
		return tratar_erro('Não foi possível redefinir')

@app.route('/historico/<usuarioID>')
def historico(usuarioID=0):
	romaneios, requisições = app.controller.historicoUsuario(usuarioID)

	if len(romaneios) or len(requisições):
		saida = json.dumps({ 'romaneios': romaneios, 'requisições': requisições })
		return tratar_sucesso(saida)
		
	else:
		return tratar_erro('Não foi possível recuperar nenhum histórico')

app.run(host=app.config['FLASK_RUN_HOST'], port=app.config['FLASK_RUN_PORT'])