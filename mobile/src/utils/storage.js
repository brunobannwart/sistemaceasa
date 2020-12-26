import { Plugins } from '@capacitor/core';

const { Storage } = Plugins;

export async function armazenarItem(chave, valor) {
    await Storage.set({ key: chave, value: valor });
}

export async function obterItem(chave) {
    const { value: valor } = await Storage.get({ key: chave });
    return valor;
}

export async function removerItem(chave) {
    await Storage.remove({ key: chave });
}

export async function liberarArmazenamento() {
    await Storage.clear();
}