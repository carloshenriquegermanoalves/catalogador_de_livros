import os
from modulos.modulo_de_interface import *
from time import sleep

class Autor:

    def __init__(self, nome_do_autor, nacionalidade_do_autor, sexo_do_autor):
        self.__nome_do_autor : str = nome_do_autor
        self.__nacionalidade_do_autor : str = nacionalidade_do_autor
        self.__sexo_do_autor : str = sexo_do_autor

    
    @property
    def nome_do_autor(self : object) -> str:
        return self.__nome_do_autor


    @nome_do_autor.setter
    def alterar_nome_do_autor(self : object, novo_nome_do_autor : str) -> None:
        self.__nome_do_autor = novo_nome_do_autor


    @property
    def nacionalidade_do_autor(self : object) -> str:
        return self.__nacionalidade_do_autor


    @nacionalidade_do_autor.setter
    def alterar_nacionalidade_do_autor(self : object, nova_nacionalidade_do_autor : str) -> None:
        self.__nacionalidade_do_autor = nova_nacionalidade_do_autor


    @property
    def sexo_do_autor(self : object) -> str:
        return self.__sexo_do_autor


    @sexo_do_autor.setter
    def sexo_do_autor(self : object, novo_sexo_do_autor : str) -> None:
        self.__sexo_do_autor = novo_sexo_do_autor


    @classmethod
    def quantidade_livros_masculinos(self : object, lista_de_livros : list) -> int:
        livros_masculinos = 0
        for autor in range(len(lista_de_livros)):
            if 'Masculino' in lista_de_livros[autor].sexo_do_autor:
                livros_masculinos += 1
        return livros_masculinos


    @classmethod
    def quantidade_livros_femininos(self : object, lista_de_livros : list) -> int:
        livros_femininos = 0
        for autor in range(len(lista_de_livros)):
            if 'Feminino' in lista_de_livros[autor].sexo_do_autor:
                livros_femininos += 0
        return livros_femininos


    @classmethod
    def lista_autores(self : object, lista_de_livros : list) -> list:
        self.__autores = []
        for autor in range(len(lista_de_livros)):
            if 'Masculino' in lista_de_livros[autor].sexo_do_autor:
                if lista_de_livros[autor].nome_do_autor not in self.__autores:
                    self.__autores_.append(lista_de_livros[autor].nome_do_autor)
        return self.__autores


    @classmethod
    def lista_autoras(self : object, lista_de_livros : list) -> list:
        self.__autoras = []
        for autor in range(len(lista_de_livros)):
            if 'Feminino' in lista_de_livros[autor].sexo_do_autor:
                if lista_de_livros[autor].nome_do_autor not in self.__autoras:
                    self.__autoras.append(lista_de_livros[autor].nome_do_autor)
        return self.__autoras


    @classmethod
    def exibir_todos_autores(self : object, lista_de_autores : list) -> str:
        cabecalho('Todos os Autores Cadastrados na Biblioteca São')
        for autor in range(len(lista_de_autores)):
            sleep(1)
            print(lista_de_autores[autor])
        sleep(1)


    @classmethod
    def exibe_autores(self : object, lista_de_autores : list) -> str:
        cabecalho('Todos os Autores Cadastrados na Biblioteca São')
        for autor in range(len(lista_de_autores)):
            sleep(1)
            print(lista_de_autores[autor])
        sleep(1)


    @classmethod
    def exibe_autoras(self : object, lista_de_autoras : list) -> str:
        cabecalho('Todas as Autoras Cadastradas na Biblioteca São')
        for autora in range(len(lista_de_autoras)):
            sleep(1)
            print(lista_de_autoras[autora])
        sleep(1)


