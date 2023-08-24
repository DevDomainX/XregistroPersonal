#!/usr/bin/env python3
from Xbaner import logo
from colorama import init, Style, Fore
init()
"""Author: Hans Saldias

   Created by: un 1lugarparaprogramar"""

global lista

lista = list()

class Persona():
    pass
    def __init__(self):
        nombre = " "
        rut = " "
        edad = 0
        direccion = " "
   
def registrarPersona():
    x = Persona()
    x.nombre = input("Nombre: ")
    x.rut = input("Rut: ")
    x.edad = input("Edad: ")
    x.direccion = input("Direccion: ")
    lista.append(x)

def listar():
   
   for x in lista:
       print(f"Nombre: {x.nombre}\nRut: {x.rut}\nEdad: {x.edad}\nDireccion: {x.direccion}\n\n")
      
def buscarPersona():
    rut = input("Ingrese rut a buscar: ")
    for x in lista:
        if rut == x.rut:
            print(f"Nombre: {x.nombre}\nRut: {x.rut}\nEdad: {x.edad}\nDireccion: {x.direccion}\n\n")
        
def guardarPersona():
       for x in lista:
           with open("lista.txt", "a") as c:
               c.write(f"Nombre: {x.nombre}\nRut: {x.rut}\nEdad: {x.edad}\nDireccion: {x.direccion}\n\n")
       
def salir():
    print("Muchas gracias por usar mi script")
   
def menu():
    while True:
        logo()
        print(Style.BRIGHT+Fore.WHITE+"""
    
    [1]  agregar persona
    
    [2] ver lista de personas 
    
    [3] buscar persona
    
    [4] Guardar
    
    [0] Salir
    
        """)
        op = input("Ingrese opcion: ")
        if op == "1":
            registrarPersona()
        elif op == "2":
            listar()
        elif op == "3":
            buscarPersona()
        elif op == "4":
            guardarPersona()
        elif op == "0":
            salir()
            break
        else:
            print("opcion, invalida")
            menu()
menu()
        