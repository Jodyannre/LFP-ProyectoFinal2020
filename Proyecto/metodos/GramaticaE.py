#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:23:09 2020

@author: Jo
"""
from nodos.NodoL import NodoL
from tipos.Tipo import Tipo
from metodos.at2 import at2
import os



class GramaticaE(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase relacionada a la nueva gramática tipo 2.
    __________________________________________________________________________________
    '''
    __nodoTemporal = ""
    
    def __init__(self,nombre):
        '''
        __________________________________________________________________________________
        ► Parámetros:
        
        • nombre = el nombre del objeto asignado a la nueva instancia.
        __________________________________________________________________________________
        ► Variables:
        
        • self.nombre = Recibe el valor de la nueva gramática tipo 2.
        • self.nt =  Lista que guarda los no terminales de la gramática.
        • self.terminales = Lista que guarda los terminales de la gramática.
        • self.ntInicial = Lista que guarda el nt inicial de la gramática.
        • self.producciones =  Lista que guarda las producciones ingresadas..
        
        ► Estáticas:
        
        • prueba = Patrón utilizado por el módulo re para el ingreso de datos.
        • patronGramar = Patrón utilizado por el módulo re para el ingreso de datos.
        • patronGramar2 =  Patrón utilizado por el módulo re para el ingreso de datos.
        • patronGramar3 = Patrón utilizado por el módulo re para el ingreso de datos.        
        __________________________________________________________________________________
        '''
        self.nombre = nombre
        self.terminales = []
        self.nt = []
        self.producciones = []
        self.ntInicial = ""
        self.automata = ""
        
    def ingreso_terminales(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de solicitar y guardar los terminales.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        while (True):
            os.system("cls")
            print('Ingrese el terminal:')
            print(">> ", end="")
            terminal = input() 
            if terminal == "":
                print("Enter para finalizar.")
                input()
                break
            elif not terminal.isupper():
                if self.repetido(1,terminal):
                    print('Terminal repetido.')
                    input()
                else:
                    nuevo = NodoL(terminal,Tipo.TERMINAL)
                    self.terminales.append(nuevo)
            else:
                print("Error, los terminales no pueden ser letras mayúsculas.")
                input()
        
    def ingreso_nt(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de solicitar y guardar los no terminales de la gramática.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        while (True):
            os.system("cls")
            print('Ingrese el no terminal:')
            print(">> ", end="")
            nt = input() 
            if nt == "":
                print("Enter para finalizar.")
                input()
                break
            elif nt[0].isupper():
                if self.repetido(0,nt):
                    print('No terminal repetido.')
                    input()
                else:
                    nuevo = NodoL(nt,Tipo.NOTERMINAL)
                    self.nt.append(nuevo)
            else:
                print("Error, los no terminales son ID con mayúscula inicial.")
                input()
                
                
    def ingreso_ntInicial(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de solicitar y guardar el nt Inicial.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        while (True):
            os.system("cls")
            print('Ingrese el inicial deseado:')
            print(">> ", end="")
            inicial = input() 
            if inicial =="":
                print("Enter para finalizar la operación.")
                input()
                break
            elif inicial[0].isupper():
                if self.repetido(0,inicial):
                    self.ntInicial = self.getNodo(inicial)
                    print("No terminal inicial asignado.")
                    print("Enter para continuar.")
                    input()
                    break
                else:
                    print ("El símbolo: ",inicial," no existe en el lenguaje \
                    \n Intentelo de nuevo con otro NT que exista.")
                    input()
            else:
                print("Error, el NT inicial tiene que ID e iniciar con mayúscula.")
                input()
                
    def ingreso_producciones(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de solicitar y guardar las producciones.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        while(True):
            os.system("cls")
            print('Ingrese la producción deseada:')
            print(">> ", end="")
            produccion = input() 
            if produccion == "":
                print("Enter para finalizar.")
                input()
                break
            if not ">" in produccion:
                print("Producción no válida.")
                input()
            else:
                produccion = produccion.replace(" ","")
                padre = produccion.split(">")
                hijo = padre[1]
                padre = padre[0]
                if self.repetido(0,padre) and self.validarExistencia(hijo):
                    self.producciones.append(produccion)
                    try:
                        if len(hijo)>1:
                            self.getNodo(padre).agregarHijo(self.listaHijos(hijo))
                    except ValueError as er:
                        self.getNodo(padre).agregarHijo(self.getNodo(hijo))
                        print (er) #Imprimir el error
                else:
                    print("Producción inválida, elementos inexistentes en la gramática")
                    input()
        print(self.producciones)
        print(self.nt[0].getHijo())

    def eliminar_producciones(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de eliminar producciones ingresadas anteriormente.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''         
        while(True):
            os.system("cls")
            print('Ingrese la producción a eliminar:')
            print(">> ", end="")
            produccion = input() 
            produccion = produccion.replace(" ","")
            if produccion == "":
                print("Enter para finalizar.")
                input()
                break
                
            else:
                if produccion in self.producciones:
                    self.producciones.remove(produccion)
                    produccion = produccion.split(">")
                    padre = produccion[0]
                    hijo = produccion[1]
                    padre = self.getNodo(padre)
                    padre.eliminarHijo(hijo)
                else:
                    print("Esa producción no existe.")
                    input()
            
        
                
    def repetido(self,tipo,valor):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que valida si el elemento ingresado ya existe en la gramática.             
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • tipo = Tipo del elemento, ya sea nt o terminal.
        • valor = Valor ingresado.
        __________________________________________________________________________________
        '''
        validar = False
        if tipo == 1:
            validar = self.recorrerLista(self.terminales,valor)
        elif tipo ==0:
            validar = self.recorrerLista(self.nt,valor)
        else:
            print()
        return validar
        
    def recorrerLista(self,lista,valor):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que recorre listas y valida la existencia de un elemento en ellas.             
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • lista = Lista a recorrer.
        • valor = Valor a validar.
        __________________________________________________________________________________
        '''
        for i in lista:
            #global __nodoTemporal
            if i.getValor() == valor:
                #__nodoTemporal = i #Toma el valor del nodo encontrado y existente.
                return True
            else:
                continue
        return False
    
    def validarExistencia(self,lista):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que valida la existencia de los elementos de la producción ingresada.             
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • lista = Lista de producciones ingresadas.
        __________________________________________________________________________________
        '''
        nt = False
        t = False
        for i in lista:
            nt = self.recorrerLista(self.nt,i)
            t = self.recorrerLista(self.terminales,i)
            if not nt and not t:
                return False
            else:
                nt = False
                t = False
                continue
        return True
    
    def setNombre(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que cambia el nombre de la gramática.            
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = El nuevo nombre para la gramática
        __________________________________________________________________________________
        '''
        self.nombre = nombre
    
    def getNombre(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna el nombre de la gramática.           
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • (Sin parámetros)
        __________________________________________________________________________________
        '''        
        return self.nombre
            
    def listaHijos(self,hijos):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que convierte el texto ingresado en una lista de nodos.          
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • hijos: Los hijos que tendrá la producción.
        __________________________________________________________________________________
        ''' 
        lista = []
        for i in hijos:
            lista.append(self.getNodo(i))
        return lista
            
    def getNodo(self,valor):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna el nodo buscado.           
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • valor: El valor guardado por el nodo buscado.
        __________________________________________________________________________________
        ''' 
        for i in self.nt:
            if i.getValor()==valor:
                return i
        for i in self.terminales:
            if i.getValor()==valor:
                return i
        return False
    
    def crearAutomata(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de crear el autómata para la gramática.           
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        self.automata = at2(self.nombre,self.terminales,self.nt,self.producciones)
        
    def getAutomata(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna el autómata de la gramática.          
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.automata
        
        
    
    def agregarDatos_Masivo(self,nombre,lista):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de agregar datos cargados de forma masiva.             
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre: El nombre de la gramática.
        • lista: La lista de producciones.           
        __________________________________________________________________________________
        '''
        self.nombre = nombre
        for i in lista:
            self.producciones.append(i)
            i = i.split(">")
            padre = i[0]
            hijo = i[1]
            if not self.repetido(0,padre):
                self.nt.append(NodoL(padre,Tipo.NOTERMINAL))
            for j in hijo:
                nodo = self.getNodo(j)
                if nodo==False and not j.isupper():
                    self.terminales.append(NodoL(j,Tipo.TERMINAL))
                elif j.isupper():
                    nodo = self.getNodo(j)
                    if nodo == False:
                        self.nt.append(NodoL(j,Tipo.NOTERMINAL))
            try:
                if len(hijo)>1:
                    self.getNodo(padre).agregarHijo(self.listaHijos(hijo))
                else:
                    self.getNodo(padre).agregarHijo([self.getNodo(hijo)])
            except ValueError as er:
                self.getNodo(padre).agregarHijo(self.getNodo(hijo))
                print (er) #Imprimir el error
        #for i in self.terminales:
            #print(i.getValor())
        #for i in self.nt:
            #print(i.getValor())
        #print (self.producciones)
        self.ntInicial = self.nt[0]
    
    def getInicial(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna el nt inicial.             
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        return self.ntInicial
        
        
                    
                    
                    
            
            
        
        
        
    
    