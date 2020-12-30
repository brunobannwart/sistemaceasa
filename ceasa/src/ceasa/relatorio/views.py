from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from escola.models import Escola
from extrato.models import Extrato
from produto.models import Produto

# Create your views here.
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

@login_required(login_url='login')
@csrf_protect
def reportinventory_view(request):
	if request.method == 'POST':
		pesquisa = request.POST.get('pesquisa')

		try:
			produto = Produto.objects.get(codigo=pesquisa)

		except:
			produto = None

		if produto == None:
			extratos = []
			erro = 'Produto informado não existente'

		else:
			extratos = Extrato.objects.filter(produto=produto)
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
	return render(request, 'report/listinventory.html', contexto)
