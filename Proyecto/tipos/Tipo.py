#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 21/03/2020

@author: Jo
'''

class Tipo(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase estática que maneja los tipos de la clase Nodo.
    __________________________________________________________________________________
    '''  
    NOTERMINAL = 0
    TERMINAL = 1
    ESTADO = 2
    SIMBOLO = 3
    EPSILON = 4


    def __init__(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Clase estática.                
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ► Variables estáticas:
        
        • NOTERMINAL = Tipo del nodo no terminal.
        • TERMINAL = Tipo del nodo terminal.
        • ESTADO = Tipo del nodo estado.
        • SIMBOLO = Tipo del Nodo simbolo.
        • EPSILON = Tipo del nodo épsilon.
        __________________________________________________________________________________
        '''
        