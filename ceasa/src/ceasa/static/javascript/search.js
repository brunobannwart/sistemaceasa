function pesquisarEscola() {
	let entrada, filtro, tabela, linha, coluna, index, texto;

	entrada = document.getElementsByTagName('input')[0];
	filtro = entrada.value.toUpperCase();
	tabela = document.getElementsByTagName('table')[0];
	linha = tabela.getElementsByTagName('tr');

	for (index = 0; index < linha.length; index += 1) {
		coluna = linha[index].getElementsByTagName('td')[0];

		if (coluna) {
			texto = coluna.textContent || coluna.innerText;

			if (texto.toUpperCase().indexOf(filtro) > -1) {
				linha[index].style.display = '';
			} else {
				linha[index].style.display = 'none';
			}
		}
	}
}

function pesquisarProduto() {
	let entrada, filtro, tabela, linha, coluna, index, texto;

	entrada = document.getElementsByTagName('input')[0];
	filtro = entrada.value.toUpperCase();
	tabela = document.getElementsByTagName('table')[0];
	linha = tabela.getElementsByTagName('tr');

	for (index = 0; index < linha.length; index += 1) {
		coluna = linha[index].getElementsByTagName('td')[1];

		if (coluna) {
			texto = coluna.textContent || coluna.innerText;

			if (texto.toUpperCase().indexOf(filtro) > -1) {
				linha[index].style.display = '';
			} else {
				linha[index].style.display = 'none';
			}
		}
	}
}

function pesquisarUsuario() {
	let entrada, filtro, tabela, linha, coluna, index, texto;

	entrada = document.getElementsByTagName('input')[0];
	filtro = entrada.value.toUpperCase();
	tabela = document.getElementsByTagName('table')[0];
	linha = tabela.getElementsByTagName('tr');

	for (index = 0; index < linha.length; index += 1) {
		coluna = linha[index].getElementsByTagName('td')[0];

		if (coluna) {
			texto = coluna.textContent || coluna.innerText;

			if (texto.toUpperCase().indexOf(filtro) > -1) {
				linha[index].style.display = '';
			} else {
				linha[index].style.display = 'none';
			}
		}
	}
}