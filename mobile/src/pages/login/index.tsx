import React, { useState } from 'react';
import {
	IonApp,
	IonHeader,
	IonToolbar,
	IonTitle,
	IonContent,
	IonLabel,
	IonInput,
	IonButton,
	IonGrid,
	IonRow,
	IonCol,
} from '@ionic/react';
import Logo from '../../assets/logo.png';
import './login.css';

interface Props {
	efetuarLogin: ((evento: React.FormEvent, cpf: string, senha: string) => void),
}

const Login: React.FC<Props> = ({
	efetuarLogin
}) => {
	const [cpf, setCPF] = useState('');
	const [senha, setSenha] = useState('');

	function mascaraCampo(valor: string, mascara: string) {
		let formatado, digitos, posição, novoCampo, tamanhoMascara, existeMascara, expressaoRegular;

		expressaoRegular = /\-|\.|\/|\(|\)| /g;
		posição = 0;
		novoCampo = '';

		digitos = valor.toString().replace(expressaoRegular, '');
		tamanhoMascara = digitos.length;

		for (let i = 0; i < tamanhoMascara; i += 1) {
			existeMascara = ((mascara.charAt(i) === '-') || (mascara.charAt(i) === '.') || (mascara.charAt(i) === '/'))
			existeMascara = existeMascara || ((mascara.charAt(i) === '(') || (mascara.charAt(i) === ')') || (mascara.charAt(i) === ' '))

			if (existeMascara) {
				novoCampo += mascara.charAt(i);
				tamanhoMascara++;
			} else {
				novoCampo += digitos.charAt(posição);
				posição++;
			}
		}

		formatado = novoCampo;
		return formatado;
	}

	return (
		<IonApp>
			<IonHeader>
				<IonToolbar
					color='dark'
					className='ion-text-center ion-padding-top'
				>
					<IonTitle>Login</IonTitle>
				</IonToolbar>
			</IonHeader>
			<IonContent className='ion-padding'>
				<header>
					<h1>Bem-vindo</h1>
					<img src={Logo} alt='CEASA' />
				</header>

				<form
					className='login'
					onSubmit={(evento: React.FormEvent) => efetuarLogin(evento, cpf, senha)}
					autoComplete='false'
				>
					<IonGrid>
						<IonRow>
							<IonCol>
								<IonLabel>CPF</IonLabel>
								<IonInput
									type='text'
									placeholder='Informe o seu CPF'
									value={cpf}
									maxlength={14}
									pattern='[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2}'
									onIonChange={e => setCPF(mascaraCampo(e.detail.value!, '000.000.000-00'))}
								/>
							</IonCol>
						</IonRow>
						<IonRow>
							<IonCol>
								<IonLabel>Senha</IonLabel>
								<IonInput
									type='password'
									placeholder='Informe a sua senha'
									value={senha}
									maxlength={50}
									onIonChange={e => setSenha(e.detail.value!)}
								/>
							</IonCol>
						</IonRow>
						<IonRow>
							<IonButton
								type='submit'
								color='success'
								expand='block'
								shape='round'
							>
								Acessar
							</IonButton>
						</IonRow>
					</IonGrid>
					<p>Não compartilhe seus dados com ninguém</p>
				</form>
			</IonContent>
		</IonApp>
	)
}

export default Login;