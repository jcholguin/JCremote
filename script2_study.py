#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:43:21 2021

@author: juancarlosholguinsotomayor
"""

print("############## Lists ################")
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

print("############## Strings ################")

#center()
print("####### center() ######")
string = "Carlos"
string = string.center(20)
print(string, len(string))

#find()
print("####### find() ######")
string = "Juan Carlos"
string = string.find("n")
print(string)

#isalnum()
print("####### isalnum() ######")
string = "los4tigres"
if string.isalnum():
    print("all are alphanumeric")

#isalpha()
print("####### isalpha() ######")
string = "lostigres"
if string.isalpha():
    print("all are in the alphabet")

#isdecimal()
print("####### isdecimal() ######")
string = "31255751"
if string.isdecimal():
    print("all are decimals")
    
#isnumeric()
print("####### isnumeric() ######")
string = "31255751"
if string.isnumeric():
    print("all are numeric")
    
#zfill()
print("####### zfill() ######")
txt = "50"
x = txt.zfill(20)
print(x)