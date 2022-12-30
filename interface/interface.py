import os
from colorama import Fore
from time import sleep
from utilidades.funcoes_uteis import ler_inteiro

largura_terminal = os.get_terminal_size()[0]

def linha(tamanho=largura_terminal) -> str:
    return '-' * largura_terminal


def cabecalho(texto: str) -> str:
    print(linha())
    print(texto.center(largura_terminal))
    print(linha())


def menu(opcoes : list, menu=1):
    contador = 1

    if menu == 1:
        cabecalho('MENU PRINCIPAL')
        for item in opcoes:
            print(f'{Fore.BLUE}{contador}º opção - {Fore.YELLOW}{item}'.center(largura_terminal))
            contador += 1
        print(linha())
        escolha = ler_inteiro('Escolha sua opção: ')
        if escolha not in [1, 2, 3]:
            print('Opção inválida! Tente novamente')
            sleep(2)
            menu()

    else:
        cabecalho('MENU DE BUSCA')
        for item in opcoes:
            print(f'{Fore.BLUE}{contador}º opção - {Fore.YELLOW}{item}'.center(largura_terminal))
            contador += 1
        print(linha())
        escolha = ler_inteiro('Escolha sua opção: ')
        if escolha not in [1, 2, 3, 4, 5]:
            print('Opção inválida! Tente novamente')
            sleep(2)
            menu()
