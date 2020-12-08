import React, { useState, useEffect } from 'react';
import {
    IonContent,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonList,
    IonItem,
} from '@ionic/react';
import Backend from '../../services/backend';

const Perfil: React.FC = () => {
    const [historicos, setHistoricos] = useState([]);

    useEffect(() => {
        async function carregarHistorico() {
            await Backend.get('/historico')
            .then(resposta => {
                setHistoricos(resposta.data.historicos);
            })
            .catch(erro => {
                setHistoricos([]);
            });
        }

        carregarHistorico();
    }, []);

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
                <IonList>
                    {historicos.map(historico => {
                        return (
                            <IonItem></IonItem>
                        )
                    })}
                </IonList>
            </IonContent>
        </>
    )
}

export default Perfil;