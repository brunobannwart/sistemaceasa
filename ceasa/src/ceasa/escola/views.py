from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from .models import Escola
from .forms import EscolaForm

# Create your views here.
@login_required(login_url='login')
def schoollist_view(request):
	escolas = Escola.objects.all()

	contexto = {
		'escolas': escolas
	}

	return render(request, 'school/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def schoolcreate_view(request):
	editar = False

	if request.method == 'POST':
		formulario = EscolaForm(request.POST)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				nova_escola = Escola.objects.create(nome=campos['nome'], rua=campos['rua'], 
					numero=campos['numero'], bairro=campos['bairro'], cidade=campos['cidade'], 
					estado=campos['estado'], cep=campos['cep'], diretor=campos['diretor'])
				nova_escola.save()

			finally:
				return redirect('schoollist')
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		formulario = {
			'nome': '',
			'rua': '',
			'numero': '',
			'bairro': '',
			'cidade': '',
			'bairro': '',
			'cidade': '',
			'estado': '',
			'cep': '',
			'diretor': '',
		}

		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar
	}

	contexto.update(csrf(request))
	return render(request, 'school/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def schooledit_view(request, id):
	if id == 0:
		return redirect('schoollist')

	editar = True

	if request.method == 'POST':
		formulario = EscolaForm(request.POST)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				editar_escola = Escola.objects.get(id=id)
				editar_escola.nome = campos['nome']
				editar_escola.rua = campos['rua']
				editar_escola.numero = campos['numero']
				editar_escola.cidade = campos['cidade']
				editar_escola.bairro = campos['bairro']
				editar_escola.estado = campos['estado']
				editar_escola.cep = campos['cep']
				editar_escola.diretor = campos['diretor']
				editar_escola.save()
			
			finally:
				return redirect('schoollist')
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		try:
			formulario = Escola.objects.get(id=id)
			erro = None
		except:
			return redirect('schoollist')

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar
	}

	contexto.update(csrf(request))
	return render(request, 'school/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def schooldelete_view(request, id):
	if id == 0:
		return redirect('schoollist')

	if request.method == 'POST':
		try:
			excluir_escola = Escola.objects.get(id=id)
			excluir_escola.delete()
		finally:
			return redirect('schoollist')
	else:
		return redirect('schoollist')