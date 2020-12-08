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
    IonButton,
} from '@ionic/react';
import './romaneio.css';

const Romaneio: React.FC = () => {
    const [numeroRomaneio, setNumeroRomaneio] = useState('');
    const [codigoProduto, setCodigoProduto] = useState('');
    const [quantidade, setQuantidade] = useState(null);

    async function tratarSubmit() {

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
                                    onChange={(e: any) => {
                                        setNumeroRomaneio(e.target.value)
                                    }}
                                    value={numeroRomaneio}
                                    placeholder='Informe o número do romaneio'
                                />
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            <IonCol>
                                <IonLabel>Código do produto</IonLabel>
                                <IonInput
                                    type='text'
                                    required
                                    onChange={(e: any) => {
                                        setCodigoProduto(e.target.value)
                                    }}
                                    value={codigoProduto}
                                    placeholder='Informe o código do produto'
                                />
                            </IonCol>
                        </IonRow>
                        <IonRow>
                            <IonCol>
                                <IonLabel>Quantidade</IonLabel>
                                <IonInput
                                    type='number'
                                    required
                                    onChange={(e: any) => {
                                        setQuantidade(e.target.value)
                                    }}
                                    min='0'
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