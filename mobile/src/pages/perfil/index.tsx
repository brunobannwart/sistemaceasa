import React from 'react';
import {
    IonContent,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonList,
    IonItem,
    IonIcon,
    IonLabel,
} from '@ionic/react';
import { useHistory } from 'react-router-dom';
import { construct, logOut, time } from 'ionicons/icons';
import Logo from '../../assets/logo.png';
import './perfil.css';

interface Props {
    efetuarLogout: (() => void),
}

const Perfil: React.FC<Props> = ({
    efetuarLogout,
}) => {
    const navegar = useHistory();

    return (
        <>
            <IonHeader>
                <IonToolbar
                    color='tertiary'
                    className='ion-text-center ion-padding-top'
                >
                    <IonTitle>Perfil</IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent className='ion-padding'>
                <header>
                    <img src={Logo} alt='CEASA' />
                </header>
                <IonList>
                    <IonItem onClick={() => {
                        navegar.push('/alterar');
                    }}>
                        <IonIcon icon={construct} />
                        <IonLabel>Alterar seus dados</IonLabel>
                    </IonItem>
                    <IonItem onClick={() => {
                        navegar.push('/historico');
                    }}>
                        <IonIcon icon={time} />
                        <IonLabel>Histórico</IonLabel>
                    </IonItem>
                    <IonItem onClick={efetuarLogout}>
                        <IonIcon icon={logOut} />
                        <IonLabel>Sair</IonLabel>
                    </IonItem>
                </IonList>
            </IonContent>
        </>
    )
}

export default Perfil;