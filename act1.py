lista = []
while True:
    Ask = input("\nCorrupt Offices (press '0' to quit)\nWhat is your command?: ").capitalize()
    if Ask == "0":
        print("\nSakto na kay gyera na!")
        break
    elif Ask == "Add":
        num = int(input("Enter a number: "))
        lista.append(num)
    elif Ask == "Display":
        print(lista)
    elif Ask == "Naa":
        lista.pop(0)
    elif Ask == "Wala":
        lista.pop(-1)
    else:
        print("\nWrong Move ka kol!")
        break