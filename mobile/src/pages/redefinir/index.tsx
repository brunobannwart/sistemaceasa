import React, { useState } from 'react';
import {
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
import { useHistory } from 'react-router-dom';

import Alerta from '../../utils/alert';
import Backend from '../../services/backend';
import Mascara from '../../utils/mask';

import Logo from '../../assets/logo.png';
import './redefinir.css';

const Redefinir: React.FC = () => {
    const navegar = useHistory();
    const [cpf, setCPF] = useState('');

    async function tratarSubmit(evento: React.FormEvent, cpf: string) {
        evento.preventDefault();

        await Backend.post('/redefinir', { cpf: cpf })
            .then(resposta => {
                navegar.push('/');
            })
            .catch(erro => {
                Alerta('Não foi possível redefinir sua senha');
            });
    }

    return (
        <>
            <IonHeader>
                <IonToolbar
                    color='dark'
                    className='ion-text-center ion-padding-top'
                >
                    <IonTitle>Redefinir senha</IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent className='ion-padding'>
                <header>
                    <img src={Logo} alt='CEASA' />
                </header>

                <form
                    className='redefinir'
                    onSubmit={(evento: React.FormEvent) => tratarSubmit(evento, cpf)}
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
                                    onIonChange={e => setCPF(Mascara(e.detail.value!, '000.000.000-00'))}
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
                                Confirmar
							</IonButton>
                        </IonRow>
                        <IonRow>
                            <IonButton
                                type='button'
                                color='danger'
                                expand='block'
                                shape='round'
                                onClick={() => navegar.push('/')}
                            >
                                Voltar para login
                            </IonButton>
                        </IonRow>
                    </IonGrid>
                </form>
            </IonContent>
        </>
    )
}

export default Redefinir;