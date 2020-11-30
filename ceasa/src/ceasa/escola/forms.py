from django import forms

# Create your form here.
class EscolaForm(forms.Form):
	nome 		=	forms.CharField(label='Nome', max_length=100)
	rua 		=	forms.CharField(label='Rua', max_length=100)
	numero 		=	forms.CharField(label='Numero', max_length=10)
	bairro 		=	forms.CharField(label='Bairro', max_length=100)
	cidade 		=	forms.CharField(label='Cidade', max_length=100)
	estado 		=	forms.CharField(label='Estado', max_length=2)
	cep 		=	forms.CharField(label='Cep', max_length=10)
	diretor 	=	forms.CharField(label='Diretor', max_length=100)

	def clean_form(self):
		nome 	=	self.cleaned_data.get('nome')
		rua		= 	self.cleaned_data.get('rua')
		numero	=	self.cleaned_data.get('numero')
		bairro	=	self.cleaned_data.get('bairro')
		cidade 	=	self.cleaned_data.get('cidade')
		estado	= 	self.cleaned_data.get('estado')
		cep		=	self.cleaned_data.get('cep')
		diretor	=	self.cleaned_data.get('diretor')

		return {
			'nome': nome,
			'rua':  rua,
			'numero': numero,
			'bairro': bairro,
			'cidade': cidade,
			'estado': estado,
			'cep': cep,
			'diretor': diretor
		}