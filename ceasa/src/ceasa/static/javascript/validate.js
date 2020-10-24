async function validarCEP(cep_entrada) {
	let cep;
	const exp = /\-|\.|\/|\(|\)| /g

	const rua = document.getElementById('rua');
	const cidade = document.getElementById('cidade');
	const bairro = document.getElementById('bairro');
	const estado = document.getElementById('estado');
	const cep_valido = document.getElementById('cep_valido');

	const parametros = {
		method: 'GET',
		mode: 'cors',
		cache: 'default'
	}

	cep = cep_entrada.value.replace(exp, '');

	if (cep.length == 8) {
		await fetch(`https://viacep.com.br/ws/${cep}/json/`, parametros)
				.then(response => {
			 		response.json().then(data => {
			 			if (data.erro != true) {
			 				rua.value = data.logradouro;
				 			bairro.value = data.bairro;
				 			cidade.value = data.localidade;
				 			estado.value = data.uf.toUpperCase();
				 			cep_valido.value = '1';
						} 
						else {
			 				cep_valido.value = '0';
						}
					});
				})
				.catch(error => {
					cep_valido.value = '0';
				});
	}
}

function validarEstado(estado_entrada) {
	const lista_estados = [
		'AC', 'AL', 'AP', 'AM', 
		'BA', 'CE', 'ES', 'GO', 
		'MA', 'MT', 'MS', 'MG', 
		'PA', 'PB', 'PI', 'RJ', 
		'RN', 'RS', 'RO', 'RR', 
		'SC', 'SP', 'SE', 'TO', 
		'DF'
	];

	if (estado_entrada.length == 2) {
		const estado_valido = document.getElementById('estado_valido');
		estado_valido.value = '0';

		for (let i = 0; i < lista_estados.length; i += 1) {
			if (estado_entrada == lista_estados[i]) {
				estado_valido.value = '1';
			}
		}
	}
}

function validarCPF(cpf_entrada) {
	let cpf, cpf_valido, numeros, digitos, soma, i, resultado, iguais, controle;
	const exp = /\-|\.|\/|\(|\)| /g

	const bloco = document.getElementById('bloco_cpf');
	const titulo = document.getElementById('titulo_cpf');
	const mensagem = document.getElementById('mensagem_cpf');

	bloco.style.display = 'none';
	titulo.style.display = 'none';
	mensagem.style.display = 'none';

	cpf = cpf_entrada.value.replace(exp, '');
	cpf_valido = document.getElementById('cpf_valido');

	if (cpf.length == 11) {
		controle = 0;
		iguais = 1;

		for (i = 0; i < cpf.length - 1; i++) {
			if (cpf.charAt(i) != cpf.charAt(i + 1)) {
				iguais = 0;
				break;
			}
		}

		if (!iguais) {
			numeros = cpf.substring(0, 9);
			digitos = cpf.substring(9);
			soma = 0;

			for (i = 10; i > 1; i--) {
				soma += numeros.charAt(10 - i) * i;
			}

			resultado = (soma * 10) % 11;

			if (resultado != digitos.charAt(0)) {
				controle = 0;

			} else {
				numeros = cpf.substring(0, 10);
				soma = 0;

				for (i = 11; i > 1; i--) {
					soma += numeros.charAt(11 - i) * i;
				}

				resultado = (soma * 10) % 11;

				if (resultado != digitos.charAt(1)) {
					controle = 0;
				} else {
					controle = 1;
				}
			}
		} else {
			controle = 0;
		}

		if (!controle) {
			bloco.style.display = 'block';
			titulo.style.display = 'block';
			mensagem.style.display = 'block';
			titulo.innerHTML = 'Aviso';
			mensagem.innerHTML = 'Informe um CPF válido';
			cpf_valido.value = '0';
		} else {
			cpf_valido.value = '1';
		}
	}
}