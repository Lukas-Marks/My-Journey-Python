def main():

    dolar = float(input("Quantos Dollares voce tem?"))
    reais = float(input("Qual o valor do real atualmente?"))

    conversao = dolar * reais
    print(f"Com USS:{dolar} voce vai receber R$:{conversao}")

if __name__ == "__main__":
    main()