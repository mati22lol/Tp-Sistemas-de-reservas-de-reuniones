DIAS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
HORARIOS = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"]

def mostrar_guia():
    """Muestra las instrucciones iniciales al usuario"""
    print("=" * 60)
    print(" GUÍA DE USO - SISTEMA DE RESERVAS ".center(60, "="))
    print("=" * 60)
    print("1. Puede gestionar entre 1 y 5 oficinas simultáneamente.")
    print("2. Los días disponibles son de Lunes a Viernes.")
    print("3. El rango horario es de 10:00 a 22:00 (bloques de 1 hora).")
    print("4. En las tablas: '0' es LIBRE y '1' es OCUPADO.")
    print("-" * 60)

def crear_oficinas(cant_ofis):
    oficinas = []
    for i in range(cant_ofis):
        matriz = []
        for h in range(len(HORARIOS)):
            fila = [0] * len(DIAS)
            matriz.append(fila)
        oficinas.append(matriz)
    return oficinas

def mostrar_oficinas(oficinas):
    print("\n" + " ESTADO ACTUAL DE LAS OFICINAS ".center(70, "█"))
    for i in range(len(oficinas)):
        print(f"\n>>> OFICINA {i + 1} ".ljust(70, "-"))
        
        # Encabezado de días
        header = "HORA".ljust(10)
        for d in DIAS:
            header += d.ljust(12)
        print(header)
        
        # Filas de horarios
        for h_idx in range(len(HORARIOS)):
            fila_texto = HORARIOS[h_idx].ljust(10)
            for d_idx in range(len(DIAS)):
                estado = "LIBRE" if oficinas[i][h_idx][d_idx] == 0 else "OCUPADO"
                fila_texto += estado.ljust(12)
            print(fila_texto)

def obtener_datos_reserva(cant_ofis):
    """Función auxiliar para pedir datos de forma limpia y validada"""
    # Validar Oficina
    ofi = int(input(f"Número de oficina (1-{cant_ofis}): "))
    while ofi < 1 or ofi > cant_ofis:
        ofi = int(input(f"Error. Ingrese una oficina válida (1-{cant_ofis}): "))
    
    # Validar Día (uso de métodos de cadena)
    dia = input("Ingrese el día (Lunes-Viernes): ").strip().capitalize()
    while dia not in DIAS:
        print("Día no válido o no laborable.")
        dia = input("Ingrese el día nuevamente: ").strip().capitalize()
    
    # Validar Horario
    hora = input("Ingrese horario (ej. 14:00): ").strip()
    while hora not in HORARIOS:
        print(f"Horario fuera de rango. Los turnos son: {HORARIOS}")
        hora = input("Ingrese horario nuevamente: ").strip()
        
    return ofi - 1, DIAS.index(dia), HORARIOS.index(hora), dia, hora

def gestionar_reserva(oficinas, tipo="reservar"):
    """Maneja tanto reservas como cancelaciones"""
    accion = "reservar" if tipo == "reservar" else "cancelar"
    print(f"\n--- FORMULARIO PARA {accion.upper()} ---")
    
    ofi_idx, d_idx, h_idx, dia_nom, hora_nom = obtener_datos_reserva(len(oficinas))
    
    if tipo == "reservar":
        if oficinas[ofi_idx][h_idx][d_idx] == 0:
            oficinas[ofi_idx][h_idx][d_idx] = 1
            print(f"\n ÉXITO: Oficina {ofi_idx+1} reservada para el {dia_nom} a las {hora_nom}.")
        else:
            print(f"\n ERROR: El turno ya está ocupado por otro usuario.")
    else:
        if oficinas[ofi_idx][h_idx][d_idx] == 1:
            oficinas[ofi_idx][h_idx][d_idx] = 0
            print(f"\n ÉXITO: Reserva cancelada para el {dia_nom} a las {hora_nom}.")
        else:
            print(f"\n AVISO: No existía ninguna reserva en ese horario.")

def menu():
    mostrar_guia()
    
    cant = int(input("¿Con cuántas oficinas desea trabajar hoy? (Máximo 5): "))
    while cant < 1 or cant > 5:
        cant = int(input("Por favor, elija entre 1 y 5 oficinas: "))
    
    oficinas = crear_oficinas(cant)
    print(f"\nSistema inicializado con {cant} oficinas.")

    while True:
        print("\n" + "=" * 30)
        print(" MENU PRINCIPAL ".center(30, " "))
        print("=" * 30)
        print("1. Ver disponibilidad (Tablas)")
        print("2. Realizar una Reserva")
        print("3. Cancelar una Reserva")
        print("4. Cambiar de Turno")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")

        if opcion == "1":
            mostrar_oficinas(oficinas)
        elif opcion == "2":
            gestionar_reserva(oficinas, "reservar")
        elif opcion == "3":
            gestionar_reserva(oficinas, "cancelar")
        elif opcion == "4":
            print("\nPara cambiar de turno, primero cancelaremos el actual y luego crearemos el nuevo.")
            gestionar_reserva(oficinas, "cancelar")
            gestionar_reserva(oficinas, "reservar")
        elif opcion == "5":
            print("\n" + " Gracias por usar PrograReservas. Hasta pronto! ".center(60, "═"))
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
        input("\nPresione ENTER para volver al menú...")


menu()