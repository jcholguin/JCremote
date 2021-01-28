#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:07:13 2021

@author: juancarlosholguinsotomayor
"""
"""
1) Implement a function that uses list slicing to reverse the list 'numbers'
numbers = [1, 2, 3, 4, 5]
"""
numbers = [1, 2, 3, 4, 5]

def reverse(lista):
    return lista[::-1]

#lista2 = list(filter(lambda lista:lista[::-1], numbers))
#print("Lista 2:", lista2)

lista = reverse(numbers)
#print(lista)


"""
2) Implement a function to check if a word is a palindrome.
"""
phrase = "anita lava la tina"
phrase2 = "el perro sigue al carro"
phrase3 = "Amore, Roma"

def check_palindrome(phrase):
    """
    phrase_tmp = phrase.strip()
    print(phrase_tmp)
    """
    phrase = phrase.lower()
    print(phrase)
    
    lista_tmp = [letra for letra in phrase]
    phrase = phrase[::-1]
    lista2_tmp = [letra for letra in phrase]
    """
    print(lista_tmp)
    print(lista2_tmp)
    """
    #counter =  0
    for n, i in enumerate(lista_tmp):
        if i == ' ':
            del(lista_tmp[n])
        lista_tmp.remove(',')
        """    
        elif i == ',':
            del(lista_tmp[n])
        """
            
            
    for n, i in enumerate(lista2_tmp):
        if i == ' ':
            del(lista2_tmp[n])
        lista2_tmp.remove(',')
        """    
        elif i == ',':
            del(lista2_tmp[n])
        """
            
    
    print(lista_tmp)
    print(lista2_tmp)
    
            

    if lista_tmp == lista2_tmp:
        print("La frase es un palindromo")
    else:
        print("La frase no es un palindromo")

#check_palindrome(phrase3)
        
        
        
"""
3) What is the output of the following code?
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
"""

#44
"""
try:
    print(4 + 7)
except TypeError:
    print("2")
except Exception:
    print("3")
else:
    print("si entro a try")
finally:
    print("4")
"""
"""
class A:
    def method(self):
        print(1)
        
class B(A):
    def method(self):
        A.method(self)
        #print(2)
        
B().method()
"""

"""
class B:
    
    def __init__(self, time, var):
        self.time = time
        self.var = var
        print(f"{self.var} {self.time}")

class A(B):
    letter_var = 'A'
    number_3 = 3
    
    def __init__(self, time, var=None, some_var=True, time_out=None):
        B.__init__(self,time, var)
        self.var = some_var
        self.time = time_out
        self.letter = self.letter_var
        self.number = self.number_3

objeto1 = A(5, "esto")
"""

"""
8) The email_list function receives a dictionary,
which contains domain names as keys, and a list of 
users as values. Develop a script to generate a list 
that contains complete email addresses (e.g. diana.prince@gmail.com).


Use the following call to function and dictionary:
print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon",
 "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
"""
"""
def email_list(dictionary):
    lista = []
    for k, v in dictionary.items():
        for i in v:
            lista.append(i+'@'+ k)
    return lista

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
"""

"""
9) Given a list of filenames, we want to rename all the files with the extension 
    hpp to the extension h by generating a list of tuples of the form (old_name, new_name).
    

That is, given the following list of filenames
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
Generate the following newfilenames list of tuples:
newfilenames = [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]

"""
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out", "algo.mp3"]

def rename(lista):
    lista_temp = []
    for i in lista:
        if '.hpp' in i:
            i2 = i.replace('.hpp','.h')
            tuple1 = (i,i2)
            lista_temp.append(tuple1)
        else:
            tuple1 = (i,i)
            lista_temp.append(tuple1)
            
    return lista_temp

print(rename(filenames))



    




























    
    
    
    
    