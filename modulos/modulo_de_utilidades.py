from colorama import Fore

def ler_numero_positivo(valor: str, tipo_de_numero : int) -> int:
    try:
        valor_positivo = int(input(valor).strip())

    except (KeyboardInterrupt):
        print(f'{Fore.RED}O usuário tentou interromper o programa!{Fore.RESET}')
        return 5

    except:
        erro = True
        while erro == True:
            valor_positivo = str(input(f'{Fore.RED}Digite um número válido:{Fore.RESET}'))
            if valor_positivo.isnumeric():
                if tipo_de_numero == 'int':
                    valor_positivo = int(valor_positivo)
                else:
                    valor_positivo = float(valor_positivo)
                if valor_positivo >= 0:
                    return valor_positivo

    else:
        return valor_positivo
