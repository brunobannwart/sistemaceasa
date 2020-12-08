import React from 'react';
import {
    IonContent,
    IonHeader,
    IonToolbar,
    IonTitle,
} from '@ionic/react';

const Requisição: React.FC = () => {

    return (
        <>
            <IonHeader>
                <IonToolbar 
                    color='tertiary'
                    className='ion-text-center ion-padding-top'
                >
                    <IonTitle>Requisição</IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent className='ion-padding'>       
            </IonContent>
        </>
    )
}

export default Requisição;