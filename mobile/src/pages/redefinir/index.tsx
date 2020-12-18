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
    IonButtons,
    IonBackButton,
} from '@ionic/react';
import { useHistory } from 'react-router-dom';
import { chevronBack } from 'ionicons/icons';

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

        const formulario = new FormData();
        formulario.append('cpf', cpf);
        
        await Backend.post('/redefinir', formulario)
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
                    <IonButtons slot='start'>
                        <IonBackButton
                            defaultHref='/'
                            icon={chevronBack}
                            style={{
                                marginRight: '-3em'
                            }}
                        />
                    </IonButtons>
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
                        <p>Um email será enviado com uma nova senha</p>
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
                    </IonGrid>
                </form>
            </IonContent>
        </>
    )
}

export default Redefinir;