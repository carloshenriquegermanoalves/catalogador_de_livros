from time import sleep

class Livro:

    def __init__(self, titulo_do_livro, nome_do_autor, genero_do_livro, quantidade_de_paginas):
        self.__titulo_do_livro : str = titulo_do_livro
        self.__nome_do_autor : str = nome_do_autor
        self.__genero_do_livro : str = genero_do_livro
        self.__quantidade_de_paginas : int = quantidade_de_paginas


    @property
    def titulo_do_livro(self : object) -> str:
        return self.__titulo_do_livro

    @titulo_do_livro.setter
    def alterar_titulo_do_livro(self : object, novo_titulo_do_livro: str) -> None:
        self.__titulo_do_livro = novo_titulo_do_livro


    @property
    def nome_do_autor(self : object) -> str:
        return self.__nome_do_autor


    @nome_do_autor.setter
    def alterar_nome_do_autor(self : object, novo_nome_do_autor : str) -> None:
        self.__nome_do_autor = novo_nome_do_autor


    @property
    def genero_do_livro(self : object) -> str:
        return self.__genero_do_livro


    @genero_do_livro.setter
    def alterar_genero_do_livro(self : object, novo_genero : str) -> None:
        self.__genero_do_livro = novo_genero


    @property
    def quantidade_de_paginas(self: object) -> int:
        return self.__quantidade_de_paginas


    @quantidade_de_paginas.setter
    def altera_quantidade_de_paginas(self : object, nova_quantidade_de_paginas : str) -> None:
        self.__quantidade_de_paginas = nova_quantidade_de_paginas


    @classmethod
    def registrar_livro_no_arquivo(livro : str, arquivo : str) -> bool:
        try:
            abrir_arquivo = arquivo.open(arquivo, 'at') #at = append text/adiciona texto
        except:
            print('Alguma coisa deu errada no registro do livro')
        else:
            try:
                abrir_arquivo.write(f'{livro.titulo_do_livro} - {livro.nome_do_autor} - {livro.genero_do_livro} - {livro.quantidade_de_paginas} -\n')
    
                arquivo = arquivo.close()        
        
            except:
                print('Alguma coisa deu errada enquanto as informações estavam sendo processadas! Vamos tentar de novo!')
            
            else:
                print(f'Um novo registro foi criado para o livro: {livro.titulo_do_livro}!')
        
        return True


    @classmethod
    def listar_livros_do_arquivo(lista_de_livros : list, arquivo : str) -> list:
        arquivo = arquivo.open(arquivo)

        for linha in arquivo:
            dado = linha.split('-')
            livro = Livro(dado[0], dado[1], dado[2], dado[3], dado[4])
            lista_de_livros.append(livro)
    
        arquivo = arquivo.close(arquivo)
        return lista_de_livros   


    @classmethod
    def procura_dados_por_titulo_do_livro(self : object, titulo_do_livro : str, lista_de_livros : list) -> object or bool:
        for livro in lista_de_livros:
            if titulo_do_livro in lista_de_livros[livro].titulo_do_livro:
                return lista_de_livros[livro]
        return False
    

    @classmethod
    def busca_livros_por_autor(self, nome_do_autor : str, lista_de_livros : list) -> list:
        self.__livros_do_autor_informado = []
        for livro in lista_de_livros:
            if nome_do_autor in lista_de_livros[livro].nome_do_autor:
                self.__livros_do_autor_informado.append(lista_de_livros[livro].titulo_do_livro)
        return self.__livros_do_autor_informado


    @classmethod
    def procura_livros_por_genero(self : object, genero_do_livro : str, lista_de_livros: list) -> list:
        self.__livros_encontrados = []
        for livro in lista_de_livros:
            if genero_do_livro in lista_de_livros[livro].genero_do_livro:
                self.__livros_encontrados.append(lista_de_livros[livro].titulo_do_livro)
        return self.__livros_encontrados


    @classmethod
    def procura_livros_por_paginas(self : object, lista_de_livros : list, quantidade_de_paginas : int, tipo_de_busca: bool =True) -> list:

        if tipo_de_busca == True:
            self.__livros_encontrados_mais_paginas = []
            for livro in lista_de_livros:
                if quantidade_de_paginas <= int(lista_de_livros[livro].quantidade_de_paginas):
                    self.__livros_encontrados_mais_paginas.append(lista_de_livros[livro].titulo_do_livro)
            return self.__livros_encontrados_mais_paginas
            

        else:
            self.__livros_encontrados_menos_paginas = []
            for livro in lista_de_livros:
                if quantidade_de_paginas >= int(lista_de_livros[livro].quantidade_de_paginas):
                    self.__livros_encontrados_menos_paginas.append(lista_de_livros[livro].titulo_do_livro)
            return self.__livros_encontrados_mais_paginas


    @classmethod
    def exibe_dados_do_livro(self, livro): #Depois que os dados do livro forem retornados
        print(f'Título do Livro - {livro.titulo_do_livro}')
        sleep(1)
        print(f'Nome do Autor - {livro.nome_do_autor}')
        sleep(1)
        print(f'Gênero do Livro - {livro.genero_do_livro}')
        sleep(1)
        print(f'Quantidade de páginas - {livro.quantidade_de_paginas}')
        sleep(1)


    @classmethod
    def exibe_livros_encontrados_por_buscas(self : object, livros_encontrados : list):
        for livro in livros_encontrados:
            print(f'{livros_encontrados[livro]}')
            sleep(1)
