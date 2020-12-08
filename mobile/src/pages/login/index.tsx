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
				<img src={Logo} alt='CEASA' />

				<form onSubmit={() => { }} autoComplete='false'>
					<IonGrid>
						<IonRow>
							<IonCol>
								<IonLabel>CPF</IonLabel>
								<IonInput
									placeholder='Informe o seu CPF'
									value={cpf}
									maxlength={14}
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
							>
								Acessar
							</IonButton>
						</IonRow>
					</IonGrid>
				</form>
			</IonContent>
		</IonApp>
	)
}

export default Login;