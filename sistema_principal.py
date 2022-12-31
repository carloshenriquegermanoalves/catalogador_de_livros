from modulos.modulo_de_arquivos import *
from modulos.modulo_de_interface import *
from modulos.modulo_de_utilidades import *
from classes import *
from time import sleep

arquivo = 'Catálogo.txt'

if verifica_arquivo(arquivo) == False:
    cria_arquivo(arquivo)

opcao_menu = 0

while opcao_menu != 4:
    lista_de_livros = Livro.listar_livros_do_arquivo(arquivo)

    cabecalho('MENU PRINCIPAL')
    opcao_menu = menu(['Ver Livros da Biblioteca', 'Cadastrar Livro', 'Buscar Livro', 'Sair do Sistema'])

    if opcao_menu == 1:
        Livro.exibe_todos_os_livros(lista_de_livros)
    elif opcao_menu == 2:
        cabecalho('Cadastro de Novo Livro')

        titulo_do_livro = str(input('Informe o título do livro: ')).strip().title()
        autor_do_livro = str(input('Informe o autor do livro: ')).strip().title()
        genero_do_livro = str(input('Informe o gênero do livro: ')).strip().title()
        quantidade_de_paginas = ler_inteiro('Informe a quantidade de páginas: ')

        livro = Livro(titulo_do_livro, autor_do_livro, genero_do_livro, quantidade_de_paginas)
        Livro.registrar_livro_no_arquivo(livro, arquivo)
        sleep(1.5)

    elif opcao_menu == 3:
        cabecalho('MENU DE BUSCA')
        escolha = menu(['Busca por Título do Livro', 'Busca por Nome do Autor', 'Busca por Gênero do Livro', 'Busca por Quantidade de Páginas'])

        if escolha == 1:
            titulo_para_busca = input('Informe o título do livro para busca: ').strip().title()
            procura_livro = Livro.busca_dados_por_titulo_do_livro(titulo_para_busca, lista_de_livros)
            
            if procura_livro == False:
                print(f'O livro {titulo_para_busca} não foi encontrado! Verifique se o livro foi cadastrado e tente novamente')
            else:
                Livro.exibe_dados_do_livro(procura_livro)

        elif escolha == 2:
            autor_para_busca = input('Informe o autor para busca: ').strip().title()
            livros_do_autor = Livro.busca_livros_por_autor(autor_para_busca, lista_de_livros)
            if len(livros_do_autor) > 0:
                cabecalho(f'Os livros do autor {autor_para_busca} são:')
                Livro.exibe_livros_encontrados_por_buscas(livros_do_autor)
            else:
                cabecalho(f'Não foi encontrado nenhum livro do autor {autor_para_busca}')
                
        elif escolha == 3:
            genero_para_busca = input('Informe o gênero do livro para busca: ').strip().title()
            livros_do_genero = Livro.busca_livros_por_genero(genero_para_busca, lista_de_livros)
            if len(livros_do_genero) > 0:
                cabecalho(f'Os livros do gênero {genero_para_busca} são:')
                Livro.exibe_livros_encontrados_por_buscas(livros_do_genero)
            else:
                cabecalho(f'Não foi encontrado nenhum livro do gênero {genero_para_busca}')

        else:
            if escolha == 4:
                tipo_de_busca = 0
                while tipo_de_busca not in [1, 2]:
                    tipo_de_busca = menu(['Digite 1 para buscar livros com a quantidade de páginas maior ou igual ao informado', 'Digite 2 para buscar livros com a quantidade de páginas menor ou igual ao informado'])
                    if tipo_de_busca not in [1, 2]:
                        print('Opção digitada não é válida! Tente novamente: ')
                        sleep(2)
                        break
        

                quantidade_de_paginas = ler_inteiro('Digite a quantidade de páginas para busca: ')
                
                if tipo_de_busca == 1:
                    livros_encontrados = Livro.busca_livros_por_paginas(lista_de_livros, quantidade_de_paginas, True)
                    if len(livros_encontrados) > 0:
                        cabecalho(f'Os livros com mais de {quantidade_de_paginas} páginas são')
                        Livro.exibe_livros_encontrados_por_buscas(livros_encontrados)
                    else:
                        cabecalho(f'Não há livros com mais de {livros_encontrados} cadastrados')

                else:
                    livros_encontrados = Livro.busca_livros_por_paginas(lista_de_livros, quantidade_de_paginas, False)
                    if len(livros_encontrados) > 0:
                        cabecalho(f'Os livros com menos de {quantidade_de_paginas} páginas são')
                        Livro.exibe_livros_encontrados_por_buscas(livros_encontrados)
                    else:
                        cabecalho(f'Não há livros com menos de {quantidade_de_paginas} cadastrados')

            else:
                print('Opção digitada não é valida! Por favor, tente novamente')
                sleep(1)
                opcao_menu = menu(['Ver Livros da Biblioteca', 'Cadastrar Livro', 'Buscar Livro', 'Sair do Sistema'])


print('Fechando o sistema. Volte sempre. . .') #Ocorre quando sai do loop do while
exit(0)
