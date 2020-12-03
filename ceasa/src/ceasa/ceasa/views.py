from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .backend import LoginBackend
from .forms import LoginForm, TrocarSenhaForm, RedefinirForm
from .utils import send_mail, random_password, hash_password

from usuario.models import Usuario

@csrf_protect
def login_view(request):
	if request.method == 'POST':
		try:
			formulario = LoginForm(request.POST)

			if formulario.is_valid():
				campos = formulario.clean_form()
				cpf = campos['cpf']
				senha = campos['senha']

				usuario = LoginBackend.authenticate(request, cpf, senha)

				if usuario != None and usuario != False:
					usuario.is_authenticated = True
					usuario.save()
					login(request, usuario, backend='ceasa.backend.LoginBackend')
					return redirect('schoollist')
				else:
					if usuario == False:
						formulario = request.POST
						erro = 'Senha não confere'
					else:
						formulario = request.POST
						erro = 'CPF não cadastrado'
			else:
				formulario = request.POST
				erro = 'Preencher campos corretamente'
		except:
			formulario = request.POST
			erro = 'Não foi possível acessar o sistema. Tente novamente'
	else:
		formulario = {
			'cpf': '',
			'senha': '',
		}
		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
	}

	contexto.update(csrf(request))
	return render(request, 'login/index.html', contexto)

def forgot_view(request):
	return render(request, 'login/forgot.html', {})

@csrf_protect
def reset_view(request):
	if request.method == 'POST':
		formulario = RedefinirForm(request.POST)

		if formulario.is_valid():
			campos	= 	formulario.clean_form()

			try:
				usuario = Usuario.objects.get(cpf=campos['cpf'])
				
				contexto = {
					'nome':	usuario.nome.upper(),
					'senha': random_password('0123456789', 6)
				}

				send_mail('Esqueci minha senha', 'option/email.html', 
					contexto, [usuario.email], settings.DEFAULT_FROM_EMAIL
				)

				usuario.senha_hash = hash_password(contexto['senha'])
				usuario.save()

				return redirect('login')

			except Exception as e:
				formulario = request.POST
				erro = 'Algum erro ocorreu'

		else:
			formulario = request.POST
			erro = 'Preencher campos corretamente'

	else:
		formulario = {
			'cpf': '',
		}

		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
	}

	contexto.update(csrf(request))
	return render(request, 'login/reset.html', contexto)

@login_required(login_url='login')
@csrf_protect
def changepassword_view(request):
	if request.method == 'POST':
		formulario = TrocarSenhaForm(request.POST)

		if formulario.is_valid():
			campos 			= formulario.clean_form()
			cpf 			= campos['cpf']
			nova_senha 		= campos['nova_senha']
			confirma_senha 	= campos['confirma_senha']

			try:
				usuario = Usuario.objects.get(cpf=campos['cpf'])

				if campos['nova_senha'] == campos['confirma_senha']:
					usuario.senha_hash = campos['nova_senha']
					usuario.save()
					return redirect('schoollist')

				else:
					formulario = request.POST
					erro = 'Senhas não são idênticas'

			except:
				formulario = request.POST
				erro = 'CPF não cadastrado'
		else:
			formulario = request.POST
			erro = 'Preencher campos corretamente'
	else:
		formulario = {
			'cpf': '',
			'nova_senha': '',
			'confirma_senha': ''
		}

		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
	}

	contexto.update(csrf(request))
	return render(request, 'option/changepassword.html', contexto)

def logout_view(request):
	try:
		cpf = request.user.cpf
		logout(request)
		usuario = Usuario.objects.get(cpf=cpf)
		usuario.is_authenticated = False
		usuario.save()
	finally:
		return redirect('login')