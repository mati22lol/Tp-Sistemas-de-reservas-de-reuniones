#LISTAS DE ALMACENAMIENTO PARA MATRICES

"""Los datos siempre seran los mismos asi que se guardan en listas"""
dia = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
horarios = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"]


#FUNCIONES QUE NECESITA EL PROGRAMA

def crear_oficinas(cant_ofis, lista_dia, lista_horarios): #Los dias van a ser de lunes a viernes (5 dias) y los horarios de 10am hasta 10pm (12 horarios)
    """Crea la cantidad de oficinas que se disponen segun el numero que se ingrese para crear sus matrices de cada una"""
    oficinas = []
    for i in range(cant_ofis):
        matriz = []
        for f in range(len(lista_horarios)):
            filas = []
            for columnas in range(len(lista_dia)):
                filas.append(0)
            matriz.append(filas)
        oficinas.append(matriz)
    return oficinas



def mostrar_oficinas(oficinas, lista_dia, lista_horarios):  #Mostrar las oficinas con 0 (libre) y 1 (ocupada)

    print("Oficina / Horario / Dias")

    for ofi in range(len(oficinas)):           # Recorre cada oficina disponible
        print(f"\nOficina {ofi + 1}")          # Muestra el número de oficina (sumamos 1 para que comience desde 1 lo que vamos a mostrar)
    
        print("        ", end="")              # Espaciado inicial para alinear el encabezado de días con la tabla
        for d in lista_dia:                    # Recorre la lista de días para mostrarlos como columnas de la tabla
            print(d, end="   ")
        print()

        for h in range(len(lista_horarios)):             # Recorre cada horario disponible (cada fila de la matriz)
            print(lista_horarios[h], end="     ")        # Muestra el horario actual como etiqueta de fila

            for d in range(len(lista_dia)):               # Recorre cada día dentro del horario actual para esa oficina
                print(oficinas[ofi][h][d], end="         ")
            
            print()




def reservar(oficinas, list_dia, lista_horarios):    #Si esta libre reserva, y si esta ocupada que avise
    selec_ofi = int(input("Que ofica quiere reservar: "))
    while selec_ofi < 0 or selec_ofi >= len(oficinas):
        print("error, vuelva a intentarlo")
        selec_ofi = int(input("Que ofica quiere reserva: "))

    selec_dia = input("Que dia quiere reservar: ")
    while selec_dia not in list_dia:
        print("error, vuelva a intentarlo")
        selec_dia = input("Que dia quiere reservar: ")

    selec_hora = input("Que horario quiere reservar: ")
    while selec_hora not in lista_horarios:
        print("error, vuelva a intentarlo")
        selec_hora = input("Que horario quiere reservar: ")

    dia_index = list_dia.index(selec_dia)                 #Aca creamos una variable para tener la posicion exacta de dia y hora que eligio el que reserva
    horario_index = lista_horarios.index(selec_hora)

    if oficinas[selec_ofi][horario_index][dia_index] == 0:   #lo que pasa aca es que, si en la lista de oficinas, en la posicion del horario que se eligio, y la posicion del dia que se eligio
        oficinas[selec_ofi][horario_index][dia_index] = 1    # Se va a fijar si esta libre (hay un 0), si lo esta, cambia el 0 por un 1, pero en cambio si esta ocupada (1), no entra al if.
        print(f"Reserva realizada para el {selec_dia} a las {selec_hora} en la oficina {selec_ofi}")
    
    else:
        print(f"Ya hay una reserva para el {selec_dia} a las {selec_hora} en la oficina {selec_ofi}") 
    
    return oficinas





