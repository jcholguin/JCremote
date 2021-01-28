#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:58:29 2021

@author: juancarlosholguinsotomayor
"""
import sys

#Lists
thislist = ["Juan", "Carlos", "Holguin"]
print("Lista sin nada: ", thislist)

thislist.append("Sotomayor")
print("Lista cambio append: ", thislist)

thislist.insert(0,"27 Nov")
print("Lista cambio insert 0: ", thislist)

thislist.remove("Holguin")
print("Lista cambio remove: ", thislist)

thislist.pop()
print("Lista cambio pop: ", thislist)

thislist2 = list(thislist)
print(thislist)
print(thislist2)

thislist.extend("hola")
print(thislist)
print(thislist2)

thislist.clear()
print(thislist, thislist2)

thislist3 = [letter for letter in 'CASA']
print(thislist3)

text = "Juan,Carlos,Holguin"
list_nombres = [word for word in text]
print(list_nombres)
list_nombres2 = text.split(",")
list_nombres4 = text.split()
print(list_nombres2)
print(list_nombres4)

print("Esta lista: ", list_nombres2)
print(list_nombres2[0])
list_nombres2[0] = "Luis"
print("Esta lista: ", list_nombres2)
print(list_nombres2[0])


""" Pending """
list_mix = []

#Tuple
print("################## Tuple #######################")
thistuple = ("Juan", "Carlos", "Holguin")
thistuple2 = ("Luis", "Alonso", "Holguin")
print(thistuple[1])
#thistuple[1] = "hola"
list1 =  list(thistuple)
list1.insert(100, "Sotomayor")
thistuple = tuple(list1)
print(thistuple)
thistuple3 = thistuple + thistuple2
print(thistuple3)

#Set
listt = [3,4,5]
print("################## Set #######################")
thisset = {1,2,"Carlos",(3,4,5), "Carlos"}
print("1)",thisset)

thisset.add("Holguin")
print("2)",thisset)

thisset.update(["Juan", "Sotomayor"])
print("3)",thisset)

thisset.remove("Carlos")
print("4)",thisset)

thisset.discard("exe")
print("5)",thisset)

thisset.pop()
print("6)",thisset)

thisset.pop()
print("7)",thisset)

thisset.pop()
print("8)",thisset)

#Dictionary
print("################## Dict #######################")
thisdict = {"nombre":"Juan", "apellido":"Holguin", 0:"Sotomayor"}
print(thisdict)
print(thisdict["apellido"])
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

value1 = thisdict["nombre"]
print(value1)
value2 = thisdict.get("nombre")
print(value2)

thisdict["nombre"] = "Carlos"
print(thisdict)

thisdict.pop("nombre")
print(thisdict)

thisdict["dia"] = 27
print(thisdict)

for i in thisdict:
    print("Primer for: ",i)
    
for i in thisdict.keys():
    print("Segundo for: ",i)

for i in thisdict.values():
    print("Tercer for: ",i)
    
for i in thisdict.items():
    print("Cuarto for: ",i)
    
for n, i in enumerate(thisdict):
    print("Quinto for: ",n, i)

#General Porposes
print(3 + 5)

print(3**2)

print(3/2)

print(3//2)

print(10%2)

print(3/2)
print(round(7/4))

print("Hola mundo")
print("Hola \t mundo")
print("Hola \n mundo")
print("Hola 'que pedo' mundo")
print("C:\nombre\directorio")
print(r"C:\nombre\directorio")

print("""
Juan
Carlos
Sotomayor""")

print(("n" * 5),"hola")

#Slicing
palabra = "Python"
print(palabra)
palabra = "J"+palabra[:0:-1]
print(palabra)

palabra = "Python es un lenguaje de programacion"
print(palabra[::-1])

print(len(palabra))

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = [a,b,c]
print(d[2][1])
"""
input2 = int(input("Escribe algo: "))
print(type(input2))
print(input2**2)
"""

tuple33 = (100, 'Hola', [1,2,3], {4,5,6}, {"n":7})
print(tuple33)
print(tuple33[2][-1])

list34 = [1,1,2,2,3,3,4,4,5,5]
list34 = list(set(list34))
print(list34)

dict35 = {1:"ey",2:"como",3:"estai"}
for key, value in dict35.items():
    print(f"The key is {key} and the value is {value}")

list_texto = []
for n, i in enumerate(dict35):
    list_texto.append(dict35[n+1])

print(" ".join(list_texto))

#sys library

if len(sys.argv) == 3:
    print("El archivo se llama ", sys.argv[0])
    print("Primer argumento ", sys.argv[1])
    print("Segundo argumento ", sys.argv[2])

else:
    print("Argumentos insuficientes, tienen que ser 2")
    
    
def area_cuadrado(base, altura):
    return base*altura

square1 = area_cuadrado(5, 6)
print(square1)

def function1(a=4, b=8):
    return b//a

num1 = function1()
print(num1)
print("#######################################")

"""
def receive(a):
    b = a[0:1]
    return b

