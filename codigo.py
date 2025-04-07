def calcular_preco(volume):
    if 2000 < volume <= 3000:
        preco = 700
        desconto = 0.15
        preco_final = preco - (preco * desconto)
        return preco_final
    elif 3001 < volume <= 6000:
        preco = 1600
        desconto = 0.30
        preco_final = preco - (preco * desconto)
        return preco_final
    elif volume > 6001:
        preco = 2000
        desconto = 0.20
        preco_final = preco - (preco * desconto)
        return preco_final
    else:
        return "Volume inválido para cálculo de preço."

# Função principal
def main():
    print("Bem-vindo ao sistema de cálculo de preço de piscina!")
    try:
        volume = float(input("Digite o volume da piscina em litros: "))
        preco_final = calcular_preco(volume)
        if isinstance(preco_final, float):
            print(f"O preço final da piscina com o desconto é: R${preco_final:.2f}")
        else:
            print(preco_final)
    except ValueError:
        print("Por favor, insira um valor numérico válido para o volume.")

# Executa a função principal
main()
