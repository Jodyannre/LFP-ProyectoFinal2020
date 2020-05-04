#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:54:53 2020

@author: Jo
"""




class NodoA(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase encargada de definir los nodos usados por las gramáticas tipo 2.
    __________________________________________________________________________________
    '''
    __contador = 0
    def __init__(self,valor):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que crea nuevos nodos A destinados a utilizarlos en graphviz.            
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = El nombre del nodo.
        • valor = El valor asignado al nodo.
        • label = El label que se encargará de generar un elemento en graphviz.
        • creacion = Verifica si el nodo ya existe.
        • asignacion = Verifica si el nodo ya esta asignado.
        • contador (estática) = Contador destinado a generar id's.
        __________________________________________________________________________________
        '''  
        self.__nombre = self.__setId()
        self.__valor = valor
        self.__label = self.__nombre+" [label="+"\""+self.__valor+"\"] ;"
        self.__creacion = self.__nombre+" ;"
        self.__asignacion = False
        
    def __setId(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna los símbolos de la pila.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        NodoA.__contador+=1
        return "n"+str(NodoA.__contador)
    def setAsignacion(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna los símbolos de la pila.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        self.__asignacion = True
    def getNombre(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna los símbolos de la pila.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.__nombre
    def getValor(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna los símbolos de la pila.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.__valor
    def getLabel(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna los símbolos de la pila.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.__label
    def getCreacion(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna los símbolos de la pila.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.__creacion
    def getAsignacion(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna los símbolos de la pila.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.__asignacion

n = NodoA("S")
