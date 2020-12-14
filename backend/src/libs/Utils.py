from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import hashlib
import random
import smtplib

def criarHashSenha(senha):
	return hashlib.sha256(senha.encode()).hexdigest()

def criarSenhaAleatoria(amostra, tamanho):
	return ''.join((random.choice(amostra) for i in range(tamanho)))

def enviarEmail(assunto, pagina, contexto, origem, destinatario):
	mensagem = MIMEMultipart('alternative')
	mensagem['subject'] = assunto
	mensagem['from'] = origem
	mensagem['to'] = destinatario

	with open(pagina, 'r') as html:
		mensagemHtml = Template(html.read())
		corpoMensagem = mensagemHtml(nome=contexto['nome'], senha=contexto['senha'], ano=datetime.now().year)

	corpo = MIMEText(corpoMensagem, 'html')
	mensagem.attach(corpo)

	with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
		try:
			smtp.ehlo()
			smtp.starttls()
			smtp.login('email@gmail.com', 'senha')
			smtp.send_message(mensagem)
			return True
		except:
			return False
