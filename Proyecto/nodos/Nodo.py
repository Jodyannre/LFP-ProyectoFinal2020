#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 21/03/2020

@author: Jo
'''

class Nodo(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase que maneja los Nodos con información de los lenguajes, los AFD y las gra-
        máticas.
    __________________________________________________________________________________
    ''' 


    def __init__(self,valor,tipo):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de crear objetos Nodo.                 
        __________________________________________________________________________________
        ► Parámetros:
        
        • valor = la información que almacenará el objeto Nodo.
        • tipo = Tipo que tendrá el objeto Nodo.
        __________________________________________________________________________________
        ► Variables:
        
        • self.valor = Toma el valor del parámetro valor.
        • self.tipo = Toma el valor del parámetro tipo.
        • self.estadoA = Variable que lleva el control de los nodos con estados de acepta-
            ción.
        __________________________________________________________________________________
        '''
        self.valor = valor
        self.tipo = tipo
        self.estadoA = False
        
        
        
    def get_valor(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Retorna la información almacenada por el Nodo.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        return self.valor
    def get_tipo(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Retorna el tipo del Nodo.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        return self.tipo
    def get_estadoA(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Retorna el booleano que valida el estado de aceptación del Nodo.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        return self.estadoA
    def set_estadoA(self,estado):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Asigna un valor a la variable self.estadoA del Nodo.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • estado: Recibe un estado a configurar como estado de aceptación.                                                              
        __________________________________________________________________________________
        '''
        self.estadoA = estado
        