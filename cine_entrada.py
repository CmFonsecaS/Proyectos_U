
print("Bienvenido a Cine")

pertenece_a_cine = input("¿Eres estudiante o funcionario del cine? (si/no): ") == "si"

descuento = 0.3 if pertenece_a_cine else 0.0

tipo_entrada = input("¿Qué tipo de entrada deseas? (estreno/normal): ")
precio_entrada = 4800 if tipo_entrada == "estreno" else 2900

cantidad_entradas = int(input("¿Cuántas entradas deseas?: "))

agregar_palomitas = input("¿Deseas agregar palomitas? (si/no): ") == "si"
precio_palomitas = 0
if agregar_palomitas:
    print("Promociones de palomitas:")
    print("1. Palomitas pequeñas → $2.500")
    print("2. Palomitas medianas → $4.500")
    print("3. Palomitas grandes → $7.800")
    
    opcion_palomitas = int(input("Elige el tamaño de palomitas (1/2/3): "))
    if opcion_palomitas == 1:
        precio_palomitas = 2500
    elif opcion_palomitas == 2:
        precio_palomitas = 4500
    elif opcion_palomitas == 3:
        precio_palomitas = 7800

agregar_bebidas = input("¿Deseas agregar bebidas? (si/no): ") == "si"
precio_bebida = 0
if agregar_bebidas:
    print("Opciones de bebidas:")
    print("1. Bebida pequeña → $1.000")
    print("2. Bebida mediana → $1.250")
    print("3. Bebida grande → $2.000")
    
    opcion_bebida = int(input("Elige el tamaño de bebida (1/2/3): "))
    if opcion_bebida == 1:
        precio_bebida = 1000
    elif opcion_bebida == 2:
        precio_bebida = 1250
    elif opcion_bebida == 3:
        precio_bebida = 2000

total_sin_descuento = precio_entrada * cantidad_entradas + precio_palomitas + precio_bebida
total_con_descuento = total_sin_descuento - (total_sin_descuento * descuento)

print("\nResumen del pedido:")
print("Total sin descuento: $" + str(total_sin_descuento))
print("Descuento aplicado: $" + str(total_sin_descuento * descuento))
print("Total a pagar: $" + str(total_con_descuento))

efectivo = float(input("\nIngresa el efectivo: $"))
vuelto = efectivo - total_con_descuento
print("Vuelto: $" + str(vuelto))

print("\n¡Gracias por tu compra en CineDuoc!")











