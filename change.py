def change():
    expense = 23.75
    money = 100
    change= money-expense
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(int(change))
    print("Centavos:")
    print(int((float(change)-int(change))*100))
