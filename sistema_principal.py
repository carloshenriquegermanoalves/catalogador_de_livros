from modulos.modulo_de_arquivos import *
from modulos.modulo_de_interface import *
from modulos.modulo_de_utilidades import *
from classes import *
from time import sleep

arquivo = 'Catálogo.txt'

if verifica_arquivo(arquivo) == False:
    cria_arquivo(arquivo)

opcao_menu = 0

while opcao_menu != 5:
    lista_de_livros = Livro.listar_livros_do_arquivo(arquivo)
    lista_de_generos = Livro.lista_generos(lista_de_livros)
    
    cabecalho('MENU PRINCIPAL')
    opcao_menu = menu(['Área de Exibição', 'Área de Cadastro', 'Área de Busca', 'Área de Edição', 'Sair do Sistema'])

    if opcao_menu == 1:
        cabecalho('MENU DE EXIBIÇÃO')
        opcao_exibicao = menu(['Ordem de Aquisição', 'Ordem Alfabética', 'Lista de Gêneros','Lista de Autores','Ordenados Alfabeticamente por Gêneros'])
        
        if opcao_exibicao == 1:
            cabecalho('Livros Cadastrados na Biblioteca:')
            Livro.exibe_todos_os_livros(lista_de_livros)

        elif opcao_exibicao == 2:
            livros_ordem_alfabetica = Livro.ordena_livros_alfabeticamente(lista_de_livros)
            cabecalho('Exibindo Todos os Livros Alfabeticamente')
            Livro.exibe_livros(livros_ordem_alfabetica)
    
        elif opcao_exibicao == 3:
            Livro.exibe_todos_os_generos(lista_de_generos)

        elif opcao_exibicao == 4:
            opcao_exibir_autor = menu(['Exibir Todos Os Autores', 'Exibir Autores Masculinos', 'Exibir Autoras', 'Quantidade de Livros por Autores Masculinos', 'Quantidade de Livros por Autoras'])
            if opcao_exibir_autor == 1:
                todos_autores = Livro.lista_todos_autores_alfabeticamente(lista_de_livros)
                Livro.exibe_todos_autores(todos_autores)
            
            elif opcao_exibir_autor == 2:
                autores_masculinos = Livro.lista_autores_alfabeticamente(lista_de_livros)
                Livro.exibe_autores(autores_masculinos)

            elif opcao_exibir_autor == 3:
                autoras = Livro.lista_autoras_alfabeticamente(lista_de_livros)
                Livro.exibe_autoras(autoras)
                
            elif opcao_exibir_autor == 4:
                quantidade_livros_masculinos = Livro.quantidade_livros_masculinos(lista_de_livros)
                cabecalho(f'A quantidade de livros escritos por autores masculinos é: {quantidade_livros_masculinos}')
                sleep(1)

            elif opcao_exibir_autor == 5:
                quantidade_livros_femininos = Livro.quantidade_livros_femininos(lista_de_livros)
                cabecalho(f'A quantidade de livros escritos por autoras é: {quantidade_livros_femininos}')
                sleep(1)

            else:
                reinicia_menu(2)

        elif opcao_exibicao == 5:
            generos_ordem_alfabetica = Genero.ordena_genero_alfabeticamente(lista_de_generos)
            livros_alfabeticamente_genero = Livro.ordena_livros_alfabeticamente_por_genero(generos_ordem_alfabetica, lista_de_livros)
            Livro.exibe_livros_alfabeticamente_por_genero(generos_ordem_alfabetica, livros_alfabeticamente_genero)

        else:
            reinicia_menu(1)


    elif opcao_menu == 2:
        cabecalho('MENU DE CADASTRO')

        titulo_do_livro = str(input('Informe o título do livro: ')).strip().title()
        autor_do_livro = str(input('Informe o autor do livro: ')).strip().title()
    
        sleep(1)
        cabecalho(f'Você sabe a nacionalidade do autor {autor_do_livro}?')
        sleep(1)
        verifica_nacionalidade = menu(['Sim', 'Não'])

        if verifica_nacionalidade == 1:
            nacionalidade_do_autor = str(input('Digite o país do autor: ')).strip().title()
        elif verifica_nacionalidade == 2:
            nacionalidade_do_autor = 'Desconhecida'
        else:
            reinicia_menu(2)

        sexo_do_autor = str(input('Digite o sexo do autor: ')).strip().title()
        genero_do_livro = str(input('Informe o gênero do livro: ')).strip().title()
        subgenero_do_livro = str(input('Digite o subgênero do livro: ')).strip().title()
        quantidade_de_paginas = ler_numero_positivo('Informe a quantidade de páginas: ', 'int')

        sleep(1)
        cabecalho(f'Você já leu o livro {titulo_do_livro}? ')
        sleep(1)
        verifica_leitura = menu(['Já li o livro', 'Não li o livro'])
        
        if verifica_leitura == 1:
            ano_de_leitura = ler_numero_positivo('Digite o ano que foi feita a leitura: ', 'int')
            nota_do_livro = ler_numero_positivo('Digite sua nota para o livro: ', 'float')
        elif verifica_leitura == 2:
            ano_de_leitura = 0
            nota_do_livro = 0
        else:
            reinicia_menu(3)

        livro = Livro(titulo_do_livro, autor_do_livro, nacionalidade_do_autor, sexo_do_autor, genero_do_livro, subgenero_do_livro, quantidade_de_paginas, ano_de_leitura, nota_do_livro)
        Livro.registrar_livro_no_arquivo(livro, arquivo)
        sleep(1.5)


    elif opcao_menu == 3:
        cabecalho('MENU DE BUSCA')
        escolha = menu(['Buscar Livro', 'Buscar Autor', 'Buscar por Data'])
        if escolha == 1:
            buscar_livro = menu(['Busca por Título do Livro', 'Busca por Gênero do Livro', 'Busca por Quantidade de Páginas'])

            if buscar_livro == 1:
                titulo_para_busca = input('Informe o título do livro para busca: ').strip().title()
                procura_livro = Livro.busca_dados_por_titulo_do_livro(titulo_para_busca, lista_de_livros)
                
                if procura_livro == False:
                    print(f'O livro {titulo_para_busca} não foi encontrado! Verifique se o livro foi cadastrado e tente novamente')
                else:
                    Livro.exibe_dados_do_livro(procura_livro)

            elif buscar_livro == 2:
                genero_para_busca = input('Informe o gênero do livro para busca: ').strip().title()
                livros_do_genero = Livro.busca_livros_por_genero(genero_para_busca, lista_de_livros)
                if len(livros_do_genero) > 0:
                    cabecalho(f'Os livros do gênero {genero_para_busca} são:')
                    Livro.exibe_livros(livros_do_genero)
                else:
                    cabecalho(f'Não foi encontrado nenhum livro do gênero {genero_para_busca}')

            elif buscar_livro == 4:
                tipo_de_busca = menu(['Buscar livros com a quantidade de páginas maior ou igual ao informado', 'Buscar livros com a quantidade de páginas menor ou igual ao informado'])
                if tipo_de_busca not in [1, 2]:
                    reinicia_menu(4)

                quantidade_de_paginas = ler_numero_positivo('Digite a quantidade de páginas para busca: ', 'int')
                    
                if tipo_de_busca == 1:
                    livros_encontrados = Livro.busca_livros_por_paginas(lista_de_livros, quantidade_de_paginas, True)
                    if len(livros_encontrados) > 0:
                        cabecalho(f'Os livros com mais de {quantidade_de_paginas} páginas são')
                        Livro.exibe_livros(livros_encontrados)
                    else:
                        cabecalho(f'Não há livros com mais de {livros_encontrados} cadastrados')

                elif tipo_de_busca == 2:
                    livros_encontrados = Livro.busca_livros_por_paginas(lista_de_livros, quantidade_de_paginas, False)
                    if len(livros_encontrados) > 0:
                        cabecalho(f'Os livros com menos de {quantidade_de_paginas} páginas são')
                        Livro.exibe_livros(livros_encontrados)
                    else:
                        cabecalho(f'Não há livros com menos de {quantidade_de_paginas} cadastrados')

        elif escolha == 2:
            buscar_autor = menu(['Livros de Autores Masculinos', 'Livros de Autoras', 'Busca por Nome do Autor', 'Busca por Nacionalidade do Autor'])
            if buscar_autor == 1:
                livros_masculinos = Livro.livros_autores(lista_de_livros)
                cabecalho('Os Livros Escritos Por Homens Cadastrados na Biblioteca São')
                Livro.exibe_livros(livros_masculinos)

            elif buscar_autor == 2:
                livros_femininos = Livro.livros_autoras(lista_de_livros)
                cabecalho('Os Livros Escritos Por Mulheres Cadastradas na Biblioteca São')
                Livro.exibe_livros(lista_de_livros)

            elif buscar_autor == 3:
                autor_para_busca = str(input('Informe o autor para busca: ')).strip().title()
                livros_do_autor = Livro.busca_livros_por_autor(autor_para_busca, lista_de_livros)
                if len(livros_do_autor) > 0:
                    cabecalho(f'Os livros do autor {autor_para_busca} são:')
                    Livro.exibe_livros_encontrados_por_buscas(livros_do_autor)
                else:
                    cabecalho(f'Não foi encontrado nenhum livro do autor {autor_para_busca}')
            
            elif buscar_autor == 4:
                nacionalidade_para_busca = str(input('Informe o país do autor para a busca: '))
                livros_nacionalidade_informada = Livro.busca_livros_nacionalidade_autor(nacionalidade_para_busca, lista_de_livros)
                if len(livros_nacionalidade_informada) > 0:
                    cabecalho(f'Os Livros Escritos por Autores do País {nacionalidade_para_busca} são')
                    Livro.exibe_livros(livros_nacionalidade_informada)
                else:
                    cabecalho(f'Não foi encontrado nenhum livro cujo autor fosse do país {nacionalidade_para_busca}')

            else:
                reinicia_menu(6)
        
        elif escolha == 3:
            opcao_de_busca = menu(['Buscar livros lidos em um ano informado', 'Buscar Livros que Não Foram Lidos'])
            if opcao_de_busca == 1:
                ano_para_busca = ler_numero_positivo('Digite um ano para a busca: ', 'int')
                livros_lidos_ano_informado = Livro.busca_livros_por_ano(lista_de_livros, ano_para_busca)
                if len(livros_lidos_ano_informado) > 0:
                    cabecalho(f'Os livros lidos no ano {ano_para_busca} são')
                    Livro.exibe_livros(livros_lidos_ano_informado)
                else:
                    cabecalho(f'Não foram lidos nenhum dos livros cadastrados em {ano_para_busca}')

    elif opcao_menu == 4:
        cabecalho('MENU DE EDIÇÃO')

        escolha_edicao = menu(['Alterar Título do Livro', 'Alterar Nome do Autor', 'Alterar Nacionalidade do Autor', 'Alterar Sexo do Autor', 'Alterar Gênero do Livro', 'Alterar Subgênero do Livro', 'Alterar Quantidade de Páginas do Livro'])


    else:
        reinicia_menu(0)

print('Fechando o sistema. Volte sempre. . .')
exit(0)
