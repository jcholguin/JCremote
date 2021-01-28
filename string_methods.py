#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 12:55:32 2021

@author: juancarlosholguinsotomayor
"""

#capitalize()
print("####### capitalize() ######")
string = "Juan Carlos Holguin Sotomayor"
string = string.capitalize()
print(string)

#casefold()
print("####### casefold() ######")
string = "Juan Carlos Holguin Sotomayor"
string = string.casefold()
print(string)

#center()
print("####### center() ######")
string = "Carlos"
string = string.center(20)
print(string, len(string))

#encode()    ??????
print("####### encode() ######")
string = "Juan Carlos"
string = string.encode()
print(string)

#endswith()
print("####### endswith() ######")
string = "Juan Carlos"
if string.endswith('los'):
    print("el ultimo nombre termina con \'los\'")

#expandtabs()   ???????
print("####### expandtabs() ######")
string = "Juan Carlos"
string = string.expandtabs(15)
print(string)

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

#isdigit()
print("####### isdigit() ######")
string = "31255751"
if string.isdigit():
    print("all are digits")

#isidentifier()
print("####### isidentifier() ######")
string = "31255751"
if string.isidentifier():
    print("is identifier")

#islower()
print("####### islower() ######")
string = "juancarlos"
if string.islower():
    print("all are in lower case")
    
#isnumeric()
print("####### isnumeric() ######")
string = "31255751"
if string.isnumeric():
    print("all are numeric")

#isprintable()
print("####### isprintable() ######")
string = "juancarlos"
if string.isprintable():
    print("all are printable")

#isspace()
print("####### isspace() ######")
string = "    "
if string.isspace():
    print("all are whitespaces")

#istitle()
print("####### istitle() ######")
string = "La Caperusita Roja"
if string.istitle():
    print("is a title")

#isupper()
print("####### isupper() ######")
string = "JUAN CARLOS"
if string.isupper():
    print("all are upper cases")

#maketrans()
txt = "Hello Sam!";
mytable = txt.maketrans("S", "P");
print(txt.translate(mytable));

#partition()
print("####### partition() ######")
string = "Juan Carlos Holguin"
string = string.partition('Carlos')
print(string)

#splitlines()
print("####### splitlines() ######")
string = "Juan Carlos \nHolguin"
string = string.splitlines()
print(string)

#startswith()
print("####### startswith() ######")
string = "Juan Carlos"
if string.startswith('Jua'):
    print("el ultimo nombre termina con \'Jua\'")

#strip()    ????
print("####### strip() ######")
string = "Juan Carlos Holguin"
string = string.strip()
print(string)

#swapcase()
print("####### swapcase() ######")
string = "Juan Carlos Holguin"
string = string.swapcase()
print(string)

#title()
print("####### title() ######")
string = "juan carlos holguin"
string = string.title()
print(string)

#translate()
print("####### translate() ######")
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80};
txt = "Hello Sam!";
print(txt.translate(mydict));

#upper()
print("####### upper() ######")
string = "juan carlos holguin"
string = string.upper()
print(string)

#zfill()
print("####### zfill() ######")
txt = "50"
x = txt.zfill(20)
print(x)


