def qual_maior(n1, n2):
    """
    Compara dois números e retorna uma mensagem indicando qual é maior
    """

    if n1 > n2:
        return f"{n1} é maior que {n2}"
    elif n2 > n1:
        return f"{n2} é maior que {n1}"
    else:
        return "Números iguais"

def ler_numero(msg):
    """Ler um número do usuário com tratamento de erro"""
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Por favor, digite um número válido!")

def main():
    """ Função principal"""
    n1 = ler_numero("Digite o primeiro valor: ")
    n2 = ler_numero("Digite o segundo valor: ")

    print(qual_maior(n1, n2))

if __name__ == "__main__":
    main()