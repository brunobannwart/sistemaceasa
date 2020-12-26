import React, { useState } from 'react';
import {
	IonApp,
	IonIcon,
	IonLabel,
	IonTabBar,
	IonTabButton,
} from '@ionic/react';
import { Route, Switch } from 'react-router-dom';
import { IonReactRouter } from '@ionic/react-router';
import { home, list, restaurant } from 'ionicons/icons';

import Alerta from './utils/alert';
import Backend from './services/backend';
import { armazenarItem, liberarArmazenamento } from './utils/storage';

import Alterar from './pages/alterar';
import Historico from './pages/historico';
import Login from './pages/login';
import Perfil from './pages/perfil';
import Redefinir from './pages/redefinir';
import Requisição from './pages/requisicao';
import Romaneio from './pages/romaneio';

import '@ionic/react/css/core.css';

import '@ionic/react/css/normalize.css';
import '@ionic/react/css/structure.css';
import '@ionic/react/css/typography.css';

import '@ionic/react/css/padding.css';
import '@ionic/react/css/float-elements.css';
import '@ionic/react/css/text-alignment.css';
import '@ionic/react/css/text-transformation.css';
import '@ionic/react/css/flex-utils.css';
import '@ionic/react/css/display.css';

import './styles/global.css';
import './styles/variables.css';

const App: React.FC = () => {
	const [autenticado, setAutenticar] = useState(false);

	async function tratarLogin(evento: React.FormEvent, cpf: string, senha: string) {
		evento.preventDefault();

		const formulario = new FormData();

		formulario.append('cpf', cpf);
		formulario.append('senha', senha);

		await Backend.post('/login', formulario)
			.then(async resposta => {
				const { escola_id, id } = resposta.data;

				await armazenarItem('escola', escola_id.toString());
				await armazenarItem('usuario', id.toString());

				setAutenticar(true);
			})
			.catch(erro => {
				Alerta('Não foi possível efetuar o login. Tente novamente');
				setAutenticar(false);
			});
	}

	async function tratarLogout() {
		await liberarArmazenamento();
		setAutenticar(false);
	}

	if (autenticado) {
		return (
			<IonApp>
				<IonReactRouter>
					<Switch>
						<Route path='/' exact component={Romaneio} />
						<Route path='/alterar' component={Alterar} />
						<Route path='/historico' component={Historico} />
						<Route path='/perfil' render={
							() => <Perfil efetuarLogout={tratarLogout} />
						} />
						<Route path='/requisicao' component={Requisição} />
						<Route path='/romaneio' component={Romaneio} />
					</Switch>
					<IonTabBar slot='bottom'>
						<IonTabButton tab='romaneio' href='/romaneio'>
							<IonIcon icon={restaurant} />
							<IonLabel>Romaneio</IonLabel>
						</IonTabButton>
						<IonTabButton tab='requisicao' href='/requisicao'>
							<IonIcon icon={list} />
							<IonLabel>Requisição</IonLabel>
						</IonTabButton>
						<IonTabButton tab='perfil' href='/perfil'>
							<IonIcon icon={home} />
							<IonLabel>Perfil</IonLabel>
						</IonTabButton>
					</IonTabBar>
				</IonReactRouter>
			</IonApp>
		)
	} else {
		return (
			<IonApp>
				<IonReactRouter>
					<Switch>
						<Route path='/' exact render={
							() => <Login
								efetuarLogin={(evento, cpf, senha) => tratarLogin(evento, cpf, senha)}
							/>}
						/>
						<Route path='/redefinir' component={Redefinir} />
					</Switch>
				</IonReactRouter>
			</IonApp>
		)
	}
}

export default App;