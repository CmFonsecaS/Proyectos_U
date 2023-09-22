
zapatos = 20000
cantidad_zapatos = int(input("Ingrese la cantidad de zapatos: "))

compra = cantidad_zapatos * zapatos

if compra >= 40000:
    print(f"Su total a pagar es: {compra}, con envio gratis")
else:
    costo_envio = compra + 3000
    print(f"Su total a pagar es: {costo_envio}, incluyendo el valor de envio")
