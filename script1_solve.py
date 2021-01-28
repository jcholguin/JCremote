#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:56:30 2021

@author: juancarlosholguinsotomayor
"""


"""
1) Implement a function that uses list slicing to reverse the list 'numbers'
numbers = [1, 2, 3, 4, 5]
"""
numbers = [1, 2, 3, 4, 5]
words = ["Carlos", "Pepe", "Jose", "Juan", "Holguin"]

def reverse(lista):
    return lista[::-1]

lista2 = list(map(lambda lista: lista[::-1], words))
print("Lista 2:", lista2)

#lista = reverse(numbers)
#print(lista)