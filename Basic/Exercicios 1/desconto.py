def main():

    precodoProduto = float(input("Qual o preço do produto?"))
    desconto = float(input("Qual é o desconto desse produto (em porcentagem)"))
    porcentagem = desconto / 100
    resultado = precodoProduto * porcentagem
    print(f"Você vai pagar {resultado} Reais")

if __name__ == "__main__":
    main()