from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from .models import Produto
from .forms import ProdutoForm

# Create your views here.
@login_required(login_url='login')
def productlist_view(request):
	produtos = Produto.objects.all()

	contexto = {
		'produtos': produtos
	}

	return render(request, 'product/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def productcreate_view(request):
	editar = False

	if request.method == 'POST':
		formulario = ProdutoForm(request.POST)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				nova_produto = Produto.objects.create(descricao=campos['descricao'])
				nova_produto.save()

			finally:
				return redirect('productlist')
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		formulario = {
			'descricao': '',
		}

		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar
	}

	contexto.update(csrf(request))
	return render(request, 'product/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def productedit_view(request, id=0):
	if id == 0:
		return redirect('productlist')

	editar = True

	if request.method == 'POST':
		formulario = ProdutoForm(request.POST)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				editar_produto = Produto.objects.get(id=id)
				editar_produto.descricao = campos['descricao']
				editar_produto.save()
			
			finally:
				return redirect('productlist')
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		try:
			formulario = Produto.objects.get(id=id)
			erro = None
		except:
			return redirect('productlist')

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar
	}

	contexto.update(csrf(request))
	return render(request, 'product/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def productdelete_view(request, id):
	if id == 0:
		return redirect('productlist')

	if request.method == 'POST':
		try:
			excluir_produto = Produto.objects.get(id=id)
			excluir_produto.delete()
		finally:
			return redirect('productlist')
	else:
		return redirect('productlist')