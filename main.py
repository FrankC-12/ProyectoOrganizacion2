from Hash import Hash_Function
from Juego import Juego

def registro(base_de_datos, indices):
    contador = 0
    while True:
        modelo = input("Introduzca el código del modelo: ")
        contador_num = 0
        contador_letra = 0
        for x in modelo:
            if x.isnumeric():
                contador_num += 1
            elif x.isalpha():
                contador_letra += 1
        while contador_letra != 6 or contador_num != 2 or (contador_letra + contador_num) != 8:
            print("Error, por favor ingrese un código válido")
            modelo = input("Introduzca el código del modelo: ")
            contador_num = 0
            contador_letra = 0
            for x in modelo:
                if x.isnumeric():
                    contador_num += 1
                elif x.isalpha():
                    contador_letra += 1
        break
    titulo = input("Ingrese el título del juego: ") 
    while len(titulo) > 10 or not titulo.isalpha() and not titulo.isnumeric():
        print("Error, el título no puede contener mas de 10 caracteres o no puede tener caracteres especiales")
        titulo = input("Ingrese el título del juego: ") 
    precio = input("Introduzca el precio del juego: ")
    while not precio.isnumeric() or int(precio) not in range(1,1000):
        print("Error, introduzca un precio válido")
        precio = input("Introduzca el precio del juego: ")

    hashing = Hash_Function(modelo)
    codigo = hashing.Hashing(modelo)

    overflow = 0
    status = "EN STOCK"

    data = open("Index.txt", "r")
    for x in data:
        i = 0
        if "\n" in x.split(",")[i+1]:
            x.split(",")[i+1] = x.split(",")[i+1].replace("\n", "")
        indices[x.split(",")[i]] = x.split(",")[i+1]
    indices[titulo] = contador
    data = open("Index.txt", "w")
    data.close()
    data = open("Index.txt", "a")
    print(indices)
    for x, y in indices.items():
        titulo = x
        data.write(f"{titulo},{contador}\n")
        contador += 1
    

    juego = Juego(codigo, titulo, precio, status, overflow)
    juego.database()

    if contador < 3:
        base_de_datos["primero"].append(juego)
        contador += 1
    elif contador < 6:
        base_de_datos["segundo"].append(juego)
        contador += 1
    else:
        base_de_datos["tercero"].append(juego)
        contador += 1






def buscar(base_de_datos, indices):
    opcion = input("Buscar por: \n1.Modelo \n2.Titulo \n> ")
    while not opcion.isnumeric() or int(opcion) not in range(1,3):
        print("Elija una opcion valida")
        opcion = input("Buscar por: \n1.Modelo \n2.Titulo \n> ")

    if opcion == "1":
        contador = 1
        data = open("Rent_A_Game.txt", "r")
        for x in data:
            i = 0
            if "\n" in x.split(",")[i+4]:
                x.split(",")[i+4] = x.split(",")[i+4].replace(",", "")
            juego = Juego(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4])
            if contador <= 3:
                base_de_datos["primero"].append(juego)
                contador += 1
            elif contador <= 6:
                base_de_datos["segundo"].append(juego)
                contador += 1
            else:
                base_de_datos["tercero"].append(juego)
                contador += 1
        while True:
            contador_num = 0
            contador_letra = 0
            modelo = input("Introduzca el código del modelo: ")
            for x in modelo:
                if x.isnumeric():
                    contador_num += 1
                elif x.isalpha():
                    contador_letra += 1
            while contador_letra != 6 or contador_num != 2 or (contador_letra + contador_num) != 8:
                print("Error, por favor introduzca un modelo valido")
                contador_num = 0
                contador_letra = 0
                modelo = input("Introduzca el código del modelo: ")
                for x in modelo:
                    if x.isnumeric():
                        contador_num += 1
                    elif x.isalpha():
                        contador_letra += 1
                

            hashing = Hash_Function(modelo)
            codigo = hashing.Hashing(modelo)

            encontrado = False
            for x, y in base_de_datos.items():
                for i in range(0, len(y)):
                    if codigo == y[i].modelo:
                        y[i].mostrar()
                        encontrado = True
            
            if encontrado != True:
                print("Error, no existe el modelo en la base de datos")
                opcion = input("Desea salir: \n1.Si \n2.No \n> ")
                while not opcion.isnumeric() or int(opcion) not in range(1,3):
                    opcion = input("Desea salir: \n1.Si \n2.No \n> ")
                if opcion == "1":
                    break
            else:
                break 
    else:
        base_de_datos = { "primero": [], "segundo": [], "tercero": []}
        contador = 1
        data = open("Rent_A_Game.txt", "r")
        for x in data:
            i = 0
            if "\n" in x.split(",")[i+4]:
                x.split(",")[i+4] = x.split(",")[i+4].replace(",", "")
            juego = Juego(x.split(",")[i],x.split(",")[i+1],x.split(",")[i+2],x.split(",")[i+3],x.split(",")[i+4])
            if contador <= 3:
                base_de_datos["primero"].append(juego)
                contador += 1
            elif contador <= 6:
                base_de_datos["segundo"].append(juego)
                contador += 1
            else:
                base_de_datos["tercero"].append(juego)
                contador += 1

        print(base_de_datos)

        while True:
            titulo = input("Ingrese el título del juego: ") 
            while len(titulo) > 10 or not titulo.isalpha() and not titulo.isnumeric():
                print("Error, el título no puede contener mas de 10 caracteres o no puede tener caracteres especiales")
                titulo = input("Ingrese el título del juego: ")
            
            data = open("Rent_A_Game.txt", "r")
            encontrado = False
            for x in data:
                print(x.split(",")[i+1])
                i = 0
                if x.split(",")[i+1] == titulo:
                    encontrado = True

            if encontrado != True:
                print("Error, no se encontro el titulo del juego")
            else:
                break
        
        data = open("Index.txt", "r")
        for x in data:
            i = 0
            if  x.split(",")[i] == titulo:
                if "\n" in x.split(",")[i+1]:
                    indice = x.split(",")[i+1].replace("\n", "")
        
        for x, y in base_de_datos.items():
            print(indice)
            juego_e = y[int(indice)]
            juego_e.mostrar()
            break

def mostrar(base_de_datos):
    for x, y in base_de_datos.items():
        for i in range(0, len(y)):
            print(y[i].modelo)
            print(y[i].titulo)
            print(y[i].precio)
            print(y[i].status)
            print(y[i].overflow)




base_de_datos = { "primero": [], "segundo": [], "tercero": []}
indices = {}
def main():
    print("Bienvenido al sistema de registro de Rent - A - Game")
    print()
    while True:
        opcion = input("Ingresa la operación que deseas realizar: \n1.Insertar un nuevo juego \n2.Búsqueda de un juego \n3.Alquiler de un juego \n4.Devolución de un juego \n5.Eliminación de un juego \n6.Salir \n>")
        while not opcion.isnumeric() or int(opcion) not in range(1,7):
            print("Por favor ingrese un número de opción válido")
            opcion = input("Ingresa la operación que deseas realizar: \n>1.Insertar un nuevo juego \n2.Búsqueda de un juego \n3.Alquiler de un juego \n4.Devolución de un juego \n5.Eliminación de un juego \n6.Salir \n> ")
        if opcion == "1":
            registro(base_de_datos,indices)
        elif opcion == "2":
            buscar(base_de_datos,indices)
        elif opcion == "3":
            mostrar(base_de_datos)
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        else:
            break
main()