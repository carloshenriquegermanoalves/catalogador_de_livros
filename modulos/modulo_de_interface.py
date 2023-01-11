import os
from colorama import Fore
from time import sleep
from modulos.modulo_de_utilidades import ler_numero_positivo

largura_terminal = os.get_terminal_size()[0]

def linha(tamanho=largura_terminal) -> str:
    linha = '-'
    return f'{Fore.YELLOW}{linha}' * largura_terminal


def cabecalho(texto: str) -> str:
    print(linha())
    print(texto.center(largura_terminal))
    print(linha())


def menu(opcoes : list) -> str:
    contador = 1
    for item in opcoes:
        print(f'{Fore.BLUE}{contador}º opção - {Fore.YELLOW}{item}'.center(largura_terminal))
        contador += 1
    print(linha())
    escolha = ler_numero_positivo('Escolha sua opção: ', 'int')    
    return escolha


def reinicia_menu(opcao_desejada : int) -> str:
    lista_de_menus = [
        ['Área de Exibição', 'Área de Cadastro', 'Área de Busca', 'Área de Edição' 'Sair do Sistema'], 
        
        ['Exibir Todos Os Autores', 'Exibir Autores Masculinos', 'Exibir Autoras'],
        
        ['Sim', 'Não'], 
        
        ['Já li o livro', 'Não li o livro'], 
        
        ['Buscar Livro', 'Buscar Autor', 'Buscar por Data'], 
        
        ['Busca por Título do Livro', 'Busca por Gênero do Livro', 'Busca por Quantidade de Páginas'],
        
        ['Digite 1 para buscar livros com a quantidade de páginas maior ou igual ao informado', 'Digite 2 para buscar livros com a quantidade de páginas menor ou igual ao informado'],
        
        ['Livros de Autores Masculinos', 'Livros de Autoras', 'Busca por Nome do Autor', 'Busca por Nacionalidade do Autor'],  
        
        ['Buscar livros lidos em um ano informado', 'Buscar Livros que Não Foram Lidos']
        
        ['Alterar Título do Livro', 'Alterar Nome do Autor', 'Alterar Nacionalidade do Autor', 'Alterar Sexo do Autor', 'Alterar Gênero do Livro', 'Alterar Subgênero do Livro', 'Alterar Quantidade de Páginas do Livro', 'Adicionar Releitura']
        
            ]

    print('Opção Digitada Não É Válida! Tente Novamente')
    sleep(1)
    menu(lista_de_menus[opcao_desejada])