str1 = "Juan"
list1 = ["Juan","Carlos","Holguin"]

proof1 = receive(str1)
proof2 = receive(list1)

print(str1)
print(list1)
"""

def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

indeterminados_posicion(5,"Hola",[1,2,3,4,5],6,7,8)


def indeterminados_nombre(**kwargs):
    print(kwargs)

indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5])  

def test(num):
    return num*2, num*10, num*1

print(type(test(5)))


#Funcion Recursiva
def cuenta(num):
    num -=1
    
    if num > 0:
        print(num)
        cuenta(num)
    else:
        print("Boooooom!")
        
cuenta(5)

#Funcion Recursiva 2
def factorial(num):
    print("Valor inicial ->", num)
    
    if num > 1:
        num = num * factorial(num-1)
    print("Valor final ->", num)
    
    return num

l = factorial(5)
print("El factorial es: ",l)

n = "10"
print(n)
n = int("10")
print(n)


"""
try:
    option = int(input("Escribe un numero: "))
    pordiez = option * 10
    print(f"Tu numero es {option} y se puede multiplicar por 10: {pordiez}")
except Exception as e:
    print("Ha ocurrido un error no previsto", type(e).__name__)
else:
    print("si pudiste, entro al else")
finally:
    print("al finally siempre entra")


option = int(input("Escribe un numero: "))
pordiez = option * 10
print(f"Tu numero es {option} y se puede multiplicar por 10: {pordiez}")
"""
"""
try:
    n = float(input("Introduce un número divisor: "))
    5/n
except TypeError:
    print("No se puede dividir el número entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e:
    print("Ha ocurrido un error no previsto", type(e).__name__ )
"""

def mi_funcion(a=None):
    if a == None:
        raise ZeroDivisionError("Error")
    else:
        print("Hola")
        
#mi_funcion()
        
##Funcion Lambda (funcion anonima)
print("################ Funcion lambda ################")
def doblar(num):
    return num*2

num1 = doblar(6)
print(num1)

doblar2 = lambda num : num*2
num2 = doblar2(7)
print(num2)

revertir = lambda cadena : cadena[::-1]
cadena1 = revertir("anita lava la tina")
print(cadena1)

##Funcion Generadora
print("################ Funcion generadora ################")
lista = [1,2,3,4,5,6]
lista_iterable = iter(lista)
numero = lista_iterable
next(lista_iterable)
numero = lista_iterable


#Funcion Filter
print("################ Funcion filter ################")
numeros = [3,6,50,44,45,80,33,66,300]

def multiplos(num):
    if num % 3 == 0:
        return True
    
filter(multiplos, numeros)
print(list(filter(multiplos, numeros)))

#Combinar lambda con filter
print(list(filter(lambda num : num % 3 == 0, numeros)))

#Funcion map
print("################ Funcion Map ################")
a = [1,10,20,100,1000]
b = [5,6,7,8,9]

lista = map(lambda x,y: x*y, a,b)
print(list(lista))













































