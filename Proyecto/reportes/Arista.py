#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 24/03/2020

@author: Jo
'''

class Arista(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase que maneja las aristas que contiene cada objeto Nodo.
    __________________________________________________________________________________
    '''  

    def __init__(self, inicial,final,valor):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de crear objetos Arista.                 
        __________________________________________________________________________________
        ► Parámetros:
        
        • inicial = el valor inicial de la Arista.
        • final = la dirección a donde se dirige la Arista.
        • valor = el valor con que se dirige la Arista del inicial al final.
        __________________________________________________________________________________
        ► Variables:
        
        • self.nodo_inicial = Toma el valor del parámetro inicial.
        • self.nodo_final = Toma el valor del parámetro final.
        • self.valor = Toma el valor del parámetro valor.
        __________________________________________________________________________________
        '''
        self.nodo_inicial = inicial
        self.nodo_final = final
        self.valor = valor     
        
        
    def get_nodoInicial(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna el valor inicial de la Arista.                 
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________

        
        '''
        return self.nodo_inicial
    def get_nodoFinal(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna el nodo final de la Arista.                 
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        return self.nodo_final
    def get_valor(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna el valor que contiene la Arista.                
        __________________________________________________________________________________
        ► Parámetros:

            (Sin parámetros)
        __________________________________________________________________________________
        '''
        return self.valor