import React, { useState } from 'react';
import {
	IonApp,
	IonIcon,
	IonLabel,
	IonRouterOutlet,
	IonTabBar,
	IonTabButton,
	IonTabs
} from '@ionic/react';

import { IonReactRouter } from '@ionic/react-router';

import { home } from 'ionicons/icons';

import Backend from './services/backend';
import Login from './pages/login';

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
		await Backend.post('/login', { cpf, senha })
		.then(resposta => {
			console.log(resposta);
			setAutenticar(true);
		})
		.catch(erro => {
			console.log(erro);
		});
	}

	if (autenticado) {
		return (
			<IonApp>
				<IonReactRouter>
					<IonTabs>
						<IonRouterOutlet>
						</IonRouterOutlet>
					</IonTabs>
					<IonTabBar slot='bottom'>
						<IonTabButton tab='perfil' href='/'>
							<IonIcon icon={home} />
							<IonLabel>Perfil</IonLabel>
						</IonTabButton>
					</IonTabBar>
				</IonReactRouter>
			</IonApp>
		)
	} else {
		return <Login />;
	}
}

export default App;