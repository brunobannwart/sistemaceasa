from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from escola.models import Escola
from produto.models import Produto

from .models import Estoque
from .forms import EstoqueForm

# Create your views here.
@login_required(login_url='login')
def stocklist_view(request):
	estoques = Estoque.objects.all()

	contexto = {
		'estoques': estoques
	}

	return render(request, 'stock/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def stockcreate_view(request):
	editar = False
	escolas = Escola.objects.all()
	produtos = Produto.objects.all()

	if request.method == 'POST':
		formulario = EstoqueForm(request.POST)

		if formulario.is_valid():
			campos = formulario.clean_form()

			if Estoque.objects.filter(escola=campos['escola'], produto=campos['produto']):
				formulario = request.POST
				erro = 'Já existe este produto no estoque desta escola'

			else:
				try:
					novo_estoque = Estoque.objects.create(escola=campos['escola'], produto=campos['produto'], quantidade=campos['quantidade'], minimo=campos['minimo'])
					novo_estoque.save()

				finally:
					return redirect('stocklist')
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		formulario = {
			'escola': '',
			'produto': '',
			'quantidade': '',
			'minimo': '',
		}

		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar,
		'escolas': escolas,
		'produtos': produtos,
	}

	contexto.update(csrf(request))
	return render(request, 'stock/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def stockedit_view(request, id):
	if id == 0:
		return redirect('stocklist')

	editar = True
	escolas = Escola.objects.all()
	produtos = Produto.objects.all()

	if request.method == 'POST':
		formulario = EstoqueForm(request.POST)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				editar_estoque = Estoque.objects.get(id=id)
				editar_estoque.escola = campos['escola']
				editar_estoque.produto = campos['produto']
				editar_estoque.quantidade = campos['quantidade']
				editar_estoque.minimo = campos['minimo']
				editar_estoque.save()

			finally:
				return redirect('stocklist')
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		try:
			formulario = Estoque.objects.get(id=id)
			erro = None
		except:
			return redirect('stocklist')

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar,
		'escolas': escolas,
		'produtos': produtos,
	}

	contexto.update(csrf(request))
	return render(request, 'stock/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def stockdelete_view(request, id):
	if id == 0:
		return redirect('stocklist')

	if request.method == 'POST':
		try:
			excluir_estoque = Estoque.objects.get(id=id)
			excluir_estoque.delete()
		finally:
			return redirect('stocklist')
	else:
		return redirect('stocklist')