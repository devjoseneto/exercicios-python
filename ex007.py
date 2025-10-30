from colorama import Fore, Style, init
init(autoreset=True)

def classificar_numero(n):
    """ Verifica se o número é positivo ou negativo e retorna uma mensagem """
    if n == 0:
        return f"{Fore.YELLOW + Style.BRIGHT}O número informado zero (0) é neutro: ele separa os positivos dos negativos na reta numérica."
    return f"{Fore.GREEN}{n} é Positivo" if n > 0 else f"{Fore.RED}{n} é Negativo"
    
def ler_numero(prompt):
    """ Ler um número do usuário com tratamento de erro """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"{Fore.RED + Style.BRIGHT}Entrada inválida! Por favor digite um número")

def main():
    n = ler_numero("Digite um número: ")
    print(classificar_numero(n))

if __name__ == "__main__":
    main()