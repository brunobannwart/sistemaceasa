from django import forms

# Create your form here.
class ProdutoForm(forms.Form):
	descricao	=	forms.CharField(label='Descrição', max_length=255, widget=forms.Textarea)

	def clean_form(self):
		descricao 	=	self.cleaned_data.get('descricao')

		return {
			'descricao': descricao,
		}