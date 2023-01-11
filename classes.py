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
    def lista_autores_alfabeticamente(self : object, lista_de_livros : list) -> list:
        self.__autores = []
        for autor in range(len(lista_de_livros)):
            if 'Masculino' in lista_de_livros[autor].sexo_do_autor:
                if lista_de_livros[autor].nome_do_autor not in self.__autores:
                    self.__autores.append(lista_de_livros[autor].nome_do_autor)
                    self.__autores.sort()
        return self.__autores


    @classmethod
    def lista_autoras_alfabeticamente(self : object, lista_de_livros : list) -> list:
        self.__autoras = []
        for autora in range(len(lista_de_livros)):
            if 'Feminino' in lista_de_livros[autora].sexo_do_autor:
                if lista_de_livros[autora].nome_do_autor not in self.__autoras:
                    self.__autoras.append(lista_de_livros[autora].nome_do_autor)
                    self.__autoras.sort()
        return self.__autoras


    @classmethod
    def lista_todos_autores_alfabeticamente(self : object, lista_de_livros : list) -> list:
        self.__todos_autores = []
        for autores in range(len(lista_de_livros)):
            if lista_de_livros[autores].nome_do_autor not in self.__todos_autores:
                self.__todos_autores.append(lista_de_livros[autores].nome_do_autor)
                self.__todos_autores.sort()
        return self.__todos_autores


    @classmethod
    def mensagem_sem_autor(self : object) -> str:
        cabecalho('Ainda Não Há Nenhum Autor Cadastrado na Biblioteca')


    @classmethod
    def exibe_todos_autores(self : object, lista_de_autores : list) -> str:
        if len(lista_de_autores) > 0:
            cabecalho('Todos os Autores Cadastrados na Biblioteca, em Ordem Alfabética, São')
            for autor in range(len(lista_de_autores)):
                sleep(1)
                print(lista_de_autores[autor])
        else:
            Autor.mensagem_sem_autor()
        sleep(1)


    @classmethod
    def exibe_autores(self : object, lista_de_autores : list) -> str:
        if len(lista_de_autores) > 0:
            cabecalho('Todos os Autores Cadastrados na Biblioteca, em Ordem Alfabética, São')
            for autor in range(len(lista_de_autores)):
                sleep(1)
                print(lista_de_autores[autor])
        else:
            Autor.mensagem_sem_autor()
        sleep(1)


    @classmethod
    def exibe_autoras(self : object, lista_de_autoras : list) -> str:
        if len(lista_de_autoras) > 0:
            cabecalho('Todas as Autoras Cadastradas na Biblioteca, em Ordem Alfabética, São')
            for autora in range(len(lista_de_autoras)):
                sleep(1)
                print(lista_de_autoras[autora])
        else:
            Autor.mensagem_sem_autor()
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
    def mensagem_sem_genero(self : object) -> str:
        cabecalho('Ainda Não Há Nenhum Gênero Cadastrado na Biblioteca')


    @classmethod
    def exibe_todos_os_generos(self : object, lista_de_generos : list) -> str:
        if len(lista_de_generos) > 0:
            cabecalho('Os Gêneros de Todos os Livros Cadastrados na Biblioteca São:')
            for genero in range(len(lista_de_generos)):
                sleep(1)
                print(f'{lista_de_generos[genero]}')
        else:
            Genero.mensagem_sem_genero()
        sleep(1)