class Genero(Autor):
    
    def __init__(self, nome_do_autor, nacionalidade_do_autor, sexo_do_autor, genero_do_livro, subgenero_do_livro):
        super().__init__(nome_do_autor, nacionalidade_do_autor, sexo_do_autor)
        self.__genero_do_livro : str = genero_do_livro
        self.__subgenero_do_livro : str = subgenero_do_livro


    @property
    def genero_do_livro(self : object) -> str:
        return self.__genero_do_livro


    @genero_do_livro.setter
    def alterar_genero_do_livro(self : object, novo_genero : str) -> None:
        self.__genero_do_livro = novo_genero


    @property
    def subgenero_do_livro(self : object) -> str:
        return self.__subgenero_do_livro


    @subgenero_do_livro.setter
    def alterar_subgenero_do_livro(self : object, novo_subgenero : str) -> None:
        self.__subgenero_do_livro = novo_subgenero


    @classmethod
    def lista_generos(self : object, lista_de_livros : list) -> list:
        self.__generos = []
        for genero in range(len(lista_de_livros)):
            if lista_de_livros[genero].genero_do_livro not in self.__generos:
                self.__generos.append(lista_de_livros[genero].genero_do_livro)
        return self.__generos


    @classmethod
    def ordena_genero_alfabeticamente(self : object, lista_de_generos : set) -> list:
        lista_de_generos.sort()
        return lista_de_generos


    @classmethod
    def exibe_todos_os_generos(self : object, lista_de_generos : list) -> str:
        cabecalho('Os Gêneros de Todos os Livros Cadastrados na Biblioteca São:')
        for genero in range(len(lista_de_generos)):
            sleep(1)
            print(f'{lista_de_generos[genero]}')
        sleep(1)


