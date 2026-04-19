dia = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
horarios = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"]


#FUNCIONES QUE NECESITA EL PROGRAMA

def crear_oficinas(cant_ofis, lista_dia, lista_horarios): #Los dias van a ser de lunes a viernes (5 dias) y los horarios de 10am hasta 10pm (12 horarios)
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

    for ofi in range(len(oficinas)):
        print(f"\nOficina {ofi + 1}")
    
        print("        ", end="")
        for d in lista_dia:
            print(d, end="   ")
        print()

        for h in range(len(lista_horarios)):
            print(lista_horarios[h], end="     ")

            for d in range(len(lista_dia)):
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



#def cancelar_oficina(oficinas):


#def mostrar_libres(oficinas):



def menu(): #Programa principal
    can_ofis = int(input("Cuantas oficinas hay: "))                #pedimos cuantas oficinas quiere crear

    while can_ofis < 1 or can_ofis > 3:                            #hacemos que no ponga ningun dato fuera de rango          ahora es de 1 a 3 pero la idea es sumar mas funciones
        print("Error vuelva a intentar, maximo 5")
        can_ofis = int(input("Cuantas oficinas hay: "))

    oficinas = crear_oficinas(can_ofis, dia, horarios)             #Creamos las oficinas con la funcion que creeamos
    
    while True:
        print()
        print("PROGRAMA DE RESERVAS DE OFICINAS")
        print()
        print("1. Mostrar los turnos de nuestras oficinas")
        print("2. Reservar alguna oficina")
        print("3. Salir del programa")

        opcion = int(input("Ingrese la opcion: "))                 #Creamos otro bucle para hacer el menu y pueda elegir la opcion (funcion que quiere realizar)
        while opcion < 1 or opcion > 5:
            print("Erro, vuelva a intentarlo")
            opcion = int(input("Ingrese la opcion: "))
        
        if opcion == 1:
            mostrar_oficinas(oficinas, dia, horarios)              #Elige opcion 1, va a mostrar las oficinas y sus reservas, utiliza la funcion que creamos
        
        elif opcion == 2:
            reservar(oficinas, dia, horarios)                      #Si elige la opcion 2, va a poder reservar en alguna de las oficinas

        elif opcion == 3:
            print("Saliendo del programa, gracias por su reserva")   
            break

menu()