export default function mascaraCampo(valor, mascara) {
    let formatado, digitos, posição, novoCampo, tamanhoMascara, existeMascara, expressaoRegular;

    // eslint-disable-next-line
    expressaoRegular = /\-|\.|\/|\(|\)| /g;
    posição = 0;
    novoCampo = '';

    digitos = valor.toString().replace(expressaoRegular, '');
    tamanhoMascara = digitos.length;

    for (let i = 0; i < tamanhoMascara; i += 1) {
        existeMascara = ((mascara.charAt(i) === '-') || (mascara.charAt(i) === '.') || (mascara.charAt(i) === '/'))
        existeMascara = existeMascara || ((mascara.charAt(i) === '(') || (mascara.charAt(i) === ')') || (mascara.charAt(i) === ' '))

        if (existeMascara) {
            novoCampo += mascara.charAt(i);
            tamanhoMascara++;
        } else {
            novoCampo += digitos.charAt(posição);
            posição++;
        }
    }

    formatado = novoCampo;
    return formatado;
}