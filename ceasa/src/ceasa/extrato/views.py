from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from escola.models import Escola
from produto.models import Produto

from .models import Extrato
# from .forms import ExtratoForm

# Create your views here.
@login_required(login_url='login')
def extractlist_view(request):
	extratos = Extrato.objects.all()

	contexto = {
		'extratos': extratos,
	}

	return render(request, 'extract/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def reportstockschool_view(request):
	if request.method == 'POST':
		pesquisa = request.POST.get('pesquisa')

		try:
			escola = Escola.objects.get(nome=pesquisa)

		except:
			escola = None

		if escola == None:
			extratos = []
			erro = 'Escola informada não existente'

		else:
			extratos = Extrato.objects.filter(escola=escola)
			erro = None

	else:
		pesquisa = ''
		extratos = []
		erro = None

	contexto = {
		'pesquisa': pesquisa,
		'extratos': extratos,
		'erro': erro,
	}

	contexto.update(csrf(request))
	return render(request, 'report/liststock.html', contexto)

# @login_required(login_url='login')
# @csrf_protect
# def extractcreate_view(request):
# 	editar = False
# 	escolas = Escola.objects.all()
# 	produtos = Produto.objects.all()

# 	if request.method == 'POST':
# 		formulario = ExtratoForm(request.POST)

# 		if formulario.is_valid():
# 			campos = formulario.clean_form()

# 			try:
# 				novo_extrato = Extrato.objects.create(escola=campos['escola'], produto=campos['produto'], 
# 								quantidade=campos['quantidade'], saldo=campos['saldo'], numero_documento=campos['numero_documento'],
# 								entrada_saida=campos['entrada_saida'], tipo_mov=campos['tipo_mov'], data_hora=campos['data_hora'])
# 				novo_extrato.save()

# 			finally:
# 				return redirect('extractlist')
# 		else:
# 			formulario = request.POST
# 			erro = 'Alguns campos não foram preenchidos corretamente'
# 	else:
# 		formulario = {
# 			'escola': '',
# 			'produto': '',
# 			'quantidade': '',
# 			'saldo': '',
# 			'numero_documento': '',
# 			'data_hora': '',
# 			'tipo_mov': '',
# 			'entrada_saida': '',
# 		}

# 		erro = None

# 	contexto = {
# 		'form': formulario,
# 		'erro': erro,
# 		'editar': editar,
# 		'escolas': escolas,
# 		'produtos': produtos,
# 	}

# 	contexto.update(csrf(request))
# 	return render(request, 'extract/form.html', contexto)


# @login_required(login_url='login')
# @csrf_protect
# def extractedit_view(request, id):
# 	if id == 0:
# 		return redirect('extractlist')

# 	editar = True
# 	escolas = Escola.objects.all()
# 	produtos = Produto.objects.all()

# 	if request.method == 'POST':
# 		formulario = ExtratoForm(request.POST)

# 		if formulario.is_valid():
# 			campos = formulario.clean_form()

# 			try:
# 				editar_extrato = Extrato.objects.get(id=id)
# 				editar_extrato.escola = campos['escola']
# 				editar_extrato.produto = campos['produto']
# 				editar_extrato.data_hora = campos['data_hora']
# 				editar_extrato.numero_documento = campos['numero_documento']
# 				editar_extrato.entrada_saida = campos['entrada_saida']
# 				editar_extrato.tipo_mov = campos['tipo_mov']
# 				editar_extrato.quantidade = campos['quantidade']
# 				editar_extrato.saldo = campos['saldo']
# 				editar_extrato.save()

# 			finally:
# 				return redirect('extractlist')
# 		else:
# 			formulario = request.POST
# 			erro = 'Alguns campos não foram preenchidos corretamente'
# 	else:
# 		try:
# 			formulario = Extrato.objects.get(id=id)
# 			erro = None
# 		except:
# 			return redirect('extractlist')

# 	contexto = {
# 		'form': formulario,
# 		'erro': erro,
# 		'editar': editar,
# 		'escolas': escolas,
# 		'produtos': produtos,
# 	}

# 	contexto.update(csrf(request))
# 	return render(request, 'extract/form.html', contexto)


# @login_required(login_url='login')
# @csrf_protect
# def extractdelete_view(request, id):
# 	if id == 0:
# 		return redirect('extractlist')

# 	if request.method == 'POST':
# 		try:
# 			excluir_extrato = Extrato.objects.get(id=id)
# 			excluir_extrato.delete()
# 		finally:
# 			return redirect('extractlist')
# 	else:
# 		return redirect('extractlist')
