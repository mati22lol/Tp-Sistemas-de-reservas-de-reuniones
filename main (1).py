import json
import random

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
    print("-" * 60)

def pedir_entero(mensaje, minimo, maximo):
    valido = False
    numero = 0

    while valido == False:
        try:
            numero = int(input(mensaje))

            if numero < minimo or numero > maximo:
                print("Error. Debe ingresar un número entre", minimo, "y", maximo)
            else:
                valido = True

        except ValueError:
            print("Error. Debe ingresar un número entero.")

    return numero    

def crear_oficinas(cant_ofis):
    oficinas = {}
    
    for i in range(1, cant_ofis + 1):
        oficinas[f"oficina_{i}"] = {}                            #La estructura que genera es exactamente el JSON

        for dia in DIAS:                                         #Tres diccionarios anidados: oficina → día → hora.
            oficinas[f"oficina_{i}"][dia] = {}
            
            for hora in HORARIOS:
                oficinas[f"oficina_{i}"][dia][hora] = {
                    "estado": "libre",
                    "cliente": "",
                    "dni": "",
                    "telefono": "",
                    "codigo": ""
                }

    return oficinas

def mostrar_oficinas(oficinas):
    print("\n" + " ESTADO ACTUAL DE LAS OFICINAS ".center(70, "█"))

    for nombre_ofi, dias in oficinas.items():
        print(f"\n>>> {nombre_ofi.upper()}".ljust(70, "-"))
        
        # Encabezado de días
        header = "HORA".ljust(10)
        for d in DIAS:
            header += d.ljust(12)
        print(header)
        
        # Filas de horarios
        for hora in HORARIOS:
            fila_texto = hora.ljust(10)

            for dia in DIAS:
                estado = dias[dia][hora]["estado"].upper()
                fila_texto += estado.ljust(12)

            print(fila_texto)

def elegir_oficina(oficinas):
    cant_ofis = len(oficinas)

    print("\nOficinas disponibles:")
    for i in range(1, cant_ofis + 1):
        print(i, "- Oficina", i)

    ofi = pedir_entero("Seleccione oficina: ", 1, cant_ofis)

    return "oficina_" + str(ofi)


def elegir_dia():
    print("\nDías disponibles:")
    for i in range(len(DIAS)):
        print(i + 1, "-", DIAS[i])

    dia = pedir_entero("Seleccione día: ", 1, len(DIAS))

    return DIAS[dia - 1]


def elegir_horario():
    print("\nHorarios disponibles:")
    for i in range(len(HORARIOS)):
        print(i + 1, "-", HORARIOS[i])

    hora = pedir_entero("Seleccione horario: ", 1, len(HORARIOS))

    return HORARIOS[hora - 1]


def obtener_datos_reserva(oficinas):
    ofi_key = elegir_oficina(oficinas)
    dia = elegir_dia()
    hora = elegir_horario()

    return ofi_key, dia, hora

def guardar_movimiento_csv(accion, oficina, dia, hora):
    try:
        archivo = open("movimientos.csv", "at")
        archivo.write(accion + ";" + oficina + ";" + dia + ";" + hora + "\n")

    except OSError as error:
        print("No se pudo guardar el movimiento en CSV:", error)

    finally:
        try:
            archivo.close()
        except NameError:
            pass

def crear_encabezado_csv():
    try:
        archivo = open("movimientos.csv", "rt")
        archivo.close()

    except FileNotFoundError:
        try:
            archivo = open("movimientos.csv", "wt")
            archivo.write("Accion;Oficina;Dia;Hora\n")

        except OSError as error:
            print("No se pudo crear el archivo CSV:", error)

        finally:
            try:
                archivo.close()
            except NameError:
                pass


def pedir_datos_clientes():
    nombre = input("Ingrese su nombre: ")
    while not nombre.isalpha():
        nombre = input("Ingrese su nombre: ")

    dni = input("Ingrese su dni: ")
    while not dni.isdigit() or len(dni) != 7:
        dni = input("Ingrese su dni: ")

    telefono = input("Ingrese su telefono: ")
    while not telefono.isdigit() or len(telefono) != 8:
        telefono = input("Ingrese su telefono: ")
    return nombre, dni, telefono


def codigo_existe(oficinas, codigo):
    for ofi_key in oficinas:
        for dia in DIAS:
            for hora in HORARIOS:

                if oficinas[ofi_key][dia][hora]["codigo"] == codigo:
                    return True
                
    return False
                
                
def generar_codigo(oficinas):
    codigo = random.randint(100000, 999999)
    if codigo_existe(oficinas, codigo):
        return generar_codigo(oficinas)
    return codigo
    

def cancelar_reserva(oficinas):
    ing_codigo = pedir_entero("Ingrese el codigo de su reserva: ",100000, 999999)
    
    for ofi_key in oficinas:
        for dia in DIAS:
            for hora in HORARIOS:

                if oficinas[ofi_key][dia][hora]["codigo"] == ing_codigo:
                    gestionar_reserva(oficinas, ofi_key, dia, hora, tipo="cancelar")
                    return
                
    print("El codigo de reserva es inexistente")


