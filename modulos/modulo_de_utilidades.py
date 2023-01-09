from colorama import Fore

def ler_numero_positivo(valor: str, tipo_de_numero : int) -> int:
    if tipo_de_numero == 1:
        try:
            valor_positivo = int(input(valor).strip())
    else:
        try:
            valor_positivo = float(input(valor).strip())

    except (KeyboardInterrupt):
        print(f'{Fore.RED}O usuário tentou interromper o programa!{Fore.RESET}')
        return 5

    except:
        erro = True
        while erro == True:
            valor_positivo = str(input(f'{Fore.RED}Digite um número válido:{Fore.RESET}'))
            if valor_positivo.isnumeric():
                if tipo_de_numero == 1:
                    valor_positivo = int(valor_inteiro_positivo)
                else:
                    valor_positivo = float(valor_inteiro_positivo)
                if valor_positivo >= 0:
                    return valor_positivo

    else:
        return valor_positivo
