from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives

import random
import hashlib

def send_mail(assunto, pagina, contexto, lista_destinatarios, 
	origem, falha_silenciosa=True):

	mensagem_html = render_to_string(pagina, contexto)

	mensagem_texto = striptags(mensagem_html)

	email = EmailMultiAlternatives(
		subject=assunto, body=mensagem_texto, 
		from_email=origem, to=lista_destinatarios
	)

	email.attach_alternative(mensagem_html, 'text/html')
	email.send(fail_silently=falha_silenciosa)

def random_password(amostra, tamanho):
	senha = ''.join((random.choice(amostra) for i in range(tamanho)))
	return senha

def hash_password(senha):
	return hashlib.sha256(senha.encode()).hexdigest()