def gestionar_reserva(oficinas, ofi_key, dia, hora, tipo="reservar"):
    """Maneja tanto reservas como cancelaciones"""
    
    accion = "reservar" if tipo == "reservar" else "cancelar"
    
    print(f"\n--- FORMULARIO PARA {accion.upper()} ---")
    
    if tipo == "reservar":
        if oficinas[ofi_key][dia][hora]["estado"] ==  "libre":

            oficinas[ofi_key][dia][hora]["estado"] = "ocupado"

            nombre, dni, telefono = pedir_datos_clientes()
            codigo = generar_codigo(oficinas)

            oficinas[ofi_key][dia][hora]["cliente"] = nombre
            oficinas[ofi_key][dia][hora]["dni"] = dni
            oficinas[ofi_key][dia][hora]["telefono"] = telefono
            oficinas[ofi_key][dia][hora]["codigo"] = codigo

            guardar_oficinas(oficinas)
            guardar_movimiento_csv("RESERVA", ofi_key, dia, hora)

            print(f"\n ÉXITO: Oficina {ofi_key} reservada para el {dia} a las {hora}.")
            print(f" Su código de reserva es: {codigo}")  
        
        else:
            print(f"\n ERROR: El turno ya está ocupado por otro usuario.")

    else:
        if oficinas[ofi_key][dia][hora]["estado"] == "ocupado":

            oficinas[ofi_key][dia][hora]["estado"] = "libre"
            oficinas[ofi_key][dia][hora]["cliente"] = ""
            oficinas[ofi_key][dia][hora]["dni"] = ""
            oficinas[ofi_key][dia][hora]["telefono"] = ""
            oficinas[ofi_key][dia][hora]["codigo"] = ""

            guardar_oficinas(oficinas)
            guardar_movimiento_csv("RESERVA", ofi_key, dia, hora)

            print(f"\n ÉXITO: Reserva cancelada para el {dia} a las {hora}.")

        else:
            print(f"\n AVISO: No existía ninguna reserva en ese horario.")

def guardar_oficinas(oficinas):
    try:
        archivo = open("reservas.json", "wt")
        json.dump(oficinas, archivo)
        print("Datos guardados.")

    except OSError as error:
        print("No se pudo guardar el archivo:", error)

    finally:
        try:
            archivo.close()
        except NameError:
            pass

def cargar_datos_oficinas():
    try:
        archivo = open("reservas.json", "rt")
        return json.load(archivo)

    except FileNotFoundError:
        return None

    except json.JSONDecodeError:
        print("El archivo de reservas tiene un formato incorrecto.")
        print("Se iniciará un sistema nuevo.")
        return None

    except OSError as error:
        print("No se pudo leer el archivo:", error)
        return None
    
    finally:
        try:
            archivo.close()
        except NameError:
            pass
    
def datos_busqueda(oficinas):
    ofi_key = elegir_oficina(oficinas)
    dia = elegir_dia()

    return ofi_key, dia


def busqueda_disponibilidad(oficinas, ofi_key, dia, indice = 0):
    if indice == len(HORARIOS):
        return None
    
    if oficinas[ofi_key][dia][HORARIOS[indice]]["estado"] == "libre":
        return HORARIOS[indice]
    
    return busqueda_disponibilidad(oficinas, ofi_key, dia, indice + 1)

def menu():
    mostrar_guia()
    crear_encabezado_csv()
    
    datos_guardados = cargar_datos_oficinas()
    if datos_guardados is not None:
        oficinas = datos_guardados
        print(f"Se cargaron las reservas existentes")
    else:
        cant = pedir_entero("Con cuantas oficinas desea trabajar  hoy? (Maximo 5): ", 1, 5)
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
        print("5. Turno proximo libre")
        print("6. Salir")        
        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            mostrar_oficinas(oficinas)

        elif opcion == "2":
            ofi_key, dia, hora = obtener_datos_reserva (oficinas)
            gestionar_reserva(oficinas, ofi_key, dia, hora,"reservar")

        elif opcion == "3":
            cancelar_reserva(oficinas)

        elif opcion == "4":
            print("\nPara cambiar de turno, primero cancelaremos el actual y luego crearemos el nuevo.")
            cancelar_reserva(oficinas)
            ofi_key, dia, hora = obtener_datos_reserva(oficinas)
            gestionar_reserva(oficinas, ofi_key, dia, hora, "reservar")

        elif opcion == "5":
            ofi_key, dia = datos_busqueda(oficinas)
            resultado = busqueda_disponibilidad(oficinas, ofi_key, dia)

            if resultado is None:
                print(f"No hay disponibilidad en la oficina{ofi_key} para el dia {dia}")
            else:
                print(f"El proximo horario libre es a las {resultado}")

        elif opcion == "6":
            print("\n" + " Gracias por usar PrograReservas. Hasta pronto! ".center(60, "═"))
            break

        else:
            print("Opción no válida. Intente de nuevo.")
        
        input("\nPresione ENTER para volver al menú...")


menu()