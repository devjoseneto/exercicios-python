import math

VALOR_LATA = 80
VALOR_GALAO = 25

def obter_area():
    while True:
        try:
            valor = int(input("Informe a area em metros quadrados (m²): "))
            if valor > 0:
                return valor
            print("Digite um valor positivo!")
        except ValueError:
            print("Valor invalido, digite um valor válido!")

def calcular_qtd_necessaria(area):
    return area / 6 * 1.1

def calcular_qtd_latas(litros_necessarios):
    latas = math.ceil(litros_necessarios / 18)
    custo_latas = latas * VALOR_LATA
    return {
        "qtd_latas": latas,
        "custo_latas": custo_latas
    }

def calcular_qtd_galoes(litros_necessarios):
    galoes = math.ceil(litros_necessarios / 3.6)
    custo_galoes = galoes * VALOR_GALAO
    return {
        "qtd_galoes": galoes,
        "custo_galoes": custo_galoes
    }

def calcular_qtd_mix(litros_necessarios):
    latas_mix = int(litros_necessarios // 18)
    resto = litros_necessarios - (latas_mix * 18)
    galoes_mix = (math.ceil(resto / 3.6))
    custo_mix = (latas_mix * VALOR_LATA) + (galoes_mix * VALOR_GALAO)
    return {
        'qtd_latas_mix': latas_mix,
        'qtd_galoes_mix': galoes_mix,
        'custo_mix': custo_mix
    }

def imprimir_resultado(area, qtd_necessaria, latas, galoes, mix):
    print('--- Resultado ---')
    print(f'Área total: {area}m²')
    print(f'Litros necessários (com 10% de folga): {qtd_necessaria:.2f} L')
    print()
    print(f'Apenas latas de 18L: {latas['qtd_latas']} lata(s) → R$ {latas['custo_latas']:.2f}')
    print(f'Apenas galoes de 3.6L: {galoes['qtd_galoes']} galao(ões) → R$ {galoes['custo_galoes']:.2f}')
    print(f'Combinação otimizada: {mix['qtd_latas_mix']} lata(s) e {mix['qtd_galoes_mix']} galão(ões) → R$ {mix['custo_mix']:.2f}')


if __name__ == '__main__':
    area = obter_area()
    qtd_necessaria = calcular_qtd_necessaria(area)
    latas = calcular_qtd_latas(qtd_necessaria)
    galoes = calcular_qtd_galoes(qtd_necessaria)
    mix = calcular_qtd_mix(qtd_necessaria)

    imprimir_resultado(area, qtd_necessaria, latas, galoes, mix)