class Livro(Genero):

    def __init__(self, titulo_do_livro, nome_do_autor, nacionalidade_do_autor, sexo_do_autor, genero_do_livro, subgenero_do_livro, quantidade_de_paginas, ano_de_leitura, nota_do_livro):
        self.__titulo_do_livro : str = titulo_do_livro
        super().__init__(nome_do_autor, nacionalidade_do_autor, sexo_do_autor, genero_do_livro, subgenero_do_livro)
        self.__quantidade_de_paginas : int = quantidade_de_paginas
        self.__ano_de_leitura : int = ano_de_leitura
        self.__nota_do_livro : float = nota_do_livro


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

    
    @property
    def ano_de_leitura(self : object) -> int:
        return self.__ano_de_leitura


    @ano_de_leitura.setter
    def altera_ano_de_leitura(self : object, ano_de_leitura_alterado : int) -> None:
        self.__ano_de_leitura = ano_de_leitura_alterado


    @property
    def nota_do_livro(self : object) -> float:
        return self.__nota_do_livro

    
    @nota_do_livro.setter
    def altera_nota_do_livro(self : object, nova_nota_do_livro : float) -> None:
        self.__nota_do_livro = nova_nota_do_livro


    @classmethod
    def registrar_livro_no_arquivo(self : object, livro : str, arquivo : str) -> None:
        try:
            abrir_arquivo = open(arquivo, 'at')
        except Exception as e:
            print(e)
            print('Alguma coisa deu errada enquanto as informações estavam sendo processadas! Vamos tentar de novo!')
        else:
            try:
                abrir_arquivo.write(f' {livro.titulo_do_livro} - {livro.nome_do_autor} - {livro.nacionalidade_do_autor} - {livro.sexo_do_autor} - {livro.genero_do_livro} - {livro.subgenero_do_livro} - {livro.quantidade_de_paginas} - {livro.ano_de_leitura} - {livro.nota_do_livro} - \n')
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
                livro = Livro(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7], dados[8])
                self.__lista_de_livros.append(livro)
        return self.__lista_de_livros


    @classmethod
    def livros_autores(self : object, lista_de_livros : list) -> list:
        self.__livros_autores = []
        for autor in range(len(lista_de_livros)):
            if 'Masculino' in lista_de_livros[autor].sexo_do_autor:
                self.__livros_autores.append(lista_de_livros[autor].titulo_do_livro)
        return self.__livros_autores


    @classmethod
    def livros_autoras(self : object, lista_de_livros : list) -> list:
        self.__livros_autoras = []
        for autora in range(len(lista_de_livros)):
            if 'Feminino' in lista_de_livros[autora].sexo_do_autor:
                self.__livros_autoras.append(lista_de_livros[autora].titulo_do_livro)
        return self.__livros_autoras


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


    def busca_livros_nacionalidade_autor(self : object, nacionalidade_autor : str, lista_de_livros : list) -> list:
        self.__livros_nacionalidade_informada = []
        for nacionalidade in range(len(lista_de_livros)):
            if nacionalidade_autor in lista_de_livros[nacionalidade].nacionalidade_do_autor:
                self.__livros_nacionalidade_informada.append(lista_de_livros[nacionalidade].titulo_do_livro)
        return self.__livros_nacionalidade_informada


    @classmethod
    def busca_livros_por_genero(self : object, genero_do_livro : str, lista_de_livros: list) -> list:
        if len(genero_do_livro) > 0:
            self.__livros_encontrados = []
            for livro in range(len(lista_de_livros)):
                if genero_do_livro in lista_de_livros[livro].genero_do_livro:
                    self.__livros_encontrados.append(lista_de_livros[livro].titulo_do_livro)
            return self.__livros_encontrados
        else:
            Genero.mensagem_sem_genero()


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
    def busca_livros_por_ano(self : object, lista_de_livros : list, ano_informado : int) -> list:
        self.__livros_ano_informado = []
        for livro in range(len(lista_de_livros)):
            if ano_informado == int(lista_de_livros[livro].ano_de_leitura):
                self.__livros_ano_informado.append(lista_de_livros[livro].titulo_do_livro)
        return self.__livros_ano_informado


    @classmethod
    def mensagem_sem_livro(self : object) -> str:
        cabecalho('Não Há Livros Cadastrados na Biblioteca')


    @classmethod
    def exibe_livros(self : object, lista_de_livros : list) -> str:
        if len(lista_de_livros) > 0:
            for livro in range(len(lista_de_livros)):
                sleep(1)
                print(f'{lista_de_livros[livro]}')
        else:
            Livro.mensagem_sem_livro()
        sleep(1)


    @classmethod
    def exibe_todos_os_livros(self : object, lista_de_livros : list) -> str:
        if len(lista_de_livros) > 0:
            for livro in range(len(lista_de_livros)):
                sleep(1)
                print(f'{lista_de_livros[livro].titulo_do_livro}')
        else:
            Livro.mensagem_sem_livro()
        sleep(1)


    @classmethod
    def exibe_livros_alfabeticamente_por_genero(self : object, lista_generos_alfabeticamente : list, lista_livros_alfabeticamente : list) -> str:
        if len(lista_generos_alfabeticamente) > 0:
            for genero in range(len(lista_generos_alfabeticamente)):
                cabecalho(f'Os livros do gênero {lista_generos_alfabeticamente[genero]} são')
                for livro in range(len(lista_livros_alfabeticamente[genero])):
                    sleep(1)
                    print(lista_livros_alfabeticamente[genero][livro])
                sleep(1)
        else:
            Livro.mensagem_sem_livro()
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
