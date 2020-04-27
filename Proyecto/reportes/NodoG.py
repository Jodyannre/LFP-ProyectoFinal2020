#!/usr/bin/python
# -*- coding: utf-8 -*-

from reportes.Arista import Arista

class NodoG(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Nodo especialmente preparado para el manejo de gráficos con la libreria graphviz.
    __________________________________________________________________________________
    '''


    def __init__(self, nombre):
        '''
        __________________________________________________________________________________
        ► Parámetros:
        
        • nombre = el nombre del objeto asignado a la nueva instancia.
        __________________________________________________________________________________
        ► Variables:
        
        • self.nombre = El nombre representativo del objeto NodoG.
        • self.lista_aristas =  la lista de todas las aristas pertenecientes al NodoG.
        • self.inicial = El estado del NodoG, referente a si es un nodo inicial.
        __________________________________________________________________________________
        '''
        self.nombre = nombre
        self.lista_aristas = []
        self.inicial = False

    def crearArista(self, nodo_final, valor):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de crear las aristas del nodo.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nodo_final: El nodo dirección.                                                    
        • valor: El valor que tendrá asociados el nodo actual al nodo dirección.            
        __________________________________________________________________________________
        '''
        self.lista_aristas.append(Arista(self, nodo_final, valor))  
        
    def get_nombre(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Retorna el nombre del objeto NodoG.                 
        __________________________________________________________________________________    

        '''
        return self.nombre
    def get_listaAristas(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Retorna la lista de aristas que pertenecen al objeto NodoG.                 
        __________________________________________________________________________________    
        '''
        return self.lista_aristas
    def get_inicial(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Retorna el estado inicial del NodoG.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nodo_final: El nodo dirección.                                                    
        • valor: El valor que tendrá asociados el nodo actual al nodo dirección.            
        __________________________________________________________________________________
        '''
        return self.inicial
    def set_nombre(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Asigna un nombre al atributo self.nombre del objeto NodoG.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre: el nombre se configurará en el objeto.                                                             
        __________________________________________________________________________________
        '''
        self.nombre = nombre
    def set_inicial(self,inicial):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Asigna un estado referente al atributo self.inicial al objeto.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • inicial: booleano que representa al estado self.inicial del NodoG.                                                          
        __________________________________________________________________________________
        '''
        self.inicial = inicial