def main():

    reais= float(input("Quantos reais voce tem?"))
    dolar = float(input("Qual o valor do dolar atualmente?"))

    conversao = reais / dolar
    print(f"Com R${reais} voce vai receber USS:{conversao}")

if __name__ == "__main__":
    main()