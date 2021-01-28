#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:56:33 2021

@author: juancarlosholguinsotomayor
"""


#Zip method
print("######## Zip method #########")
lista_nombres = ["Juan","Luis","Maria", "Luis"]
lista_apellidos = ["Holguin", "Holguin", "Sotomayor", "Zazueta"]

names = zip(lista_nombres, lista_apellidos)

print(names)
for i in names:
    print(i)
    
#Count method
print("\n######## Count method #########")
lista_contar = ["Rojo", "Azul", "Rosa", "Amarillo", "Negro", "Azul"]
quantity = lista_contar.count("Azul")
print(quantity)

#Index method
print("######## Index method #########")
lista_index = [1,6,3,4,5,6,7,8,9,10,11,12,13,14,15,16,6]
el_index = lista_index.index(6)
print(el_index)

#Reverse method
print("######## Reverse method #########")
lista_to_reverse = ["Juan", "Carlos", "Holguin", "Sotomayor"]
lista_to_reverse.reverse()
print(lista_to_reverse)

#Sort method
print("######## Sort method #########")
list_to_sort = [5,7,1,10,2,3]
list_to_sort.sort()
print(list_to_sort)

#Copy Method
print("######## Copy method #########")
lista1 = ["Juan","Carlos","Holguin","Sotomayor"]
lista2 = lista1.copy()
lista2.pop()
print(lista2)
















