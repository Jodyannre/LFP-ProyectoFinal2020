# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:13:14 2020

@author: Jo
"""


class NodoL(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase relacionada a nodos para la gramática tipo 2.
    __________________________________________________________________________________
    '''
    def __init__(self,valor,tipo):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que crea un nuevo NodoL                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • valor = Valor que guardará el nodo.
        • tipo = El tipo del valor guardado.
        __________________________________________________________________________________
        '''
        self.valor = valor
        self.hijos = []
        self.tipo = tipo
        
    def eliminarHijo(self,hijo):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de eliminar hijos del nodoL.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • hijo = El hijo a eliminar en formato de texto.
        __________________________________________________________________________________
        '''
        validar = 0
        for i in self.hijos:
            if len(hijo) == len(i):
                for j in range(0,len(i)):
                    if hijo[j]==i[j].getValor():
                        validar+=1
                    else:
                        break
                if len(hijo)==validar:
                    self.hijos.remove(i)
                    return ""
        return False

    
    def agregarHijo(self,hijo):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que agrega hijos al nodo.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • hijo = Lista de hijos a agregar al nodo.
        __________________________________________________________________________________
        '''
        self.hijos.append(hijo)
        
    def getHijo(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la lista de hijos del nodo.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.hijos
    
    def getValor(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna el valor guardado en el nodo.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.valor
    def getTipo(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna el tipo del valor guardado en el nodo.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.tipo
    