class Livro(Genero):

    def __init__(self, titulo_do_livro, nome_do_autor, nacionalidade_do_autor, sexo_do_autor, genero_do_livro, subgenero_do_livro, quantidade_de_paginas):
        self.__titulo_do_livro : str = titulo_do_livro
        super().__init__(nome_do_autor, nacionalidade_do_autor, sexo_do_autor, genero_do_livro, subgenero_do_livro)
        self.__quantidade_de_paginas : int = quantidade_de_paginas


    @property
    def titulo_do_livro(self : object) -> str:
        return self.__titulo_do_livro


    @titulo_do_livro.setter
    def alterar_titulo_do_livro(self : object, novo_titulo_do_livro: str) -> None:
        self.__titulo_do_livro = novo_titulo_do_livro


    @property
    def quantidade_de_paginas(self: object) -> int:
        return self.__quantidade_de_paginas


    @quantidade_de_paginas.setter
    def altera_quantidade_de_paginas(self : object, nova_quantidade_de_paginas : str) -> None:
        self.__quantidade_de_paginas = nova_quantidade_de_paginas


    @classmethod
    def registrar_livro_no_arquivo(self : object, livro : str, arquivo : str) -> None:
        try:
            abrir_arquivo = open(arquivo, 'at')
        except Exception as e:
            print(e)
            print('Alguma coisa deu errada enquanto as informações estavam sendo processadas! Vamos tentar de novo!')
        else:
            try:
                abrir_arquivo.write(f' {livro.titulo_do_livro} - {livro.nome_do_autor} - {livro.nacionalidade_do_autor} - {livro.sexo_do_autor} - {livro.genero_do_livro} - {livro.subgenero_do_livro} {livro.quantidade_de_paginas} -\n')
            except Exception as e:
                print(e)
                print('Alguma coisa deu errado quando as informações estavam sendo salvas! Vamos tentar novamente!')
            else:
                print(f'Um novo registro para o livro {livro.titulo_do_livro} foi criado!')
                abrir_arquivo.close()


    @classmethod
    def listar_livros_do_arquivo(self : object, arquivo : str) -> list:
        self.__lista_de_livros = []
        if os.path.exists(arquivo):
            arquivo = open(arquivo, 'r')
            for item in arquivo.readlines():
                dados = item.split('-')
                livro = Livro(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6])
                self.__lista_de_livros.append(livro)
        return self.__lista_de_livros


    @classmethod
    def ordena_livros_alfabeticamente(self : object, lista_de_livros: list) -> list:
        self.__ordem_alfabetica = []
        for livro in range(len(lista_de_livros)):
            self.__ordem_alfabetica.append(lista_de_livros[livro].titulo_do_livro)
        self.__ordem_alfabetica.sort()
        return self.__ordem_alfabetica


    @classmethod
    def ordena_livros_alfabeticamente_por_genero(self : object, generos_alfabeticamente : list, lista_de_livros : list) -> list:
        self.__livros_ordenados_por_generos_alfabeticos = []
        for genero in range(len(generos_alfabeticamente)):
            self.__livros_do_genero_indexado = []
            for livros in range(len(lista_de_livros)):
                if lista_de_livros[livros].genero_do_livro in generos_alfabeticamente[genero]:
                    self.__livros_do_genero_indexado.append(lista_de_livros[livros].titulo_do_livro)
                    self.__livros_do_genero_indexado.sort()
            self.__livros_ordenados_por_generos_alfabeticos.append(self.__livros_do_genero_indexado)
        return self.__livros_ordenados_por_generos_alfabeticos


    @classmethod
    def busca_dados_por_titulo_do_livro(self : object, titulo_do_livro : str, lista_de_livros : list) -> object or bool:
        for livro in range(len(lista_de_livros)):
            if titulo_do_livro in lista_de_livros[livro].titulo_do_livro:
                return lista_de_livros[livro]
        return False
    

    @classmethod
    def busca_livros_por_autor(self : object, nome_do_autor : str, lista_de_livros : list) -> list:
        self.__livros_do_autor_informado = []
        for livro in range(len(lista_de_livros)):
            if nome_do_autor in lista_de_livros[livro].nome_do_autor:
                self.__livros_do_autor_informado.append(lista_de_livros[livro].titulo_do_livro)
        return self.__livros_do_autor_informado


    @classmethod
    def busca_livros_por_genero(self : object, genero_do_livro : str, lista_de_livros: list) -> list:
        self.__livros_encontrados = []
        for livro in range(len(lista_de_livros)):
            if genero_do_livro in lista_de_livros[livro].genero_do_livro:
                self.__livros_encontrados.append(lista_de_livros[livro].titulo_do_livro)
        return self.__livros_encontrados


    @classmethod
    def busca_livros_por_paginas(self : object, lista_de_livros : list, quantidade_de_paginas : int, tipo_de_busca: bool =True) -> list:

        if tipo_de_busca == True:
            self.__livros_encontrados_mais_paginas = []
            for livro in range(len(lista_de_livros)):
                if quantidade_de_paginas <= int(lista_de_livros[livro].quantidade_de_paginas):
                    self.__livros_encontrados_mais_paginas.append(lista_de_livros[livro].titulo_do_livro)
            return self.__livros_encontrados_mais_paginas

        else:
            self.__livros_encontrados_menos_paginas = []
            for livro in range(len(lista_de_livros)):
                if quantidade_de_paginas >= int(lista_de_livros[livro].quantidade_de_paginas):
                    self.__livros_encontrados_menos_paginas.append(lista_de_livros[livro].titulo_do_livro)
            return self.__livros_encontrados_menos_paginas


    @classmethod
    def exibe_todos_os_livros(self : object, lista_de_livros : list) -> str:
        cabecalho('Livros Cadastrados na Biblioteca:')
        for livro in range(len(lista_de_livros)):
            sleep(1)
            print(f'{lista_de_livros[livro].titulo_do_livro}')
        sleep(1)


    @classmethod
    def exibe_livros_alfabeticamente(self : object, lista_de_livros : list) -> str:
        cabecalho('Exibindo Todos os Livros Alfabeticamente')
        for livro in range(len(lista_de_livros)):
            sleep(1)
            print(f'{lista_de_livros[livro]}')
        sleep(1)


    @classmethod
    def exibe_livros_alfabeticamente_por_genero(self : object, lista_generos_alfabeticamente : list, lista_livros_alfabeticamente : list) -> str:
        for genero in range(len(lista_generos_alfabeticamente)):
            cabecalho(f'Os livros do gênero {lista_generos_alfabeticamente[genero]} são')
            for livro in range(len(lista_livros_alfabeticamente[genero])):
                sleep(1)
                print(lista_livros_alfabeticamente[genero][livro])
        sleep(1)


    @classmethod
    def exibe_dados_do_livro(self : object, livro : str) -> str:
        cabecalho(f'Dados do Livro "{livro.titulo_do_livro}"')
        sleep(1)
        print(f'Nome do Autor - {livro.nome_do_autor}')
        sleep(1)
        print(f'País do Autor - {livro.nacionalidade_do_autor}')
        sleep(1)
        print(f'Sexo do Autor - {livro.sexo_do_autor}')
        sleep(1)
        print(f'Gênero do Livro - {livro.genero_do_livro}')
        sleep(1)
        print(f'Subgênero do Livro - {livro.subgenero_do_livro}')
        sleep(1)
        print(f'Quantidade de páginas - {livro.quantidade_de_paginas}')
        sleep(1)


    @classmethod
    def exibe_livros_encontrados_por_buscas(self : object, livros_encontrados : list) -> str:
        for livro in range(len(livros_encontrados)):
            sleep(1)
            print(f'{livros_encontrados[livro]}')
        sleep(1)
