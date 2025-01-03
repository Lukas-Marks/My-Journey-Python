def main():

    idade = int(input("Quantos anos voce tem?"))

    if idade < 16:
        print("Menor")
    elif idade >= 16 or idade <= 18:
        print("Emancipado")
    else:
        print("Maior de idade")
if __name__ == "__main__":
    main()


