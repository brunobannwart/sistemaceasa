import React, { useState, useEffect } from 'react';
import {
    IonContent,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonSegment,
    IonSegmentButton,
    IonList,
    IonItem,
    IonLabel,
} from '@ionic/react';
import Alerta from '../../utils/alert';
import Backend from '../../services/backend';

const Historico: React.FC = () => {
    const [opção, setOpção] = useState('romaneio');
    const [requisições, setRequisições] = useState([]);
    const [romaneios, setRomaneios] = useState([]);
    var controle;

    useEffect(() => {
        async function carregarHistorico() {
            await Backend.get('/historico')
                .then(resposta => {
                    const { data } = resposta;
                    setRequisições(data.requisições);
                    setRomaneios(data.romaneios);
                })
                .catch(erro => {
                    Alerta('Não foi possível recuperar o histórico de romaneios e requisições');
                    setRequisições([]);
                    setRomaneios([]);
                });
        }

        carregarHistorico();
    }, []);

    if (opção === 'romaneio') {
        controle = true;
    } else {
        controle = false;
    }

    return (
        <>
            <IonHeader>
                <IonToolbar
                    color='tertiary'
                    className='ion-text-center ion-padding-top'
                >
                    <IonTitle>Histórico</IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent className='ion-padding'>
                <IonSegment
                    value={opção}
                    onIonChange={
                        (e: CustomEvent) => setOpção(e.detail.value!)
                    }
                >
                    <IonSegmentButton value='romaneio'>
                        <IonLabel>Romaneio</IonLabel>
                    </IonSegmentButton>
                    <IonSegmentButton value='requisição'>
                        <IonLabel>Requisição</IonLabel>
                    </IonSegmentButton>
                </IonSegment>

                {controle ?
                    <IonList>
                        {romaneios.map(romaneio => {
                            const { escola, numero_romaneio, data_hora, produto, quantidade } = romaneio;

                            return (
                                <IonItem>
                                    <IonLabel>{escola}</IonLabel>
                                    <IonLabel>{numero_romaneio}</IonLabel>
                                    <IonLabel>{produto}</IonLabel>
                                    <IonLabel>{quantidade}</IonLabel>
                                </IonItem>
                            )
                        })}
                    </IonList> :
                    <IonList>
                        {requisições.map(requisição => {
                            const { escola, numero_documento, data_hora, produto, quantidade } = requisição;

                            return (
                                <IonItem>
                                    <IonLabel>{escola}</IonLabel>
                                    <IonLabel>{numero_documento}</IonLabel>
                                    <IonLabel>{produto}</IonLabel>
                                    <IonLabel>{quantidade}</IonLabel>
                                </IonItem>
                            )
                        })}
                    </IonList>
                }
            </IonContent>
        </>
    )
}

export default Historico;