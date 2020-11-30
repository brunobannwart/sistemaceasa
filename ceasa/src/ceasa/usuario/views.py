from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from escola.models import Escola

from .models import Usuario
from .forms import UsuarioForm, UsuarioEditarForm

# Create your views here.
@login_required(login_url='login')
def userlist_view(request):
	usuarios = Usuario.objects.all()

	contexto = {
		'usuarios': usuarios
	}

	return render(request, 'user/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def usercreate_view(request):
	editar = False
	escolas = Escola.objects.all()

	if request.method == 'POST':
		formulario = UsuarioForm(request.POST)

		if formulario.is_valid():
			campos = formulario.clean_form()

			if Usuario.objects.filter(cpf=campos['cpf']):
				formulario = request.POST
				erro = 'Já existe usuário com esse CPF'

			else:
				try:
					novo_usuario = Usuario.objects.create(nome=campos['nome'], cpf=campos['cpf'], 
						telefone=campos['telefone'], tipo=campos['tipo'], senha_hash=campos['senha'], escola=campos['escola'])
					novo_usuario.save()

				finally:
					return redirect('userlist')
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		formulario = {
			'nome': '',
			'cpf': '',
			'telefone': '',
			'senha'
			'tipo': '',
			'escola': '',
		}

		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar,
		'escolas': escolas,
	}

	contexto.update(csrf(request))
	return render(request, 'user/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def useredit_view(request, id):
	if id == 0:
		return redirect('userlist')

	editar = True
	escolas = Escola.objects.all()

	if request.method == 'POST':
		formulario = UsuarioEditarForm(request.POST)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				editar_usuario = Usuario.objects.get(id=id)
				editar_usuario.nome = campos['nome']
				editar_usuario.cpf = campos['cpf']
				editar_usuario.telefone = campos['telefone']

				if request.POST.get('senha') != '':
					editar_usuario.senha_hash = campos['senha']

				editar_usuario.tipo = campos['tipo']
				editar_usuario.escola = campos['escola']
				editar_usuario.save()
			
			finally:
				return redirect('userlist')
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		try:
			formulario = Usuario.objects.get(id=id)
			erro = None
		except:
			return redirect('userlist')

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar,
		'escolas': escolas,
	}

	contexto.update(csrf(request))
	return render(request, 'user/form.html', contexto)	

@login_required(login_url='login')
@csrf_protect
def userdelete_view(request, id):
	if id == 0:
		return redirect('userlist')

	if request.method == 'POST':
		try:
			excluir_usuario = Usuario.objects.get(id=id)
			excluir_usuario.delete()
		finally:
			return redirect('userlist')
	else:
		return redirect('userlist')