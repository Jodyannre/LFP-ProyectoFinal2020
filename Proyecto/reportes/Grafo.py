#!/usr/bin/python
# -*- coding: utf-8 -*-

from graphviz import Digraph
from reportes.Arista import Arista
from reportes.NodoG import NodoG

class Grafo(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase destinada al manejo de imágenes y creación de las mismas.
    __________________________________________________________________________________
    '''    

    def __init__(self, nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de crear los objetos aristas del nodo.                 
        __________________________________________________________________________________
        ► Parámetros:
        
        • nombre = el nombre del objeto asignado a la nueva instancia.
        • nodos = La lista de nodos que contendrá el grafo.
        • nodos_aceptacion = La lista de nodos que pertenecen al estado de aceptación.
        __________________________________________________________________________________
        '''
        self.nombre = nombre
        self.nodos = []
        self.nodos_aceptacion = []

    def agregarNodo(self, nodo):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de agregar nodos a la lista self.nodos.                 
        __________________________________________________________________________________
        ► Parámetros:
        
        • nodo = el nodo a agregar en la lista self.nodos del objeto Grafo.
        __________________________________________________________________________________
        '''        
        self.nodos.append(nodo)
    
    def obtenerNodo(self, nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de retornar el nodo buscado.                
        __________________________________________________________________________________
        ► Parámetros
        
        • nombre = el nombre representativo del objeto Nodo buscado.
        __________________________________________________________________________________
        '''       
        for n in self.nodos:
            if n.get_nombre() == nombre:
                return n
        return False

    def setNodoAceptacion(self, nombre):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de establecer los nodos con estado de aceptación.
        __________________________________________________________________________________
        ► Parámetros
        
        • nombre = el nombre representativo del objeto nodo.
        __________________________________________________________________________________
        '''        
        self.nodos_aceptacion.append(self.obtenerNodo(nombre))

    def esAceptacion(self, nombre):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de retornar una validación referente al estado de aceptación
            de un nodo.
        __________________________________________________________________________________
        ► Parámetros:
        
        • nombre = el nombre representativo del objeto Nodo a validar.
        __________________________________________________________________________________
        '''        
        for n in self.nodos_aceptacion:
            if n.get_nombre() == nombre:
                return True
        
        return False
    
    def setEstadoInicial(self, nombre):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de establecer el nodo inicial del Grafo.
        __________________________________________________________________________________
        ► Parámetros:
        
        • nombre = el nombre representativo del objeto nodo a establecer.
        __________________________________________________________________________________
        '''        
        self.obtenerNodo(nombre).inicial = True
    
    def getEstadoInicial(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna el nodo con el estado inicial = True.
        __________________________________________________________________________________
        ► Variables: 
        
            (Sin parámetros)
        __________________________________________________________________________________
        '''        
        for n in self.nodos:
            if n.inicial:
                return n
        return None

    def graficar(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de graficar la información en formato pdf.
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        '''        
        f = Digraph(format='png', name='Grafo_Automata')
        f.attr(rankdir='LR', size='8,5')
        f.attr('node', shape='circle')

        for n in self.nodos:
            
            if not self.esAceptacion(n.get_nombre()):
                f.node(n.get_nombre())


        f.attr('node', shape='doublecircle')


        for n in self.nodos_aceptacion:
            f.node(n.get_nombre())

        for arista in self.nodos:
            for a in arista.get_listaAristas():
                f.edge(arista.get_nombre(), a.get_nodoFinal().get_nombre(), label=a.get_valor())

        
        # ------------------ estado inicial ------------------
        f.attr('node', shape='none')
        f.attr('edge', arrowhead='empty', arrowsize='1.5')
        
        f.edge('', self.getEstadoInicial().get_nombre(), None)

        f.render()
        # ----------------------------------------------------------
        
    def agregar_datos(self,transiciones,nt,terminales,ntA,ntI):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de agregar todos los datos del AFD a graficar.
        __________________________________________________________________________________
        ► Parámetros:
        
        • transiciones = lista de transiciones.
        • nt =  lista de no terminales.
        • terminales = Lista de terminales.
        • ntA = Estados de aceptación.
        • ntI = Estado inicial.
        __________________________________________________________________________________
        '''        
        for i in nt:
            self.agregarNodo(NodoG(i))
        for i in transiciones:
            i = i.replace(";",",")
            i = i.split(",")
            if i[1]!= "-" and i[2]!= "-":
                self.obtenerNodo(i[0]).crearArista(self.obtenerNodo(i[1]),i[2])
            elif i[1]== "-" and i[2]!="-":
                self.agregarNodo(NodoG(i[0]+"F"))
                self.obtenerNodo(i[0]).crearArista(self.obtenerNodo(i[0]+"F"),i[2])
                ntA.append(i[0]+"F")
        self.setEstadoInicial(ntI)
        for i in ntA:
            self.setNodoAceptacion(i)
            
    def agregar_datos2(self,estadoI,estadoF,transicion):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de agregar todos los datos del AFD a graficar.
        __________________________________________________________________________________
        ► Parámetros:
        
        • transiciones = lista de transiciones.
        • nt =  lista de no terminales.
        • terminales = Lista de terminales.
        • ntA = Estados de aceptación.
        • ntI = Estado inicial.
        __________________________________________________________________________________
        '''        
        nodoI = self.obtenerNodo(estadoI)
        nodoF = self.obtenerNodo(estadoF)
        
        if nodoI == False:
            self.agregarNodo(NodoG(estadoI))
        if nodoF == False:
            self.agregarNodo(NodoG(estadoF))
        self.obtenerNodo(estadoI).crearArista(self.obtenerNodo(estadoF),transicion)

    
    
            





