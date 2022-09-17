from colas.cola import Cola
import os, sys, time

cola = Cola()

def cls():
    os.system("cls")

def menu():
    cls()
    while True:
        print("""****** Menu Principal ******
        
        1. Ingresar una Orden
        2. Entregar una Orden
        3. Mostrar Ordenes
        4. Datos del Estudiante
        5. Salir""")

        opc = input("Ingrese opción: ")

        if opc == "1":
            cls()
            print("*** Bienvenido a Hot Dog Rapidog ***")
            x = input("Ingrese el ingrediente de su Hog dog: ")
            cola.push(x)
            input("Hot Dog agregado a la orden...")
            menu()
            break
        if opc == "2":
            cls()
            print("*** Entregar Orden ***\n")
            cola.first()
            confirm = input("Confirmar orden Si/No: ")

            if confirm.lower().strip() == "si":
                cola.pop()
                menu()
            else:
                menu()
            break
        if opc == "3":
            cls()
            print("*** Ordenes de Hot Dog ingresadas al sistema ***\n")
            cola.mostrar()
            input("Presione una tecla para continuar...")
            menu()
            break
        if opc == "4":
            cls()      
            print("\n           Datos estudiante               \n")     
            print("**********************************************")
            print("****                IPC 2                 ****")
            print("****              Sección N               ****")
            print("****                                      ****")
            print("****      Ing. en Ciencias y sistemas     ****")
            print("****    Henry Alexander García Montúfar   ****")
            print("****              201407049               ****")
            print("**********************************************\n")

            input("Presione una tecla para continuar...")
            menu()
            break
        if opc == "5":
            cls()
            print("Saliendo del sistema...")
            time.sleep(0.5)
            os.system("exit")
            break
        else:
            print("\nOpcion inorrecta...")
            time.sleep(0.5)
            cls()
            menu()
            break

menu()