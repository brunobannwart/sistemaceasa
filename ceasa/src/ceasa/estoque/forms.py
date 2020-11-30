from django import forms
from escola.models import Escola
from produto.models import Produto

# Create your form here.
class EstoqueForm(forms.Form):
	escola 		=	forms.ModelChoiceField(label='Escola', widget=forms.Select, queryset=Escola.objects.all())
	produto 	=	forms.ModelChoiceField(label='Produto', widget=forms.Select, queryset=Produto.objects.all())
	quantidade 	=	forms.IntegerField(label='Quantidade')
	minimo		=	forms.IntegerField(label='Estoque mínimo')

	def clean_form(self):
		escola 		=	self.cleaned_data.get('escola')
		produto 	=	self.cleaned_data.get('produto')
		quantidade 	= 	self.cleaned_data.get('quantidade')
		minimo		=	self.cleaned_data.get('minimo')

		return {
			'escola': escola,
			'produto': produto,
			'quantidade': quantidade,
			'minimo': minimo
		}