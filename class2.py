#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:48:24 2021

@author: juancarlosholguinsotomayor
"""


class Mother:
    contenedor_objetos_hijos = []
    
    def __init__(self, ID, nombre, edad, telefono):
        self.ID = ID
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        print(f"""
        \t Se ha creado un usuario:
        Tu ID es: {self.ID}
        Nombre:   {self.nombre}""")
    
    def __str__(self):
        return f"Soy un objeto o heredo de la clase Mother\n"
    
    def imprimir(self):
        pass
    
    def proof(self):
        print(f"Total de Attributos {len(self.__dict__.keys())}")
    
class Child1(Mother):
    def __init__(self, ID, nombre, edad, telefono, casa):
        super().__init__(ID, nombre, edad, telefono)
        self.casa = casa
        
    def __str__(self):
        return super().__str__() + f"Soy un objeto de la clase Child1 y mi attributo unico es {self.casa}"
    
    def imprimir(self):
        print(f"Child1: {self.nombre}")
    
    def proof(self):
        option = input("Que metodo quieres usar, 1)Superclase, 2)Clase local: ")
        if option == '1':
            super().proof()
        elif option == '2':
            print("Si imprimo esto es que estoy llamando al metodo local")
        else:
            print("No existe esa opcion")
    
class Child2(Mother):
    def __init__(self, ID, nombre, edad, telefono, departamento):
        super().__init__(ID, nombre, edad, telefono)
        self.departamento = departamento
        
    def __str__(self):
        return super().__str__() + f"Soy un objeto de la clase Child2 y mi attributo unico es {self.departamento}"
    
    def imprimir(self):
        print(f"Child2: {self.nombre}")
    
class Child3(Mother):
    def __init__(self, ID, nombre, edad, telefono, hotel):
        Mother.__init__(self,ID, nombre, edad, telefono)
        self.hotel = hotel
    
    def __str__(self):
        return Mother.__str__(self) + f"Soy un objeto de la clase Child3 y mi attributo unico es {self.hotel}"
    
    def imprimir(self):
        print(f"Child3: {self.nombre}")

objeto1 = Mother("001", "Juan", 20, "31255751")
objeto2 = Child1("002", "Carlos", 21, "3317897538", "casa1")
objeto3 = Child2("003", "Holguin", 22, "3312402423", "departamento1")
objeto4 = Child3("004", "Sotomayor", 23, "3345678923", "hotel1")

objeto1.contenedor_objetos_hijos.extend([objeto2,objeto3,objeto4])

for n, i in enumerate(objeto1.contenedor_objetos_hijos):
    #print(f"{n})\n{i}")
    i.imprimir()

print("########################################")

#print(objeto4.contenedor_objetos_hijos)
objeto2.proof()

        
        
        
        