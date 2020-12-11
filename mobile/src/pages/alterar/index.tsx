import React, { useState } from 'react';
import {
    IonContent,
    IonHeader,
    IonTitle,
    IonInput,
    IonButton,
    IonLabel,
    IonCol,
    IonRow,
    IonGrid,
    IonToolbar
} from '@ionic/react';
import { useHistory } from 'react-router-dom';
import Backend from '../../services/backend';
import './alterar.css';

const Alterar: React.FC = () => {
    const navegar = useHistory();

    const [cpf, setCPF] = useState('');
    const [novaSenha, setNovaSenha] = useState('');
    const [confirmaSenha, setConfirmaSenha] = useState('');

    async function tratarSubmit() {
        const formulario = {
            'cpf': cpf,
            'nova_senha': novaSenha,
            'confirma_senha': confirmaSenha,
        }

        await Backend.post('/alterar', formulario)
            .then(resposta => {

            })
            .catch(erro => {

            });

        navegar.push('/perfil');
    }

    return (
        <>
            <IonHeader>
                <IonToolbar
                    color='tertiary'
                    className='ion-text-center ion-padding-top'
                >
                    <IonTitle>Alterar seus dados</IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent className='ion-padding'>
                <form className='alterar' onSubmit={() => tratarSubmit()} autoComplete='off'>
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
                                    required
                                    onIonChange={e => setCPF(e.detail.value!)}
                                />
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            <IonCol>
                                <IonLabel>Nova senha</IonLabel>
                                <IonInput
                                    type='password'
                                    placeholder='Informe a sua nova senha'
                                    value={novaSenha}
                                    maxlength={50}
                                    required
                                    onIonChange={e => setNovaSenha(e.detail.value!)}
                                />
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            <IonCol>
                                <IonLabel>Confirme nova senha</IonLabel>
                                <IonInput
                                    type='password'
                                    placeholder='Informe a confirmação de nova senha'
                                    value={confirmaSenha}
                                    maxlength={50}
                                    required
                                    onIonChange={e => setConfirmaSenha(e.detail.value!)}
                                />
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            <IonButton
                                type='submit'
                                color='success'
                                expand='block'
                            >
                                Salvar
							</IonButton>
                        </IonRow>
                    </IonGrid>
                </form>
            </IonContent>
        </>
    );
}

export default Alterar;