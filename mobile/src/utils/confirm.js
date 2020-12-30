export default function exibirConfirmar(titulo, mensagem, func) {
    const alerta = document.createElement('ion-alert');

    alerta.header = titulo;
    alerta.message = mensagem;
    alerta.buttons = [
        {
            text: 'Cancelar',
            role: 'cancel',
            handler: () => {}
        },
        {
            text: 'Confirmar',
            handler: () => func(),
        }
    ];

    document.body.appendChild(alerta);
    return alerta.present();
}