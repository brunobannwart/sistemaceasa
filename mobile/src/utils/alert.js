export default function exibirAlerta(mensagem) {
    const alerta = document.createElement('ion-alert');

    alerta.header = 'Aviso';
    alerta.message = mensagem;
    alerta.buttons = ['OK'];

    document.body.appendChild(alerta);
    return alerta.present();
}