
print("--------Bank ZFgroup--------")

saldo = 1000
confirmacion = "si"

while confirmacion == "si":
    print("\n====Menú====")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    match opcion:
        case "1":
            print(f"Su saldo actual es: {saldo}€")
        case "2":
            monto_retirar = float(input("Ingrese el monto a retirar: "))
            if monto_retirar <= saldo:
                saldo -= monto_retirar
                print(f"Ha retirado {monto_retirar}€. Su nuevo saldo es: {saldo}€")
            else:
                print("Saldo insuficiente para realizar el retiro.")
        case "3":
            monto_depositar = float(input("Ingrese el monto a depositar: "))
            saldo += monto_depositar
            print(f"Ha depositado {monto_depositar}€. Su nuevo saldo es: {saldo}€")
        case "4":
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

    confirmacion = input("¿Desea realizar otra operación? (si/no): ").lower()

    if confirmacion == "no":
        print("Gracias por usar el cajero automático. ¡Hasta luego!")