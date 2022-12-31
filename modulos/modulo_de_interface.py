import os
from colorama import Fore
from time import sleep
from modulos.modulo_de_utilidades import ler_inteiro

largura_terminal = os.get_terminal_size()[0]

def linha(tamanho=largura_terminal) -> str:
    linha = '-'
    return f'{Fore.YELLOW}{linha}' * largura_terminal


def cabecalho(texto: str) -> str:
    print(linha())
    print(texto.center(largura_terminal))
    print(linha())


def menu(opcoes : list) -> str:
    escolha = 0
    while escolha not in [1, 2, 3, 4]:
        contador = 1
        for item in opcoes:
            print(f'{Fore.BLUE}{contador}º opção - {Fore.YELLOW}{item}'.center(largura_terminal))
            contador += 1
        print(linha())
        escolha = ler_inteiro('Escolha sua opção: ')
        if escolha not in [1, 2, 3, 4]:
            print('Opção digitada não é válida! Tente novamente: ')
            sleep(1)
            print(linha())
        
    return escolha
