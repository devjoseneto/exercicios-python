IR_PERCENTUAL = 0.11
INSS_PERCENTUAL = 0.08
SINDICATO_PERCENTUAL = 0.05

def obter_valor_positivo(msg):
    while True:
        try:
            valor = float(input(msg))
            if valor > 0:
                return valor
            print("❌ O valor deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido.")

def calcular_salario(valor_hora, qtd_horas):
    return valor_hora * qtd_horas

def calcular_descontos(salario):
    return {
        "ir": salario * IR_PERCENTUAL,
        "inss": salario * INSS_PERCENTUAL,
        "sindicato": salario * SINDICATO_PERCENTUAL
    }

def calcular_salario_liquido(salario, descontos):
    return salario - sum(descontos.values())

def imprimir_folha_salarial(salario, descontos, salario_liquido):
    print(f'+ Salário Bruto : R$ {salario:.2f}')
    print(f'- IR (11%)      : R$ {descontos["ir"]:.2f}')
    print(f'- INSS (8%)     : R$ {descontos["inss"]:.2f}')
    print(f'- Sindicato (5%): R$ {descontos["sindicato"]:.2f}')
    print(f'= Salário Líquido: R$ {salario_liquido:.2f}')

salario_hora = obter_valor_positivo("Informe o valor da hora trabalhada: R$")
hora_mes = obter_valor_positivo("Informe o total de horas trabalhadas no mês: ")
salario_bruto = calcular_salario(salario_hora, hora_mes)
descontos = calcular_descontos(salario_bruto)
salario_liquido = calcular_salario_liquido(salario_bruto, descontos)

imprimir_folha_salarial(salario_bruto, descontos, salario_liquido)