#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:57:48 2020

@author: Jo
"""

from metodos.pila import pila
from tipos.Tipo import Tipo
from nodos.NodoA import NodoA
from graphviz import render


class EvaluarT2(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase relacionada a la validación de gramáticas de tipo 2.
    __________________________________________________________________________________
    '''
    def __init__(self,gramatica,cadena):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que inicializa un nuevo objeto de validación.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • gramatica = La gramática que se utilizará para validar la cadena ingresada.
        • cadena = Cadena ingresada por el usuario para su validación.
        • tabla = Tabla generada por las acciones realizadas en la pila.
        • pilaTemp = Pila que contiene los valores de los nodos utilizados en la validación.
        • NodosA = Nodos accedidos por el validador en la búsqueda de validar la cadena.
        • arbol = Árbol generado por la cadena de entrada.
        __________________________________________________________________________________
        '''  
        
        self.automata = gramatica
        self.cadena = cadena
        self.tabla = ["PILA$ENTRADA$TRANSICIÓN","Λ$"+self.cadena+"$I,Λ,Λ;P,#",\
                      "#$"+self.cadena+"$P,Λ,Λ;Q,"+self.automata.getInicial().getValor()]
        self.pilaTemp = ["#",self.automata.getInicial().getValor()]
        self.NodosA = []
        self.arbol = ""
        
        
    def evaluar(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de evaluar la cadena ingresa con la gramática seleccionada.
        __________________________________________________________________________________
        ► Parámetros:
        
        • (Sin parámetros)
        __________________________________________________________________________________
        '''  
        stack = pila()
        stack.push("#")
        stack.push(self.automata.getInicial())
        for i in range(0,len(self.cadena)):
            avanzar = False
            while not avanzar:
                leido = False
                #encontrado = False
                #hijo = False
                ultimo = stack.pop()
                #self.pilaTemp.pop()
                try:
                    print()
                    #print (ultimo.getValor())
                except Exception as ex:
                    print (ex)
                    print (ultimo)
                while not leido:
                    if ultimo == "#":
                        self.crearTabla(self.pilaTemp,self.cadena[i:],"Fallido",None)
                        self.guardar(self.tabla)
                        #print(self.getArbol())
                        self.drawArbol()
                        return "Cadena inválida"
                    elif ultimo.getTipo()== Tipo.NOTERMINAL:
                        hijos = ultimo.getHijo()
                        for j in hijos:
                            if j[0].getTipo() == Tipo.TERMINAL:
                                if self.cadena[i] == j[0].getValor():
                                    son = self.hijoAtexto(j)
                                    self.crearTabla(self.pilaTemp,self.cadena[i:],ultimo.getValor(),son)
                                    self.pilaTemp.pop()
                                    for k in reversed(j):
                                        stack.push(k)
                                        self.pilaTemp.append(k.getValor())
                                    self.crearArbol(ultimo, j)
                                        
                                    leido = True  
                                    #son = self.hijoAtexto(j)
                                    #self.crearTabla(self.pilaTemp,self.cadena[i:],ultimo.getValor(),son)
                                    
                                    break
                        if not leido:
                            validador = ""
                            for j in hijos:
                                validador = self.rec(j,self.cadena[i])
                                if validador:
                                    stack.push(j[0])
                                    self.crearTabla(self.pilaTemp,self.cadena[i:],ultimo.getValor(),j[0].getValor())
                                    self.pilaTemp.pop()
                                    self.pilaTemp.append(j[0].getValor())
                                    self.crearArbol(ultimo,j)
                                    leido = True
                                    #encontrado = True
                                    break
                            if not validador:
                                self.crearTabla(self.pilaTemp,self.cadena[i:],"Fallido",None)
                                ultimo = stack.pop()
                                self.pilaTemp.pop()
                    elif ultimo.getTipo()==Tipo.TERMINAL:
                        if ultimo.getValor()== self.cadena[i]:
                            self.crearTabla(self.pilaTemp,self.cadena[i:],None,ultimo.getValor())
                            self.pilaTemp.pop()
                            leido = True
                            #encontrado = True
                            avanzar = True
                        else:
                            self.crearTabla(self.pilaTemp,self.cadena[i:],"Fallido",None)
                            self.guardar(self.tabla)
                            #print(self.getArbol())
                            self.drawArbol()
                            return "Cadena inválida."
                #if not encontrado:
                    #print (stack.pop().getValor())
        self.tabla.append("#$"+"--"+"$Q,Λ,#;F,Λ")
        ultimo = stack.pop()
        self.pilaTemp.pop()
        #print (ultimo)
        if ultimo == "#":
            self.tabla.append("Λ$"+"--"+"$Aceptación")
            self.guardar(self.tabla)
            #print(self.getArbol())
            self.drawArbol()
            return "Cadena válida."
        else:
            #print(self.getArbol())
            self.drawArbol()
            return "Cadena inválida."
        
    
    def rec(self,hijos,char):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método recursivo que busca un camino dentro de la pila para el caracter evaluado.
        __________________________________________________________________________________
        ► Parámetros:
        
        • hijos: Los posibles nodos hijos que tendrían un camino disponible para evaluar.
        • char: El caracter en evaluación.
        __________________________________________________________________________________
        '''  
        hijo = hijos[0]
        if hijo.getTipo()== Tipo.TERMINAL:
            if hijo.getValor()== char:
                return True
            else:
                return False
        elif hijo.getTipo() == Tipo.NOTERMINAL:
            for i in hijo.getHijo():
                val = self.rec(i,char)
                if val:
                    return True
            return False

    def crearTabla(self,p,cadena,padre,hijo):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de crear la tabla que contendrá los movimientos de la pila.
        __________________________________________________________________________________
        ► Parámetros:
        
        • p = Pila actual.
        • cadena =  Cadena evaluada.
        • padre = Padre en donde se encuentra actualmente la pila.
        • hijo = Hijos a los que se puede dirigir el padre.
        __________________________________________________________________________________
        '''  
        pila = ""
        for i in reversed(p):
            pila = pila+i
        if padre != "Fallido":
            transicion = self.buscarTransicion(hijo,padre)
            elemento = pila+"$"+cadena+"$"+transicion
        else:
            elemento = pila+"$"+cadena+"$"+"Fallido"
        #print(elemento)
        self.tabla.append(elemento)
        
        
    def buscarTransicion(self,hijo,padre=None):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de buscar una transición válida entre nodos.
        __________________________________________________________________________________
        ► Parámetros:
        
        • hijo = Lista de hijos actual en donde se encuentra evaluando la pila.
        • padre =  El actual nodo padre en donde se encuentra la pila.
_________________________________________________________
        '''  
        a = self.automata.getAutomata().get_transiciones()
        if padre != None:
            if hijo != None:
                for i in a:
                    #Padre en posición 2
                    #Hijo en posición 4
                    j = i.replace(";",",")
                    j = j.split(",")
                    if padre == j[2] and hijo == j[4]:
                        return i
            else:
                print("No se qué poner aquí")
                   
        else:
            for i in a:
                #Padre en posición 2
                #Hijo en posición 4
                j = i.replace(";",",")
                j = j.split(",")
                if hijo == j[1] and hijo == j[2]:
                    return i            
        return False
    
    def hijoAtexto(self,hijo):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método que retorna el valor guardado en un nodo.
        __________________________________________________________________________________
        ► Parámetros:
        
        • hijo = Lista de nodos hijo.
        __________________________________________________________________________________
        '''  
        retorno = ""
        try:
            for i in hijo:
                retorno = retorno+i.getValor()
        except Exception as ex:
            print (ex)
            return hijo.getValor()
            
        return retorno
    
    def guardar(self,lista):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de crear el archivo csv que guardará la tabla generada.
        __________________________________________________________________________________
        ► Parámetros:
        
        • lista: Lista de todas las acciones realizadas dentro de la pila.
        __________________________________________________________________________________
        '''  
        texto = ""
        for i in range(0,len(lista)):
            if i == 0:
                texto = lista[i]+"\n"
            else:
                texto = texto+lista[i]+"\n"
            
        texto = texto.replace("Λ","-")
        archivo = open("tabla"+".csv","w")
        archivo.write(texto)
        archivo.close()
        
    def crearArbol(self,padre,hijos):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de crear el árbol generado por la cadena en su evaluación.
        __________________________________________________________________________________
        ► Parámetros:
        
        • padre = El padre donde se encuentra actualmente el autómata evaluando.
        • hijos =  Los hijos del padre actual.
        __________________________________________________________________________________
        '''  
        NodoPadre = self.getNodoA(padre.getValor())
        if NodoPadre == False:
            NodoPadre = NodoA(padre.getValor())
            NodoPadre.setAsignacion()
            self.NodosA.append(NodoPadre)
            try:
                for i in hijos:
                    NodoHijo = NodoA(i.getValor())
                    self.NodosA.append(NodoHijo)
                    self.escribirArbol(NodoPadre, NodoHijo)
            except Exception as ex:
                print(ex)
                NodoHijo = NodoA(hijos.getValor())
                self.NodosA.append(NodoHijo)
                self.escribirArbol(NodoPadre, NodoHijo)
        else:
            NodoPadre.setAsignacion()
            try:
                for i in hijos:
                    NodoHijo = NodoA(i.getValor())
                    self.NodosA.append(NodoHijo)
                    self.escribirArbol(NodoPadre, NodoHijo)
            except Exception as ex:
                print(ex)
                NodoHijo = NodoA(hijos.getValor())
                self.NodosA.append(NodoHijo)
                self.escribirArbol(NodoPadre, NodoHijo)
            

        
    def getNodoA(self,valor):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de retornar nodos no asignados dentro de un árbol.
        __________________________________________________________________________________
        ► Parámetros:
        
        • valor: El valor a buscar dentro de los nodos existentes.
        __________________________________________________________________________________
        '''  
        for i in self.NodosA:
            if valor == i.getValor() and not i.getAsignacion():
                return i
        return False
    
    def escribirArbol(self,padre,hijo):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de crear un string con los movimiento de la pila.
        __________________________________________________________________________________
        ► Parámetros:
        
        • padre: Nodo padre en donde se encuentra actualmente la pila.
        • hijo: Nodos hijos del padre actual.
        __________________________________________________________________________________
        '''  
        if self.arbol=="":
            self.arbol = padre.getNombre()+";"+"\n"
            self.arbol = self.arbol+padre.getLabel()+"\n"
            self.arbol = self.arbol+padre.getNombre()+"->"+hijo.getNombre()+"\n"
            self.arbol = self.arbol+hijo.getLabel()+"\n"
        else:
            self.arbol = self.arbol+padre.getNombre()+"->"+hijo.getNombre()+"\n"
            self.arbol = self.arbol+hijo.getLabel()+"\n"            
            
    def getArbol(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de retornar el árbol generado.
        __________________________________________________________________________________
        ► Parámetros:
        
        • (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        return self.arbol
            
        
    def drawArbol(self):
        '''
        __________________________________________________________________________________
        ► Descripción:
        
        → Método encargado de crear el archivo gv del árbol creado.
        __________________________________________________________________________________
        ► Parámetros:
        
        • (Sin parámetros)
        __________________________________________________________________________________
        ''' 
        texto = "digraph A{ \n"
        texto = texto+self.getArbol()+"\n}"
        archivo = open("arbol.gv","w")
        archivo.write(texto)
        archivo.close()
        render('dot', 'png', 'C:/Users/Jo/Documents/eclipse/Proyecto1_Lenguajes/Proyecto/arbol.gv')   
        