def cancelar_oficina(oficinas, list_dia, lista_horarios):
    selec_ofi = int(input("Que ofica quiere cancelar: "))
    while selec_ofi < 0 or selec_ofi >= len(oficinas):
        print("error, vuelva a intentarlo")
        selec_ofi = int(input("Que ofica quiere cancelar: "))               
                                                                            
    selec_dia = input("Que dia quiere cancelar: ")                         #Me parecio que lo mejor era hacerlo como el de reservas, solo que en este caso lo haria al revez 
    while selec_dia not in list_dia:                                       
        print("error, vuelva a intentarlo")
        selec_dia = input("Que dia quiere cancelar: ")

    selec_hora = input("Que horario quiere cancelar: ")
    while selec_hora not in lista_horarios:
        print("error, vuelva a intentarlo")
        selec_hora = input("Que horario quiere cancelar: ")
    
    dia_index = list_dia.index(selec_dia)
    horario_index = lista_horarios.index(selec_hora)                  #Volvemos a buscar por los valores de posicion en las que estan

    if oficinas[selec_ofi][horario_index][dia_index] == 1:            #Pero esta vez si esta en uno, que remplace el 1 por 0
        oficinas[selec_ofi][horario_index][dia_index] = 0
        print(f"Se cancelo el turno para la oficina {selec_ofi} a las {selec_hora} el dia {selec_dia}")
    
    else:                                                                                                           #Y en caso contrario, que avise que no hizo cambios
        print(f"No hay turno reservado para la oficina {selec_ofi}, a las {selec_hora} para el dia {selec_dia}")





def mostrar_libres(oficinas, lista_dia, lista_horario):

    for ofi in range(len(oficinas)):
        print(f"Oficina {ofi + 1}")
        
        for dia in range(len(lista_dia)):
            print(f"{lista_dia[dia]}:")
            for hora in range(len(lista_horario)):
                if oficinas[ofi][hora][dia] == 0:
                    print(f"{lista_horario[hora]} ", end="")
            print()
        print()


def buscar_disponibilidad(oficinas, lista_dia, lista_horarios):
    selec_dia = input("Que dia quiere reservar: ")
    while selec_dia not in lista_dia:
        print("error, vuelva a intentarlo")
        selec_dia = input("Que dia quiere reservar: ")

    selec_hora = input("Que horario quiere reservar: ")
    while selec_hora not in lista_horarios:
        print("error, vuelva a intentarlo")
        selec_hora = input("Que horario quiere reservar: ")

    dia_index = lista_dia.index(selec_dia)                 #Aca creamos una variable para tener la posicion exacta de dia y hora que eligio el que reserva
    horario_index = lista_horarios.index(selec_hora)

    for ofi in range(len(oficinas)):
        if oficinas[ofi][horario_index][dia_index] == 0: 
            print(f"Hay disponibilidad para tu dia y horario en la oficina {ofi + 1}")
            
        
        else:
            print("Para este dia y horario ya esta todo reservado")
            



def menu(): #Programa principal
    can_ofis = int(input("Cuantas oficinas hay: "))                #pedimos cuantas oficinas quiere crear

    while can_ofis < 1 or can_ofis > 3:                            #hacemos que no ponga ningun dato fuera de rango          ahora es de 1 a 3 pero la idea es sumar mas funciones
        print("Error vuelva a intentar, maximo 5")
        can_ofis = int(input("Cuantas oficinas hay: "))

    oficinas = crear_oficinas(can_ofis, dia, horarios)             #Creamos las oficinas con la funcion que creeamos
    
    while True:
        print()
        print("-" * 25)
        print("PROGRAMA DE RESERVAS DE OFICINAS")
        print("-" * 25)
        print("1. Mostrar los turnos")
        print("2. Reservar alguna oficina")
        print("3. Cancelar turno")
        print("4. Mostrar turno libres")
        print("5. Buscar disponibilidad")
        print("6. Salir del programa")

        opcion = int(input("Ingrese la opcion: "))                 #Creamos otro bucle para hacer el menu y pueda elegir la opcion (funcion que quiere realizar)
        while opcion < 1 or opcion > 5:
            print("Error, vuelva a intentarlo")
            opcion = int(input("Ingrese la opcion: "))

        print("")
        
        if opcion == 1:
            mostrar_oficinas(oficinas, dia, horarios)              #Elige opcion 1, va a mostrar las oficinas y sus reservas, utiliza la funcion que creamos
        
        elif opcion == 2:
            reservar(oficinas, dia, horarios)                      #Si elige la opcion 2, va a poder reservar en alguna de las oficinas

        elif opcion == 3:
            cancelar_oficina(oficinas, dia, horarios)

        elif opcion == 4:
            mostrar_libres(oficinas, dia, horarios)

        elif opcion ==5:
            buscar_disponibilidad(oficinas, dia, horarios)

        elif opcion == 6:
            print("Saliendo del programa, gracias por su reserva")   
            break
        
        print("")
        input(" Presiones enter para entrar al menu")
        print("/n /n")

menu()