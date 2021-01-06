from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives

from io import BytesIO
from xhtml2pdf import pisa

import random
import hashlib

def send_mail(assunto, pagina, contexto, lista_destinatarios, 
	origem, falha_silenciosa=True):

	mensagem_folha = render_to_string(pagina, contexto)

	mensagem_texto = striptags(mensagem_folha)

	email = EmailMultiAlternatives(
		subject=assunto, body=mensagem_texto, 
		from_email=origem, to=lista_destinatarios
	)

	email.attach_alternative(mensagem_folha, 'text/html')
	email.send(fail_silently=falha_silenciosa)

def random_password(amostra, tamanho):
	senha = ''.join((random.choice(amostra) for i in range(tamanho)))
	return senha

def hash_password(senha):
	return hashlib.sha256(senha.encode()).hexdigest()

def render_to_pdf(pagina, contexto={}):
	fragmento = get_template(pagina)
	folha = fragmento.render(contexto)
	resultado = BytesIO()

	pdf = pisa.pisaDocument(BytesIO(folha.encode('utf-8')), resultado)

	if not pdf.err:
		return HttpResponse(resultado.getvalue(), content_type='application/pdf')
	
	return None