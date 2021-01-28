#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 22:21:49 2021

@author: juancarlosholguinsotomayor
"""
variable1 = []
from io import open
fichero2 = open('fichero.txt', 'w')
fichero = open('fichero.txt', 'r')

text = "Como estas"
fichero2.write(text)
"""
texto = fichero.read()
print("Read: ", texto)
"""
fichero.seek(0)
texto2 = fichero.readline()
print("Readline: ", texto2)
"""
texto3 = fichero.readlines()
print("Readlines: ", texto3)
"""
fichero2.close()
fichero.close()



