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

def calcular_custo_minimo(latas, galoes, mix):
    custo_minimo = min(latas['custo_latas'], galoes['custo_galoes'], mix['custo_mix'])
    if custo_minimo == latas['custo_latas']:
        return 'Apenas latas'
    elif custo_minimo == galoes['custo_galoes']:
        return 'Apenas galoes'
    else:
        return 'Mistura otimizada'

def imprimir_resultado(area, qtd_necessaria, latas, galoes, mix, melhor_opcao):
    print('--- Resultado ---')
    print(f'Área total: {area}m²')
    print(f'Litros necessários (com 10% de folga): {qtd_necessaria:.2f} L')
    print()
    print(f'Apenas latas de 18L: {latas['qtd_latas']} lata(s) → R$ {latas['custo_latas']:.2f}')
    print(f'Apenas galoes de 3.6L: {galoes['qtd_galoes']} galao(ões) → R$ {galoes['custo_galoes']:.2f}')
    print(f'Combinação otimizada: {mix['qtd_latas_mix']} lata(s) e {mix['qtd_galoes_mix']} galão(ões) → R$ {mix['custo_mix']:.2f}')
    print(f'Melhor opção: {melhor_opcao}')

def salvar_resultados_em_arquivo(area, qtd_necessaria, latas, galoes, mix, melhor_opcao):
    with open("resultado_tinta.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write('--- Resultado ---\n')
        arquivo.write(f'Área total: {area}m²\n')
        arquivo.write(f'Litros necessários (com 10% de folga): {qtd_necessaria:.2f} L\n')
        arquivo.write("\n")
        arquivo.write(f'Apenas latas de 18L: {latas['qtd_latas']} lata(s) → R$ {latas['custo_latas']:.2f}\n')
        arquivo.write(f'Apenas galoes de 3.6L: {galoes['qtd_galoes']} galao(ões) → R$ {galoes['custo_galoes']:.2f}\n')
        arquivo.write(f'Combinação otimizada: {mix['qtd_latas_mix']} lata(s) e {mix['qtd_galoes_mix']} galão(ões) → R$ {mix['custo_mix']:.2f}\n')
        arquivo.write(f'Melhor opção: {melhor_opcao}\n')
    print("Resultado salvo com sucesso em resultado_tinta.txt")

def perguntar_se_quer_salvar():
    while True:
        resposta = input("\nDeseja salvar o resultado em um arquivo? (s/n): ").strip().lower()
        if resposta in {'s', 'sim'}:
            return True
        if resposta in ('n', 'nao', 'não'):
            return False
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

if __name__ == '__main__':
    area = obter_area()
    qtd_necessaria = calcular_qtd_necessaria(area)
    latas = calcular_qtd_latas(qtd_necessaria)
    galoes = calcular_qtd_galoes(qtd_necessaria)
    mix = calcular_qtd_mix(qtd_necessaria)
    melhor_opcao = calcular_custo_minimo(latas, galoes, mix)
    imprimir_resultado(area, qtd_necessaria, latas, galoes, mix, melhor_opcao)
    if perguntar_se_quer_salvar():
        salvar_resultados_em_arquivo(area, qtd_necessaria, latas, galoes, mix, melhor_opcao)
    else:
        print("\nResultado não foi salvo.")
