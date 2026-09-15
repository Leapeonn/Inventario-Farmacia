# Inventario-Farmacia
Sistema de inventario para farmacia

Programa en Python que administra el inventario de una farmacia desde la consola. Permite registrar medicamentos, sumar unidades a los que ya existen, realizar ventas descontando existencias, consultar el stock de un medicamento y ver las indicaciones de uso de cada uno.

Cómo ejecutarlo
Tener instalado Python 3.
Descargar el archivo inventario.py.
Abrir una terminal en la carpeta del archivo y escribir: python inventario.py
Elegir las opciones del menú escribiendo su número.
Funciones

buscar_posicion(claves, clave): recibe la lista de claves y la clave a buscar. Devuelve la posición del medicamento o -1 si no existe.

hay_existencia(existencias, posicion, unidades): recibe la lista de existencias, la posición del medicamento y las unidades pedidas. Devuelve True si hay stock suficiente y False si no.

calcular_subtotal(precio, unidades): recibe el precio unitario y la cantidad. Devuelve el importe de esa línea de venta.

registrar_medicamento(nombres, laboratorios, precios, existencias, claves, indicaciones, clave_actual): recibe las listas del inventario y la siguiente clave libre. Registra un medicamento nuevo o suma unidades a uno existente. Devuelve la siguiente clave libre.

procesar_venta(nombres, precios, existencias, claves): recibe las listas de nombres, precios, existencias y claves. Vende uno o varios medicamentos validando el stock. Devuelve el total cobrado.

consultar_existencia(nombres, laboratorios, existencias, claves, minimo): recibe las listas de datos y el stock mínimo. Muestra las unidades de un medicamento y avisa si está bajo el mínimo. Devuelve las unidades disponibles o -1 si no se consultó nada.

ver_indicaciones(nombres, laboratorios, indicaciones, claves): recibe las listas de datos. Muestra los medicamentos y las indicaciones del que se elija. Devuelve el texto mostrado o una cadena vacía.

menu_principal(registrados, ventas_dia): recibe la cantidad de medicamentos y las ventas acumuladas. Muestra el menú y devuelve la opción elegida.




Prueba 1: se registraron Acetaminofén (clave 100, $0.25, 50 unidades) e Ibuprofeno (clave 101, $0.40, 30 unidades) y se vendieron 3 unidades de Acetaminofén. Resultado: el programa mostró un total a cobrar de $0.75, las existencias de Acetaminofén bajaron a 47 y el menú mostró Ventas del día: $0.75.

Prueba 2: se intentó vender 40 unidades de Ibuprofeno teniendo solo 30. Resultado: el programa mostró el aviso Solo quedan 30 unidades de Ibuprofeno, no descontó nada y al cerrar la venta indicó Venta cerrada sin artículos.

Prueba 3: se sumaron 20 unidades a Ibuprofeno con la opción de medicamento existente, luego se consultaron sus existencias y sus indicaciones. Resultado: las existencias pasaron de 30 a 50, la consulta mostró Ibuprofeno (Genfar): 50 unidades sin aviso de stock bajo, y la opción 4 mostró el texto de uso que se escribió al registrarlo.
