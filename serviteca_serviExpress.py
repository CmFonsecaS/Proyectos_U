automoviles = []
continuar = True  # Variable que controla el bucle principal

while continuar:
    print("\nMenú de opciones:")
    print("1. Registrar automóvil")
    print("2. Registro mantenimiento")
    print("3. Consultar automóvil")
    print("4. Salir")

    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        print("\nRegistro de automóvil:")
        
        # Validación de "patente"
        patente_valida = False
        while not patente_valida:
            patente = input("Ingrese la patente del automóvil (Formato AA1000 o BBBB10): ")
            if len(patente) == 6 and ((patente[:2].isalpha() and patente[2:].isdigit()) or (patente[:4].isalpha() and patente[4:].isdigit())):
                patente_valida = True
            else:
                print("Formato de patente incorrecto. Por favor, intente de nuevo.")
        
        # Validación de "marca"
        marca_valida = False
        while not marca_valida:
            marca = input("Ingrese la marca del automóvil: ")
            if marca != "":
                marca_valida = True
            else:
                print("Marca no puede estar vacía. Inténtelo de nuevo.")
        
        # Validación de "modelo"
        modelo_valido = False
        while not modelo_valido:
            modelo = input("Ingrese el modelo del automóvil: ")
            if modelo != "":
                modelo_valido = True
            else:
                print("Modelo no puede estar vacío. Inténtelo de nuevo.")
        
        # Validación de "anio_fabricacion" se utiliza anio por el tema de la letra "ñ" 
        anio_fabricacion_valido = False
        while not anio_fabricacion_valido:
            anio_fabricacion = input("Ingrese el año de fabricación: ")
            if anio_fabricacion.isdigit():
                anio_fabricacion = int(anio_fabricacion)
                if 1900 <= anio_fabricacion <= 2021:
                    anio_fabricacion_valido = True
                else:
                    print("El año de fabricación debe estar de 1900 a 2021.")
            else:
                print("Ingrese un número válido para el año de fabricación.")

        tipo_vehiculo = input("Ingrese el tipo de vehículo (b/d/e/h): ")

        automovil = {
            "patente": patente,
            "marca": marca,
            "modelo": modelo,
            "anio_fabricacion": anio_fabricacion,
            "tipo_vehiculo": tipo_vehiculo,
            "registros": []
        }
        automoviles.append(automovil)
        print("Automóvil registrado con éxito.")

    elif opcion == "2":
        patente = input("Ingrese la patente del automóvil para el registro de mantenimiento: ")
        encontrado = False
        for automovil in automoviles:
            if automovil["patente"] == patente:
                fecha_valida = False
                while not fecha_valida:
                    fecha = input("Ingrese la fecha del mantenimiento (Formato dd/mm/yyyy): ")
                    if len(fecha) == 10 and fecha[2] == "/" and fecha[5] == "/":
                        day = fecha[:2]
                        month = fecha[3:5]
                        year = fecha[6:]
                        if day.isdigit() and month.isdigit() and year.isdigit():
                            day = int(day)
                            month = int(month)
                            year = int(year)
                            if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2021:
                                fecha_valida = True
                            else:
                                print("Fecha inválida. Por favor, ingrese una fecha válida en el formato dd/mm/yyyy.")
                        else:
                            print("Fecha inválida. Por favor, ingrese una fecha válida en el formato dd/mm/yyyy.")
                    else:
                        print("Formato de fecha incorrecto. Por favor, ingrese la fecha en el formato dd/mm/yyyy.")
                
                observaciones = input("Ingrese las observaciones del mantenimiento: ")
                registro = f"Fecha: {fecha}\nObservaciones: {observaciones}"
                automovil["registros"].append(registro)
                encontrado = True

        if not encontrado:
            print("El automóvil no se encuentra registrado en el sistema.")

    elif opcion == "3":
        patente = input("Ingrese la patente del automóvil para consultar: ")
        encontrado = False
        for automovil in automoviles:
            if automovil["patente"] == patente:
                print("Información del automóvil:")
                print(f"Patente: {automovil['patente']}")
                print(f"Marca: {automovil['marca']}")
                print(f"Modelo: {automovil['modelo']}")
                print(f"Año de Fabricación: {automovil['anio_fabricacion']}")
                print(f"Tipo de Vehículo: {automovil['tipo_vehiculo']}")
                if automovil["registros"]:
                    print("Registros de Mantenimiento:")
                    for registro in automovil["registros"]:
                        print(registro)
                else:
                    print("No hay registros de mantenimiento para este automóvil.")
                encontrado = True

        if not encontrado:
            print("El automóvil no se encuentra registrado en el sistema.")

    elif opcion == "4":
        print("Cerrando sesión.")
        continuar = False  # Cambia el valor de la variable para salir

    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4).")


