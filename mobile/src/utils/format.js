export default function formatarData(data_hora) {
    var data, dia, mes, ano, hora, minutos;

    data = new Date(data_hora);

    data.setMinutes(
        data.getMinutes() + data.getTimezoneOffset(),
    );

    dia = (data.getDate() < 10) ?
        '0'.concat(data.getDate().toString()) :
        data.getDate().toString();

    mes = (data.getMonth() + 1 < 10) ?
        '0'.concat(data.getMonth().toString()) :
        data.getMonth().toString();

    ano = data.getFullYear().toString();
    hora = data.getHours().toString();
    minutos = data.getMinutes().toString();

    return dia.concat('/', mes, '/', ano, ' ', hora, ':', minutos);
}