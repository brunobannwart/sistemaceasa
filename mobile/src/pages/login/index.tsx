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

const Login: React.FC = () => {
	const [cpf, setCPF] = useState('');
	const [senha, setSenha] = useState('');

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

				<form onSubmit={() => {}} autoComplete='false'>
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
									onChange={
										(e: any) => setCPF(e.target.value)
									}
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
									onChange={
										(e: any) => setSenha(e.target.value)
									}
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
				</form>
				<p>Não compartilhe seus dados com ninguém</p>
			</IonContent>
		</IonApp>
	)
}

export default Login;