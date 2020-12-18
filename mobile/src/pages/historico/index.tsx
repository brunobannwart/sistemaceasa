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
    IonButtons,
    IonBackButton,
    IonRefresher,
    IonRefresherContent,
} from '@ionic/react';
import { RefresherEventDetail } from '@ionic/core';
import { chevronBack } from 'ionicons/icons';

import Alerta from '../../utils/alert';
import Backend from '../../services/backend';
import Formatar from '../../utils/format';

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

    async function recarregarHistorico(evento: CustomEvent<RefresherEventDetail>) {
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

        evento.detail.complete();
    }

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
                    <IonButtons slot='start'>
                        <IonBackButton
                            defaultHref='/perfil'
                            icon={chevronBack}
                            style={{
                                marginRight: '-3em'
                            }}
                        />
                    </IonButtons>
                    <IonTitle>Histórico</IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent className='ion-padding'>
                <IonRefresher
                    slot='fixed'
                    onIonRefresh={
                        (evento: CustomEvent<RefresherEventDetail>) => {
                            recarregarHistorico(evento);
                        }
                    }
                >
                    <IonRefresherContent />
                </IonRefresher>
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
                                    <IonLabel>{Formatar(data_hora)}</IonLabel>
                                    <IonLabel>{produto}</IonLabel>
                                    <IonLabel>{quantidade}</IonLabel>
                                </IonItem>
                            )
                        })}
                    </IonList> :
                    <IonList>
                        {requisições.map(requisição => {
                            const { escola, numero_documento, tipo, data_hora, produto, quantidade } = requisição;

                            return (
                                <IonItem>
                                    <IonLabel>{escola}</IonLabel>
                                    <IonLabel>{numero_documento}</IonLabel>
                                    <IonLabel>{Formatar(data_hora)}</IonLabel>
                                    <IonLabel>{tipo}</IonLabel>
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