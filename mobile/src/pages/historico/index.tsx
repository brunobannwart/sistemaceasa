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
    IonCard,
    IonCardHeader,
    IonCardTitle,
    IonCardSubtitle,
    IonCardContent,
} from '@ionic/react';
import { RefresherEventDetail } from '@ionic/core';
import { chevronBack } from 'ionicons/icons';

import Alerta from '../../utils/alert';
import Backend from '../../services/backend';
import Formatar from '../../utils/format';
import { obterItem } from '../../utils/storage';

import './historico.css';

const Historico: React.FC = () => {
    const [opção, setOpção] = useState('romaneio');
    const [requisições, setRequisições] = useState([]);
    const [romaneios, setRomaneios] = useState([]);
    var controle;

    useEffect(() => {
        async function carregarHistorico() {
            const token = await obterItem('token');
            const codigoUsuario = await obterItem('usuario');

            await Backend.get(`/historico/${codigoUsuario}`, {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            })
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
        const token = await obterItem('token');
        const codigoUsuario = await obterItem('usuario');

        await Backend.get(`/historico/${codigoUsuario}`, {
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
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
                    mode='md'
                >
                    <IonSegmentButton value='romaneio'>
                        <IonLabel>Romaneio</IonLabel>
                    </IonSegmentButton>
                    <IonSegmentButton value='requisição'>
                        <IonLabel>Requisição</IonLabel>
                    </IonSegmentButton>
                </IonSegment>

                {controle ?
                    <IonList className='historico'>
                        {romaneios.map(romaneio => {
                            const { id, escola, numero_romaneio, sequencia, data_hora, produto, quantidade } = romaneio;

                            return (
                                <IonItem key={id}>
                                    <IonCard>
                                        <IonCardHeader>
                                            <IonCardTitle>Documento: {numero_romaneio}</IonCardTitle>
                                            <IonCardSubtitle>Nº Sequencia: {sequencia}</IonCardSubtitle>
                                            <IonCardSubtitle>Data: {Formatar(data_hora)}</IonCardSubtitle>
                                        </IonCardHeader>
                                        <IonCardContent>
                                            <IonLabel>{escola}</IonLabel>
                                            <IonLabel>Produto: {produto}</IonLabel>
                                            <IonLabel>Quantidade: {quantidade}</IonLabel>
                                        </IonCardContent>
                                    </IonCard>
                                </IonItem>
                            )
                        })}
                    </IonList> :
                    <IonList className='historico'>
                        {requisições.map(requisição => {
                            const { id, escola, numero_documento, tipo, data_hora, produto, quantidade } = requisição;

                            return (
                                <IonItem key={id}>
                                    <IonCard>
                                        <IonCardHeader>
                                            <IonCardTitle>Documento: {numero_documento}</IonCardTitle>
                                            <IonCardSubtitle>Tipo: {tipo}</IonCardSubtitle>
                                            <IonCardSubtitle>Data: {Formatar(data_hora)}</IonCardSubtitle>
                                        </IonCardHeader>
                                        <IonCardContent>
                                            <IonLabel>{escola}</IonLabel>
                                            <IonLabel>Produto: {produto}</IonLabel>
                                            <IonLabel>Quantidade: {quantidade}</IonLabel>
                                        </IonCardContent>
                                    </IonCard>
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