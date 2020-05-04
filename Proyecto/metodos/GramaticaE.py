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
        for i in range(len(hijos)):
            if hijos[len(hijos)-1]=="'" and i == (len(hijos)-2):
                lista.append(self.getNodo(hijos[i:]))
                return lista
            else:
                lista.append(self.getNodo(hijos[i]))
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
        lista = self.eliminarRecursividad2(lista)
        for i in range(len(lista)):
            self.producciones.append(lista[i])
            #print(lista[i])
            j = lista[i].split(">")
            padre = j[0]
            hijo = j[1]
            nuevo = hijo[len(hijo)-2]+"'"
            hijoTemp = ""
            if "'" in hijo:
                if not self.repetido(0,nuevo):
                    self.nt.append(NodoL(nuevo,Tipo.NOTERMINAL))
                hijoTemp = hijo[0:len(hijo)-2]
                
            if not self.repetido(0,padre):
                self.nt.append(NodoL(padre,Tipo.NOTERMINAL))
            
            if not "epsilon" in hijo and not "'" in hijo:
                
                for j in hijo:
                    nodo = self.getNodo(j)
                    if nodo==False and not j.isupper():
                        self.terminales.append(NodoL(j,Tipo.TERMINAL))
                    elif j.isupper():
                        nodo = self.getNodo(j)
                        if nodo == False:
                            self.nt.append(NodoL(j,Tipo.NOTERMINAL))                
            elif "'" in hijo:
                
                for j in hijoTemp:
                    nodo = self.getNodo(j)
                    if nodo==False and not j.isupper():
                        self.terminales.append(NodoL(j,Tipo.TERMINAL))
                    elif j.isupper():
                        nodo = self.getNodo(j)
                        if nodo == False:
                            self.nt.append(NodoL(j,Tipo.NOTERMINAL))
            else:
                if not self.repetido(0,"epsilon"):
                    self.nt.append(NodoL(hijo,Tipo.EPSILON))

            try:
                if len(hijo)>1 and not "epsilon" in hijo:
                    self.getNodo(padre).agregarHijo(self.listaHijos(hijo))
                elif len(hijo)>1 and "epsilon" in hijo:
                    self.getNodo(padre).agregarHijo([self.getNodo(hijo)])
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
        #print(lista[0][0])
        self.ntInicial = self.getNt(lista[0][0])
    
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
        
    def eliminarRecursividad2(self, lista):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que elimina la recursividad por izquierda             
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • lista: Lista de producciones.          
        __________________________________________________________________________________
        '''
        # 0 = Transición sin recursividad
        # 1 = Transición con recursividad
        nLista = []
        ConR = []
        SinR = []
        leido = []
        padre = ""
        padres = ""
        hijo = ""
        validar = False
        while True:
            validar = False
            padre = ""
            hijo = ""
            for i in lista:
                repetido = False
                i = i.replace(" ","")
                for j in leido:
                    if j == i:
                        repetido = True
                        break
                if padre == "" and not repetido and i[0] not in padres:
                    validar = True
                    j = i.split(">")
                    padre = j[0]
                    padres = padres+padre
                    hijo = j[1]
                    leido.append(i)
                    if hijo[0].isupper() and hijo[0]==padre:
                        ConR.append(hijo[1:])
                    else:
                        SinR.append(hijo)
                elif padre != "" and padre==i[0] and not repetido:
                    validar = True
                    j = i.split(">")
                    hijo = j[1]
                    if hijo[0].isupper() and hijo[0]==padre:
                        ConR.append(hijo[1:])
                    else:
                        SinR.append(hijo)
                else:
                    continue
            if not validar:
                break
            if len(ConR) > 0:
                nPadre = padre+"'"
                for i in SinR:
                    nLista.append(padre+">"+i+nPadre)
                for i in ConR:
                    nLista.append(nPadre+">"+i+nPadre)
                nLista.append(nPadre+">"+"epsilon")
                ConR = []
                SinR = []
            else:
                for i in SinR:
                    nLista.append(padre+">"+i)
                SinR = []
            repetido = False
        #print(nLista)            
        return nLista
    
    
    def getNt(self,valor):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna un nt buscado.            
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • valor: Valor del nt buscado.          
        __________________________________________________________________________________
        '''
        for i in self.nt:
            #print (i.getValor())
            if i.getValor()==valor:
                return i
        return False
                
            
            
#n = GramaticaE("nueva")
#lista =["S > a A","S > b B","A > A 0","A > A 1","A > 0","B > B s","B > m"]
#lista = ["S > z M N z","M > a M a","M > z","N > b N b","N > z"]

#n.formatearEntradaTipo2(lista)
                     