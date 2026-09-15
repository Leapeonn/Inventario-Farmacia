# Inventario de farmacia - version 1
# Cada medicamento ocupa la misma posicion en todas las listas.


def buscar_posicion(claves, clave):
    # Devuelve la posicion del medicamento o -1 si la clave no existe
    if clave in claves:
        return claves.index(clave)
    return -1


def hay_existencia(existencias, posicion, unidades):
    # Devuelve True si alcanzan las unidades pedidas
    if unidades <= existencias[posicion]:
        return True
    return False


def calcular_subtotal(precio, unidades):
    # Devuelve el importe de una linea de venta
    return precio * unidades


def registrar_medicamento(nombres, laboratorios, precios, existencias, claves, indicaciones, clave_actual):
    # Devuelve la siguiente clave disponible
    print("\n=== REGISTRO DE MEDICAMENTO ===")
    print("(Escribe 0 en cualquier campo para volver al menú)")

    if len(nombres) > 0:
        print("¿El medicamento ya está en el sistema?")
        print("1) Sí, solo quiero sumar unidades")
        print("2) No, es un medicamento nuevo")
        respuesta = int(input("Elige: "))
        while respuesta not in [0, 1, 2]:
            print("Esa opción no existe, intenta de nuevo.")
            respuesta = int(input("Elige: "))
        if respuesta == 0:
            print("Registro cancelado.")
            return clave_actual
    else:
        print("Todavía no hay medicamentos, se registrará uno nuevo.")
        respuesta = 2

    # --- Sumar unidades a uno que ya existe ---
    if respuesta == 1:
        clave = int(input("Clave del medicamento: "))
        posicion = buscar_posicion(claves, clave)
        if posicion == -1:
            print("No hay ningún medicamento con esa clave.")
            return clave_actual
        unidades = int(input(f"Unidades a sumar para {nombres[posicion]}: "))
        while unidades < 0:
            print("Las unidades no pueden ser negativas.")
            unidades = int(input(f"Unidades a sumar para {nombres[posicion]}: "))
        if unidades == 0:
            print("Sin cambios.")
            return clave_actual
        existencias[posicion] += unidades
        print(f"Listo. {nombres[posicion]} ahora tiene {existencias[posicion]} unidades.")
        return clave_actual

    # --- Medicamento nuevo, el usuario escribe todos sus datos ---
    nombre = input("Nombre comercial: ").strip()
    while nombre == "":
        print("El nombre es obligatorio.")
        nombre = input("Nombre comercial: ").strip()
    if nombre == "0":
        print("Registro cancelado.")
        return clave_actual

    laboratorio = input("Laboratorio que lo fabrica: ").strip()
    while laboratorio == "":
        print("El laboratorio es obligatorio.")
        laboratorio = input("Laboratorio que lo fabrica: ").strip()
    if laboratorio == "0":
        print("Registro cancelado.")
        return clave_actual

    uso = input("¿Para qué sirve y cómo se toma?: ").strip()
    while uso == "":
        print("Describe el uso del medicamento.")
        uso = input("¿Para qué sirve y cómo se toma?: ").strip()
    if uso == "0":
        print("Registro cancelado.")
        return clave_actual

    precio = float(input("Precio por unidad: "))
    while precio < 0:
        print("El precio no puede ser negativo.")
        precio = float(input("Precio por unidad: "))
    if precio == 0:
        print("Registro cancelado.")
        return clave_actual

    unidades = int(input("Unidades iniciales: "))
    while unidades < 0:
        print("Las unidades no pueden ser negativas.")
        unidades = int(input("Unidades iniciales: "))
    if unidades == 0:
        print("Registro cancelado.")
        return clave_actual

    claves.append(clave_actual)
    nombres.append(nombre)
    laboratorios.append(laboratorio)
    indicaciones.append(uso)
    precios.append(precio)
    existencias.append(unidades)
    print(f"\n{nombre} quedó registrado con la clave {clave_actual}.")
    return clave_actual + 1


