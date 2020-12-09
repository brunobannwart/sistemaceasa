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

import Backend from './services/backend';

import Alterar from './pages/alterar';
import Historico from './pages/historico';
import Login from './pages/login';
import Perfil from './pages/perfil';
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

	async function tratarLogin(cpf: string, senha: string) {
		await Backend.post('/login', { cpf: cpf, senha: senha })
			.then(resposta => {
				setAutenticar(true);
			})
			.catch(erro => {
				setAutenticar(false);
			});
	}

	function tratarLogout() {
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
		return <Login efetuarLogin={(cpf, senha) => tratarLogin(cpf, senha)} />;
	}
}

export default App;