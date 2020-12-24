import React, { useState } from 'react';
import {
    IonContent,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonIcon,
    IonInput,
    IonLabel,
    IonRow,
    IonGrid,
    IonCol,
    IonButton,
    IonSelect,
    IonSelectOption,
} from '@ionic/react';
import { useHistory } from 'react-router-dom';

import { BarcodeScanner } from '@ionic-native/barcode-scanner';
import { barcode } from 'ionicons/icons';

import Alerta from '../../utils/alert';
import Backend from '../../services/backend';

import './requisicao.css';

const Requisição: React.FC = () => {
    const navegar = useHistory();

    const [tipo, setTipo] = useState('');
    const [codigoProduto, setCodigoProduto] = useState('');
    const [quantidade, setQuantidade] = useState('');

    async function tratarSubmit(evento: React.FormEvent) {
        evento.preventDefault();

        const formulario = new FormData();

        formulario.append('tipo', tipo);
        formulario.append('data_hora', new Date().toString());
        formulario.append('codigo_produto', codigoProduto);
        formulario.append('quantidade', quantidade);

        await Backend.post('/requisicao', formulario)
            .then(resposta => {
                navegar.push('/perfil');
            })
            .catch(erro => {
                Alerta('Não foi possível registrar requisição');
            });
    }

    async function escanear() {
        await BarcodeScanner.scan()
            .then(resposta => {
                setCodigoProduto(resposta.text);
            })
            .catch(erro => {
                Alerta('Não foi possível escanear código de barra');
            });
    }

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
                <form
                    className='requisicao'
                    onSubmit={(evento: React.FormEvent) => tratarSubmit(evento)}
                    autoComplete='off'
                >
                    <IonGrid>
                        <IonRow>
                            <IonCol>
                                <IonLabel>Tipo</IonLabel>
                                <IonSelect
                                    value={tipo}
                                    onIonChange={
                                        e => setTipo(e.detail.value!)
                                    }
                                    okText='Confirmar'
                                    cancelText='Cancelar'
                                >
                                    <IonSelectOption value='' disabled hidden>
                                        Selecione um tipo
                                    </IonSelectOption>
                                    <IonSelectOption value='RQ'>
                                        Requisição
                                    </IonSelectOption>
                                    <IonSelectOption value='DV'>
                                        Devolução
                                    </IonSelectOption>
                                    <IonSelectOption value='AJ'>
                                        Ajuste
                                    </IonSelectOption>
                                </IonSelect>
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

                                <div className='scanner'>
                                    <p>ou</p>

                                    <IonButton
                                        type='button'
                                        color='medium'
                                        expand='block'
                                        onClick={() => escanear()}
                                    >
                                        <IonIcon slot='start' icon={barcode} />
                                        <IonLabel>Escanear</IonLabel>
                                    </IonButton>
                                </div>
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

export default Requisição;