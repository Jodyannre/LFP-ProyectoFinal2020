#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:10:46 2020

@author: Jo
"""
from reportes.Grafo import Grafo


class at2(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase relacionada a los autómatas tipo 2.
    __________________________________________________________________________________
    '''
    def __init__(self,nombre,terminales,nt,producciones):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que inicializa un nuevo at2.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = El nombre del at2.
        • estados = Lista de estados finitos del autómata.
        • alfabetoMaquina = Alfabeto que usará el autómata.
        • simbolosPila = Símbolos que usara la pila.
        • transiciones = Transiciones existentes en el autómata.
        • estadoI = Estado inicial.
        • estadosA = Estados de aceptación.
        • terminales = Lista de terminales de la gramática tipo 2.
        • producciones = LIsta de producciones de la gramática.
        __________________________________________________________________________________
        '''        
        self.nombre = nombre
        self.estados = ["I","P","Q","F"]
        self.alfabetoMaquina = []
        self.simbolosPila = ["#","S"]
        self.transiciones = ["I,Λ,Λ;P,#","P,Λ,Λ;Q,S"]
        self.estadoI = ["I"]
        self.estadosA = ["F"]
        self.__terminales=terminales
        self.__producciones=producciones
        self.__nt = nt
        self.grafica = ""
        self.agregarInformacion()
        self.agregarAlfabeto()
        self.agregarSimbolos()
        
    def get_simbolosPila(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna los símbolos de la pila.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.simbolosPila
    def get_estadoI(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna el estado inicial.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.estadoI
    def get_estadoA(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna los estados de aceptación.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.estadosA
    def get_transiciones(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna las transiciones.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.transiciones
    def get_estados(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna los estados.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.estados
    def get_alfabeto(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna el alfabeto.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.alfabetoMaquina
        
    def agregarInformacion(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de agregar información al autómata y al grafo correspondiente.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        '''  
        g = Grafo("Nuevo")
        g.agregar_datos2("I","P","-,-;#")
        g.agregar_datos2("P","Q","-,-;"+self.__producciones[0][0])
        g.agregar_datos2("Q","F","-,#;-")
        g.setEstadoInicial("I")
        g.setNodoAceptacion("F")
        lista = ""
        for i in self.__producciones:
            i = i.split(">")
            self.transiciones.append("Q,Λ,"+i[0]+";Q,"+i[1])
            #g.agregar_datos2("Q", "Q", "Λ,"+i[0]+";"+i[1])
            lista = lista+ "\n" + "-,"+i[0]+";"+i[1]
        for i in self.__terminales:
            self.transiciones.append("Q,"+i.getValor()+","+i.getValor()+";Q,Λ")
            #g.agregar_datos2("Q","Q",i.getValor()+","+i.getValor()+";Λ")
            lista = lista + "\n" + i.getValor()+","+i.getValor()+";-"
        g.agregar_datos2("Q","Q",lista)
        self.grafica = g
             
    
    def getGrafo(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna la gráfica del autómata.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        '''  
        return self.grafica
    
    def agregarAlfabeto(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de crear el alfabeto de la máquina.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        '''  
        for i in self.__terminales:
            self.simbolosPila.append(i.getValor())
            self.alfabetoMaquina.append(i.getValor())
    
    def agregarSimbolos(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de crear los símbolos del sistema.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        '''  
        for i in self.__nt:
            self.simbolosPila.append(i.getValor())
    def getNombre(self):
        return self.nombre
            
        