def procesar_venta(nombres, precios, existencias, claves):
    # Devuelve el total cobrado en esta venta
    if len(nombres) == 0:
        print("\nNo hay medicamentos para vender.")
        return 0

    total = 0
    articulos = 0
    seguir = True
    while seguir:
        print("\n=== CAJA ===")
        for i in range(len(nombres)):
            print(f"[{claves[i]}] {nombres[i]} - ${precios[i]} - {existencias[i]} disponibles")
        clave = int(input("Clave del medicamento (0 para cerrar la venta): "))
        if clave == 0:
            seguir = False
            continue

        posicion = buscar_posicion(claves, clave)
        if posicion == -1:
            print("Clave incorrecta.")
            continue

        unidades = int(input(f"¿Cuántas unidades de {nombres[posicion]}? "))
        if unidades <= 0:
            print("Cantidad no válida, se omite este artículo.")
            continue

        if not hay_existencia(existencias, posicion, unidades):
            print(f"Solo quedan {existencias[posicion]} unidades de {nombres[posicion]}.")
            continue

        subtotal = calcular_subtotal(precios[posicion], unidades)
        existencias[posicion] -= unidades
        total += subtotal
        articulos += 1
        print(f"Agregado: {unidades} x {nombres[posicion]} = ${subtotal}")
        print(f"Total acumulado: ${total}")

    if articulos == 0:
        print("Venta cerrada sin artículos.")
    else:
        print(f"\nTotal a cobrar: ${total} ({articulos} artículos)")
    return total


def consultar_existencia(nombres, laboratorios, existencias, claves, minimo):
    # Devuelve las unidades del medicamento consultado o -1 si no se consultó nada
    if len(nombres) == 0:
        print("\nNo hay medicamentos registrados.")
        return -1

    print("\n=== CONSULTA DE EXISTENCIAS ===")
    clave = int(input("Clave del medicamento (0 para volver): "))
    if clave == 0:
        return -1
    posicion = buscar_posicion(claves, clave)
    if posicion == -1:
        print("Esa clave no corresponde a ningún medicamento.")
        return -1

    print(f"{nombres[posicion]} ({laboratorios[posicion]}): {existencias[posicion]} unidades")
    if existencias[posicion] < minimo:
        print("Aviso: existencias por debajo del mínimo, conviene reabastecer.")
    return existencias[posicion]


def ver_indicaciones(nombres, laboratorios, indicaciones, claves):
    # Devuelve el texto de indicaciones mostrado, o "" si no se mostró nada
    if len(nombres) == 0:
        print("\nNo hay medicamentos registrados.")
        return ""

    print("\n=== INDICACIONES ===")
    for i in range(len(nombres)):
        print(f"[{claves[i]}] {nombres[i]}")
    clave = int(input("Clave del medicamento (0 para volver): "))
    if clave == 0:
        return ""
    posicion = buscar_posicion(claves, clave)
    if posicion == -1:
        print("Esa clave no corresponde a ningún medicamento.")
        return ""

    print(f"\n{nombres[posicion]} - {laboratorios[posicion]}")
    print(f"Uso: {indicaciones[posicion]}")
    return indicaciones[posicion]


def menu_principal(registrados, ventas_dia):
    # Devuelve la opcion elegida por el usuario
    print("\n======= FARMACIA =======")
    print(f"Medicamentos registrados: {registrados} | Ventas del día: ${ventas_dia}")
    print("1) Registrar medicamento")
    print("2) Vender")
    print("3) Consultar existencias")
    print("4) Ver indicaciones de un medicamento")
    print("5) Cerrar sistema")
    opcion = int(input("Opción: "))
    while opcion not in [1, 2, 3, 4, 5]:
        print("Esa opción no está en el menú.")
        opcion = int(input("Opción: "))
    return opcion


# ================= PROGRAMA PRINCIPAL =================
nombres = []
laboratorios = []
indicaciones = []
precios = []
existencias = []
claves = []

clave_actual = 100
ventas_dia = 0
minimo_stock = 10
opcion = 0

while opcion != 5:
    opcion = menu_principal(len(nombres), ventas_dia)

    if opcion == 1:
        clave_actual = registrar_medicamento(nombres, laboratorios, precios, existencias, claves, indicaciones, clave_actual)
    elif opcion == 2:
        ventas_dia += procesar_venta(nombres, precios, existencias, claves)
    elif opcion == 3:
        unidades = consultar_existencia(nombres, laboratorios, existencias, claves, minimo_stock)
        if unidades == 0:
            print("Este medicamento está agotado.")
    elif opcion == 4:
        texto = ver_indicaciones(nombres, laboratorios, indicaciones, claves)
        if texto != "":
            print("Consulta terminada.")

print(f"\nSistema cerrado. Total vendido hoy: ${ventas_dia}")
