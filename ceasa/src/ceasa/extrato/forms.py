from django import forms
from escola.models import Escola
from produto.models import Produto

# Create your form here.
class ExtratoForm(forms.Form):
	escola 				=	forms.ModelChoiceField(label='Escola', widget=forms.Select, queryset=Escola.objects.all())
	produto 			=	forms.ModelChoiceField(label='Produto', widget=forms.Select, queryset=Produto.objects.all())
	data_hora			=	forms.DateTimeField(label='Data/hora')
	entrada_saida 		= 	forms.CharField(label='E/S', max_length=1)
	tipo_mov			=	forms.CharField(label='Tipo de movimentação', max_length=2)
	numero_documento	=	forms.CharField(label='Número do documento', max_length=255)
	quantidade 			=	forms.IntegerField(label='Quantidade')
	saldo 				=	forms.IntegerField(label='Saldo')

	def clean_form(self):
		escola 				=	self.cleaned_data.get('escola')
		produto 			=	self.cleaned_data.get('produto')
		quantidade 			= 	self.cleaned_data.get('quantidade')
		saldo				=	self.cleaned_data.get('saldo')
		numero_documento	=	self.cleaned_data.get('numero_documento')
		tipo_mov			=	self.cleaned_data.get('tipo_mov')
		entrada_saida		=	self.cleaned_data.get('entrada_saida')
		data_hora 			=	self.cleaned_data.get('data_hora')

		return {
			'escola': escola,
			'produto': produto,
			'quantidade': quantidade,
			'saldo': saldo,
			'numero_documento': numero_documento,
			'tipo_mov': tipo_mov,
			'entrada_saida': entrada_saida,
			'data_hora': data_hora,
		}