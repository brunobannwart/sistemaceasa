import React, { useState } from 'react';
import {
    IonContent,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonGrid,
    IonRow,
    IonCol,
    IonLabel,
    IonInput,
    IonDatetime,
    IonButton,
} from '@ionic/react';
import Backend from '../../services/backend';
import './romaneio.css';

const Romaneio: React.FC = () => {
    const [numeroRomaneio, setNumeroRomaneio] = useState('');
    const [dataHora] = useState(new Date().toString());
    const [codigoProduto, setCodigoProduto] = useState('');
    const [quantidade, setQuantidade] = useState('');

    async function tratarSubmit() {
        const formulario = {
            'numero_romaneio': numeroRomaneio,
            'data_hora': dataHora,
            'codigo_produto': codigoProduto,
            'quantidade': parseInt(quantidade, 10),
        }

        await Backend.post('/romaneio', formulario)
            .then(resposta => {

            })
            .catch(erro => {

            });
    }

    return (
        <>
            <IonHeader>
                <IonToolbar
                    color='tertiary'
                    className='ion-text-center ion-padding-top'
                >
                    <IonTitle>Romaneio</IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent className='ion-padding'>
                <form className='romaneio' onSubmit={() => tratarSubmit()} autoComplete='off'>
                    <IonGrid>
                        <IonRow>
                            <IonCol>
                                <IonLabel>Número do romaneio</IonLabel>
                                <IonInput
                                    type='text'
                                    required
                                    onIonChange={e => setNumeroRomaneio(e.detail.value!)}
                                    value={numeroRomaneio}
                                    placeholder='Informe o número do romaneio'
                                />
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            <IonCol>
                                <IonLabel>Data e hora</IonLabel>
                                <IonDatetime
                                    value={dataHora}
                                    displayFormat='DD/MM/YYYY HH:mm'
                                    min='2020-01-01'
                                    mode='ios'
                                    cancelText='Cancelar'
                                    doneText='OK'
                                    readonly
                                />
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            <IonCol>
                                <IonLabel>Código do produto</IonLabel>
                                <IonInput
                                    type='text'
                                    required
                                    onIonChange={e => setCodigoProduto(e.detail.value!)}
                                    value={codigoProduto}
                                    placeholder='Informe o código do produto'
                                />
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            <IonCol>
                                <IonLabel>Quantidade</IonLabel>
                                <IonInput
                                    type='text'
                                    required
                                    onIonChange={e => setQuantidade(e.detail.value!)}
                                    pattern='[0-9]*'
                                    value={quantidade}
                                    placeholder='Informe a quantidade do produto'
                                />
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            <IonButton
                                type='submit'
                                color='success'
                            >
                                Salvar
                            </IonButton>
                        </IonRow>
                    </IonGrid>
                </form>
            </IonContent>
        </>
    )
}

export default Romaneio;