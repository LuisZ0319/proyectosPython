
notas = [8, 4.2, 5, 3, 10]

while True:
    print("*******MENU*******")
    print("1. Añadir nota")
    print("2. Mostrar notas")
    print("3. Calcular media")
    print("4. Mostrar nota más alta")
    print("5. Mostrar nota más baja")
    print("6. Notas aprobadas")
    print("7. Buscar notas")
    print("8. Eliminar nota")
    print("9. Salir")

    while True:
        try:
            opcion = input("Seleccione una opción: ")
            break
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

    match opcion:
        case "1":
            while True:
                try:
                    nota = float(input("Ingrese la nota a añadir: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        print(f"Nota {nota} añadida correctamente.")
                        break
                    else:
                        print("Error: La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Error: Por favor, ingrese un número válido.")
        case "2":
            print("Notas actuales:", notas)
        case "3":
            if notas:
                media = sum(notas) / len(notas)
                print(f"La media de las notas es: {media:.2f}")
            else:
                print("No hay notas para calcular la media.")
        case "4":
            if notas:
                nota_maxima = max(notas)
                print(f"La nota más alta del alumno es: {nota_maxima}")
            else:
                print("No hay notas para mostrar.")
        case "5":
            if notas:
                nota_minima = min(notas)
                print(f"La nota más baja del alumno es: {nota_minima}")
            else:
                print("No hay notas para mostrar.")
        case "6":
            notasAprobadas = 0
            for i in notas:
                if i >= 5:
                    notasAprobadas += 1
            print(f"El número de notas aprobadas es: {notasAprobadas}")
        case "7": 
            encontrada = False
            buscarnota = float(input("Ingrese la nota a buscar: "))
            for i in notas:
                if i == buscarnota:
                    encontrada = True
                    print(f"La nota {buscarnota} se encuentra en la lista.")
                    break
            if not encontrada:
                print(f"La nota {buscarnota} no se encuentra en la lista.")
        case "8":
            eliminar = False
            if not notas:
                print("No hay notas para eliminar.")
            else:
                for i in notas:
                    print(i)
                eliminarNota = float(input("Ingrese la nota a eliminar: "))
                if eliminarNota in notas:
                    notas.remove(eliminarNota)
                    eliminar = True
                    print(f"La nota {eliminarNota} ha sido eliminada.")
                else:
                    print(f"La nota {eliminarNota} no se encuentra en la lista.")
        case "9":
            print("¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")
    