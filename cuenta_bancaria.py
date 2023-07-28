import os
import re

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    
class Cliente(Persona):
    
    def __init__(self, nombre, apellido, num_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.apellido}, {self.nombre}\nNumero de cuenta: {self.num_cuenta}\nBalance: ${self.balance}"

    def depositar(self, dinero):
        self.balance += dinero

    def retirar(self, dinero):
        if self.balance >= dinero:
            self.balance -= dinero
            print("Operación exitosa.")
        else:
            print("Fondos insuficientes.")
        

def imprimir_menu():
    print("\n***\tCUENTA BANCARIA\t***")
    print("-------------------------\n")
    print("1) Depositar")
    print("2) Retirar")
    print("3) Salir")


def elegir_opcion():
    while True:
        opcion = input("Elija una opcion: ")
        try:
            opcion = int(opcion)
            if opcion in range(1, 4):
                break
            else:
                print("Esa opción no está disponible. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

    return opcion

def crear_cliente():
    nombre_cliente = input("Ingrese su nombre: ")
    while not re.match(r"[^\s\d]+", nombre_cliente):
        nombre_cliente = input("Error. Ingrese su nombre nuevamente: ")
    apellido_cliente = input("Ingrese su apellido: ")
    while not re.match(r"[^\s\d]+", apellido_cliente):
        apellido_cliente = input("Error. Ingrese su apellido nuevamente: ")
    cuenta_cliente = int(input("Ingrese su número de cuenta: "))
    cliente = Cliente(nombre_cliente, apellido_cliente, cuenta_cliente)
    
    return cliente

def elegir_monto():

    print("Opciones: \n")
    print("1) 500")
    print("2) 1000")
    print("3) 2000")
    print("4) 5000")
    print("5) 10000")
    print("6) Otro monto")
    while True:
        opcion = input("Elija una opcion: ")
        try:
            opcion = int(opcion)
            if opcion in range(1, 7):
                break
            else:
                print("Esa opción no está disponible. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

    match opcion:
        case 1:
            monto = 500
        case 2:
            monto = 1000
        case 3:
            monto = 2000
        case 4:
            monto = 5000
        case 5:
            monto = 10000
        case 6:
            monto = int(input("Ingrese el monto a retirar: "))

    return monto

def ejecutar_programa():
    seguir = "s"
    mi_cliente = crear_cliente()

    while seguir == "s":
        os.system("cls")
        print(mi_cliente)
        imprimir_menu()
        match elegir_opcion():
            case 1:
                os.system("cls")
                monto = int(input("Ingrese el monto a depositar: "))
                mi_cliente.depositar(monto)
            case 2:
                os.system("cls")
                monto = elegir_monto()
                mi_cliente.retirar(monto)
                os.system("pause")
            case 3:
                seguir = "n"
                os.system("cls")
                print("Muchas gracias!")

ejecutar_programa()