from django import forms

# Create your form here.
class ProdutoForm(forms.Form):
	codigo		=	forms.CharField(label='Código', max_length=50)
	descricao	=	forms.CharField(label='Descrição', max_length=255, widget=forms.Textarea)

	def clean_form(self):
		codigo		=	self.cleaned_data.get('codigo')
		descricao 	=	self.cleaned_data.get('descricao')

		return {
			'codigo': codigo,
			'descricao': descricao,
		}