from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from escola.models import Escola
from estoque.models import Estoque
from extrato.models import Extrato
from produto.models import Produto

# Create your views here.
@login_required(login_url='login')
@csrf_protect
def reportextractschool_view(request):
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
	return render(request, 'report/extractschool.html', contexto)

@login_required(login_url='login')
@csrf_protect
def reportmissingstock_view(request):
	if request.method == 'POST':
		pesquisa = request.POST.get('pesquisa')

		try:
			escola = Escola.objects.get(nome=pesquisa)

		except:
			escola = None

		if escola == None:
			estoques = []
			erro = 'Escola informada não existente'

		else:
			estoques = Estoque.objects.filter(escola=escola)
			erro = None

		faltando = []

		for estoque in estoques:
			if estoque.quantidade < estoque.minimo:
				faltando.append(estoque)

	else:
		pesquisa = ''
		faltando = []
		erro = None

	contexto = {
		'pesquisa': pesquisa,
		'estoques': faltando,
		'erro': erro,
	}

	contexto.update(csrf(request))
	return render(request, 'report/missingstock.html', contexto)

@login_required(login_url='login')
@csrf_protect
def reportadjustment_view(request):
	if request.method == 'POST':
		pesquisa = request.POST.get('pesquisa')
		inicio = request.POST.get('inicio')
		termino = request.POST.get('termino')

		try:
			escola = Escola.objects.get(nome=pesquisa)

		except:
			escola = None

		if escola == None:
			extratos = []
			erro = 'Escola informada não existente'

		else:
			extratos = Extrato.objects.filter(escola=escola, data_hora__gte=inicio, data_hora__lte=termino)
			erro = None

		ajustes = []

		for extrato in extratos:
			if extrato.tipo_mov == 'AJ':
				ajustes.append(extrato)

	else:
		pesquisa = ''
		inicio = ''
		termino = ''
		ajustes = []
		erro = None

	contexto = {
		'pesquisa': pesquisa,
		'inicio': inicio,
		'termino': termino,
		'extratos': ajustes,
		'erro': erro,
	}

	contexto.update(csrf(request))
	return render(request, 'report/adjustment.html', contexto)