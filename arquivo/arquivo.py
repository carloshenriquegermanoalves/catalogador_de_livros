import os

def cria_arquivo(nome_do_arquivo: str) -> None:
    try:
        novo_arquivo = open(nome_do_arquivo, "wt+")
        novo_arquivo.close()
    except:
        print("Alguma coisa deu errado na criação do arquivo!")
    else:
        print(f'O arquivo {nome_do_arquivo} foi criado com sucesso!')


def verifica_arquivo(nome_do_arquivo : str) -> bool:
    if os.path.exists(nome_do_arquivo): #Função que verifica se o arquivo de catálogo existe
        return True
    else:
        return False


arquivo = cria_arquivo('Catálogo.txt')