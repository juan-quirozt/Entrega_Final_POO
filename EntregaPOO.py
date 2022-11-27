print("¿Que deseas hacer?")
print("1. Ingresar un contacto")
print("2. Consultar un contacto")
print("3. Eliminar un contacto")
print("4. Modificar un contacto")
criterio = int(input("Seleccione su opcion: "))


##########################################################################
    #INGRESAR UN CONTACTO
##########################################################################

if criterio == 1:

    archivo = open('pruebas.txt', 'a')
     
    num_agregar = int(input("¿Cuantos contactos desea agregar? "))

    for i in range(num_agregar):
        identificacion = input("Ingrese la Identificacion: ")   #Se piden los datos por pantalla
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")

        contacto = identificacion + " " + nombre + " " + apellido     #Se genera el string con los esos datos                                      
        archivo.write(contacto + "\n")  #AQUÍ SE ESCRIBE EN EL txt
        print("El contacto ha sido agregado")
        
        if i < (num_agregar - 1):
            print("\nSiguiente contacto")

    archivo.close()
    

##########################################################################
    #CONSULTAR UN CONTACTO
##########################################################################

if criterio == 2:

    archivo = open('pruebas.txt', 'r')
    datos = archivo.read().splitlines()
    
    print("\n¿Por que criterio desea buscar?")
    print("1. Buscar por identificacion")
    print("2. Buscar por nombre")
    print("3. Buscar por apellido")
    print("4. Buscar por identificacion nombre apellido")
    print("5. Buscar por identificacion nombre")
    print("6. Buscar por identificacion apellido")
    print("7. Buscar por nombre apellido")
    tipo_busqueda = int(input("Seleccione su opcion: "))

    if tipo_busqueda == 1:
        
        contador = 0
        busqueda = input("Ingrese la identificacion del contacto a buscar: ")

        for renglon in datos:
            c = renglon.split()
            if busqueda == c[0]:
                print(renglon)
                contador += 1
        if contador == 0:
            print("No se encontro el contacto")

        
    if tipo_busqueda == 2:

        contador = 0
        busqueda = input("Ingrese el nombre del contacto a buscar: ")

        for renglon in datos:
            c = renglon.split()
            if busqueda == c[1]:
                print(renglon)
                contador += 1
        if contador == 0:
            print("No se encontro el contacto")

        
    if tipo_busqueda == 3:

        contador = 0
        busqueda = input("Ingrese el apellido del contacto a buscar: ")

        for renglon in datos:
            c = renglon.split()
            if busqueda == c[2]:
                print(renglon)
                contador += 1
        if contador == 0:
            print("No se encontro el contacto")
        

    if tipo_busqueda == 4:

        contador = 0
        busqueda = input("Ingrese identificacion nombre apellido del contacto a buscar: ")

        for renglon in datos:
            c = renglon.split()
            if busqueda.split() == c:
                print(renglon)
                contador += 1
        if contador == 0:
            print("No se encontro el contacto")

                
    if tipo_busqueda == 5:

        contador = 0
        busqueda = input("Ingrese identificacion nombre del contacto a buscar: ")

        for renglon in datos:
            c = renglon.split()
            comparar = busqueda.split()
            if comparar[0] == c[0] and comparar[1] == c[1]:
                print(renglon)
                contador += 1
        if contador == 0:
            print("No se encontro el contacto")


    if tipo_busqueda == 6:

        contador = 0
        busqueda = input("Ingrese identificacion apellido del contacto a buscar: ")

        for renglon in datos:
            c = renglon.split()
            comparar = busqueda.split()
            if comparar[0] == c[0] and comparar[1] == c[2]:
                print(renglon)
                contador += 1
        if contador == 0:
            print("No se encontro el contacto")

    if tipo_busqueda == 7:

        contador = 0
        busqueda = input("Ingrese nombre apellido del contacto a buscar: ")

        for renglon in datos:
            c = renglon.split()
            comparar = busqueda.split()
            if comparar[0] == c[1] and comparar[1] == c[2]:
                print(renglon)
                contador += 1
        if contador == 0:
            print("No se encontro el contacto")
            
    archivo.close()
    
##########################################################################
    #ELIMINAR UN CONTACTO
##########################################################################
            
if criterio == 3:
    
    archivo = open('pruebas.txt', 'r')
    datos = archivo.read().splitlines()
                
    print("\n¿Por que criterio desea eliminar?")
    print("1. Eliminar por identificacion")

    tipo_busqueda = int(input("Seleccione su opcion: "))

    if tipo_busqueda == 1:
        
        contador = 0
        busqueda = input("Ingrese la identificacion del contacto a eliminar: ")

        i = 0
        for renglon in datos:
            c = renglon.split()
            if busqueda == c[0]:
                bandera = i
                contador += 1
                break
            i += 1
        if contador == 0:
            print("No se encontro el contacto")
            
        archivo.close()
    if contador != 0:        
        


        with open(r"pruebas.txt", 'r+') as archivo:
            
            ##AQUÍ SE PROCEDE A BORRAR EL ARCHIVO CUANDO YA SE IDENTIFICO
            datos = archivo.readlines()
            archivo.seek(0)
            archivo.truncate()
            for number, line in enumerate(datos):
                if number != i:
                    archivo.write(line)
            print("El contacto ha sido eliminado")
        archivo.close()


##########################################################################
    #ELIMINAR UN CONTACTO
##########################################################################


if criterio == 4:
    
    archivo = open('pruebas.txt', 'r')
    datos = archivo.read().splitlines()
                
    print("\n¿Por que criterio desea modificar?")
    print("1. Modificar por identificacion nombre apellido")

    tipo_busqueda = int(input("Seleccione su opcion: "))

    if tipo_busqueda == 1:
        
        contador = 0
        busqueda = input("Ingrese identificacion nombre apellido del contacto a modificar: ")

        i = 0
        for renglon in datos:
            c = renglon.split()
            if busqueda.split() == c:
                bandera = i
                contador += 1
                break
            i += 1
        if contador == 0:
            print("No se encontro el contacto")
            
        archivo.close()
        
    if contador != 0:        
        modificado = input("Ingrese, ahora modificado, este contacto: ")


        with open(r"pruebas.txt", 'r+') as archivo:
            
            ##AQUÍ SE PROCEDE A MODIFICAR EL ARCHIVO CUANDO YA SE IDENTIFICO
            datos = archivo.readlines()
            archivo.seek(0)
            archivo.truncate()
            for number, line in enumerate(datos):
                if number != i:
                    archivo.write(line)
                else:
                    archivo.write(modificado + "\n")
            print("El contacto ha sido modificado")
        archivo.close()
            

