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
    IonIcon,
    IonButton,
} from '@ionic/react';
import { useHistory } from 'react-router-dom';

import { BarcodeScanner } from '@ionic-native/barcode-scanner';
import { barcode } from 'ionicons/icons';

import Alerta from '../../utils/alert';
import Backend from '../../services/backend';
import { obterItem } from '../../utils/storage';

import './romaneio.css';

const Romaneio: React.FC = () => {
    const navegar = useHistory();

    const [numeroRomaneio, setNumeroRomaneio] = useState('');
    const [codigoProduto, setCodigoProduto] = useState('');
    const [quantidade, setQuantidade] = useState('');

    async function tratarSubmit(evento: React.FormEvent) {
        evento.preventDefault();
        const codigoEscola = await obterItem('escola');
        const token = await obterItem('token');
        const codigoUsuario = await obterItem('usuario');

        const formulario = new FormData();

        formulario.append('numero_romaneio', numeroRomaneio);
        formulario.append('data_hora', new Date().toString());
        formulario.append('codigo_escola', codigoEscola ? codigoEscola : '0');
        formulario.append('codigo_produto', codigoProduto);
        formulario.append('quantidade', quantidade);
        formulario.append('codigo_usuario', codigoUsuario ? codigoUsuario : '0');

        await Backend.post('/romaneio', formulario, {
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
            .then(resposta => {
                navegar.push('/perfil');
            })
            .catch(erro => {
                Alerta('Não foi possível registrar romaneio');
            });
    }

    async function escanear() {
        await BarcodeScanner.scan()
            .then(resposta => {
                setCodigoProduto(resposta.text);
            })
            .catch(erro => {
                Alerta('Não foi possível ler código de barra');
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
                <form
                    className='romaneio'
                    onSubmit={(evento: React.FormEvent) => tratarSubmit(evento)}
                    autoComplete='off'
                >
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
                                    maxlength={255}
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
                                    maxlength={50}
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
                                        <IonLabel>Leitor</IonLabel>
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

export default Romaneio;