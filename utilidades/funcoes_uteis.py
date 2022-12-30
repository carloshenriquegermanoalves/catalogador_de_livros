from colorama import Fore

def ler_inteiro(valor: str) -> int:
    try:
        valor_inteiro = int(input(valor).strip())

    except (KeyboardInterrupt):
        print(f'{Fore.RED}O usuário tentou interromper o programa!{Fore.RESET}')
        return 4

    except:
        erro = True
        while erro == True:
            valor_inteiro = str(input('{Fore.RED}Digite um número válido:{Fore.RESET}'))
            if (valor_inteiro.isnumeric()):
                valor_inteiro = int(valor_inteiro)
                erro = False
                return valor_inteiro

    else:
        return valor_inteiro
