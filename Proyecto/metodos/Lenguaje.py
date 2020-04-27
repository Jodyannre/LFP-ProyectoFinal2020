#!/usr/bin/python
# -*- coding: utf-8 -*-
from metodos.afd import afd
from metodos.Gramatica import Gramatica
from nodos.Nodo import Nodo
from tipos.Tipo import Tipo
import re
import os
import time




class Lenguaje(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase lenguaje encargada de crear los lenguajes usados en el programa.
    __________________________________________________________________________________
    '''


    def __init__(self, nombre):
        '''
        __________________________________________________________________________________
        ► Parámetros:
        
        • nombre = el nombre del objeto asignado a la nueva instancia.
        __________________________________________________________________________________
        ► Variables:
        
        • self.nombre = Recibe el valor de nombre.
        • self.grammarN =  Gramática perteneciente al lenguaje.
        • self.afdN = AFD perteneciente al lenguaje.
        • self.cadenas_validas = Lista que guarda las cadenas válidas.
        • self.cadenas_invalidas =  Lista que guarda las cadenas inválidas.  
        __________________________________________________________________________________
        '''
        self.grammarN = Gramatica(nombre)
        self.afdN = afd(nombre)
        self.nombre = nombre
        self.cadenas_validas = []
        self.cadenas_invalidas = []
        self.evaluar = False
        
     
    def set_afd(self, afd):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de crear el afd del lenguaje.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • afd = El afd a agregar al lenguaje.
        __________________________________________________________________________________
        '''
        self.afdN = afd
        self.nombre = afd.get_nombre()
        self.crear_gramatica()
        self.convertir_grammar()
        
    def set_grammar(self,grammar):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de crear la gramática del lenguaje.            
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • grammar = La gramática a agregar al lenguaje.        
        __________________________________________________________________________________
        '''
        self.grammarN = grammar 
        self.nombre = grammar.get_nombre()
        self.convertir_grammar() 
        self.crear_afd(self.grammarN.get_pc(), self.grammarN.get_pcN())
        
    def crear_afd(self, lista,listaN):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de crear el afd cuando se agrega una gramática.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        •lista: Lista de transiciones del afd.
        •listaN: Lista de transiciones del afd en formato nodo.
        __________________________________________________________________________________
        '''
        nuevoAfd = afd(self.nombre)
        estadosA = []
        nodoActual = listaN[0][0]
        nodoProd = listaN[0][1]
        noEA= []
        estados = []
        for i in lista:
            i = i.replace(";",",")
            i = i.split(",")
            if not i[0] in estados:
                estados.append(i[0])
                
        for i in estados:
            for j in lista:
                j = j.replace(";",",")
                j = j.split(",")
                if j[1] == "-" and not j[0] in estadosA:
                    estadosA.append(j[0])
                    break
                else:
                    continue


        #print(estadosA)

        for i in lista:
            i = i.replace(";",",")
            i = i.split(",")
            if not i[0] in nuevoAfd.get_estados() and i[0]!="-":
                nuevoAfd.agregar_estados(i[0])
            if not i[1] in nuevoAfd.get_estados() and i[1]!="-":
                nuevoAfd.agregar_estados(i[1])
            if not i[2] in nuevoAfd.get_simbolos() and i[2]!="-":
                nuevoAfd.agregar_simbolos(i[2])
        for i in estadosA:
            nuevoAfd.agregar_estadoA(i)
                
        nuevoAfd.agregar_estadoI(nuevoAfd.get_estados()[0])
        nuevoAfd.set_transiciones(self.grammarN.get_pc(), self.grammarN.get_pcN())
        self.afdN = nuevoAfd
        #print(self.afdN.get_estadoI())
        #print(self.afdN.get_estadoA())
        #print(self.afdN.get_estados())
        #print(self.afdN.get_transiciones())
        #print(self.afdN.get_simbolos())
        
    def crear_gramatica(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de crear una gramática cuando se agrega un afd.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        #Estados ->
        nuevaGramatica = Gramatica(self.nombre)
        nt = []
        terminal = []
        ntI = ""
        producciones = []
        pcN = []
        pc = []
        nuevaGramatica.set_izquierda(False)
        for i in self.afdN.get_estados():
            nuevaGramatica.agregar_no_terminales(i)
        for i in self.afdN.get_simbolos():
            nuevaGramatica.agregar_terminal(i)
        nuevaGramatica.agreger_nt_inicial(self.afdN.get_estadoI())
        
        for i in self.afdN.get_transiciones():
            temporal = i.replace(";",",")
            temporal = temporal.split(",")
            if temporal[1] == "-" or temporal[1] == " ":
                produccion = temporal[0]+">"+temporal[2]
            else:
                produccion = temporal[0]+">"+temporal[2]+temporal[1]
            nuevaGramatica.mostrar_gramatica(temporal[0], produccion)
            producciones.append(produccion)
        nuevaGramatica.set_guardar(producciones)   
        nuevaGramatica.set_producciones(producciones)
        self.grammarN = nuevaGramatica
        #print(self.grammarN.get_no_terminales())
        #print(self.grammarN.get_terminales())
        #print(self.grammarN.get_ntInicial())
        #print(self.grammarN.get_producciones())
        
        
        
    def convertir_grammar(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de convertir los componentes de la gramática a formato nodo.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        prod = self.grammarN.get_pc() #Producciones completas
        direccion = ""
        conversion = []
        conversionN = []
        
        if self.grammarN.get_izquierda():
            for i in prod:
                inicial = i.split(">")
                final = inicial[1]
                inicial = inicial[0]
                direccion = ""
                
                if "'" in i:
                    dir = False
                    for j in final:
                        if "'" in final:
                            if not "'" in inicial:
                                direccion = inicial+"'"
                            else:
                                direccion = inicial
                            final = final.replace(direccion,"")
                            break
                        else:
                            if j.isupper():
                                direccion = j
                                final = final.replace(direccion,"")
                                break
                            else:
                                direccion = ""
                            
                    if direccion == "":
                        if final=="épsilon" or final=="epsilon":
                            final = "-" 
                            conversion.append(inicial+","+"-"+";"+final)  
                            nodoI = self.grammarN.buscar_nodo(inicial)
                            nodoD = self.grammarN.buscar_nodo(direccion)  
                            conversionN.append([nodoI,"-","-"])                          
                        else:                                                                            
                            nodoI = self.grammarN.buscar_nodo(inicial)
                            nodoD = self.grammarN.buscar_nodo(direccion)
                            nodoF = self.grammarN.buscar_nodo(final)
                            conversion.append(inicial+","+"-"+";"+final)
                            conversionN.append([nodoI,"-",nodoF])
                    else:    
                        if final=="épsilon" or final=="epsilon":
                            final = "-"
                            conversion.append(inicial+","+direccion+";"+final)
                            nodoI = self.grammarN.buscar_nodo(inicial)
                            nodoD = self.grammarN.buscar_nodo(direccion)             
                            conversionN.append([nodoI,nodoD,"-"])      
                            
                        else:                                        
                            nodoI = self.grammarN.buscar_nodo(inicial)
                            nodoD = self.grammarN.buscar_nodo(direccion)
                            nodoF = self.grammarN.buscar_nodo(final)
                            conversion.append(inicial+","+direccion+";"+final)
                            conversionN.append([nodoI,nodoD,nodoF])
                        
                    
                elif "épsilon" in i or "epsilon" in i:
                    conversion.append(inicial+",-;-")
                    nodoI = self.grammarN.buscar_nodo(inicial)
                    conversionN.append([nodoI,"-","-"])
                    
                else:
                    if i[len(i)-1].isupper():
                        direccion = i[len(i)-1]
                        final = final.replace(direccion,"")
                        conversion.append(inicial+","+direccion+";"+final)
                        nodoI = self.grammarN.buscar_nodo(inicial)
                        nodoD = self.grammarN.buscar_nodo(direccion)
                        nodoF = self.grammarN.buscar_nodo(final)
                        conversionN.append([nodoI,nodoD,nodoF])
                    else:
                        direccion = ""
                        conversion.append(inicial+",-;"+final)
                        nodoI = self.grammarN.buscar_nodo(inicial)
                        nodoD = self.grammarN.buscar_nodo(direccion)
                        nodoF = self.grammarN.buscar_nodo(final)
                        conversionN.append([nodoI,"-",nodoF])
        else:
            for i in prod:
                inicial = i.split(">")
                final = inicial[1]
                inicial = inicial[0]
                direccion = ""            
                if "épsilon" in final or "epsilon" in final:
                    conversion.append(inicial+",-;-")
                    nodoI = self.grammarN.buscar_nodo(inicial)
                    nodoD = self.grammarN.buscar_nodo(direccion)
                    nodoF = self.grammarN.buscar_nodo(final)
                    conversionN.append([nodoI,"-","-"])                    
                else:
                    if i[len(i)-1].isupper():
                        direccion = i[len(i)-1]
                        final = final.replace(direccion,"")
                        conversion.append(inicial+","+direccion+";"+final)
                        nodoI = self.grammarN.buscar_nodo(inicial)
                        nodoD = self.grammarN.buscar_nodo(direccion)
                        nodoF = self.grammarN.buscar_nodo(final)
                        conversionN.append([nodoI,nodoD,nodoF])
                    else:
                        direccion = ""
                        conversion.append(inicial+",-;"+final)
                        nodoI = self.grammarN.buscar_nodo(inicial)
                        nodoD = self.grammarN.buscar_nodo(direccion)
                        nodoF = self.grammarN.buscar_nodo(final)
                        conversionN.append([nodoI,"-",nodoF])
        
        #print(conversion)
        #print(conversionN)
        self.grammarN.pc = conversion
        self.grammarN.pcN = conversionN
            
    def obtener_lista_nt(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista de producciones de un no terminal.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = El valor del no terminal.
        __________________________________________________________________________________
        '''
        lista = self.formatear_lista_nt()
        listaR = []
        for i in lista:
            if i[0].get_valor()==nombre:
                listaR.append(i[1:])
                #print(listaR)
                break
        return listaR
        
    def formatear_lista_nt(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de formatear una lista al formato (nt,(prod,prod,prod.......))                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        lista = self.grammarN.get_pcN()
        #print(self.grammarN.get_pc())
        listaR = []
        tempo = []
        tmp = []
        nt = ""
        lista_ordenada = []
        epsilon = Nodo("epsilon",4)
        for i in lista:
            temporal = i
            #print(i)
            try:
                if len(temporal[2])>1:
                    temporal[2].append(temporal[1])
                    #print(temporal[2])
                else:
                    if not temporal[2]=="-" and not temporal[1]=="-":
                        temporal[2] = [temporal[2],temporal[1]]
                    elif temporal[1]=="-":
                        #temporal[2]=["-"] #cambio de caracter a nodo épsilon 25-03-2020
                        temporal[2]=[epsilon]
            except:
                if not temporal[2]=="-" and not temporal[1]=="-":
                    temporal[2] = [temporal[2],temporal[1]]
                elif temporal[2]=="-" and temporal[1]=="-":
                    #temporal[2]=["-"] #cambio por nodo epsilon
                    temporal[2]=[epsilon]
                elif temporal[1]=="-":
                    temporal[2]=[temporal[2]]
            temporal.pop(1)
            listaR.append(temporal)
            #print(temporal)
        #print(listaR)
        
        for i in listaR:
            if i[0].get_valor() in nt:
                for j in range (1,len(i)):
                    for k in range(0,len(i[j])):
                        tmp.append(i[j][k])
                    if i == listaR[len(listaR)-1]:
                        tempo.append(tmp)   
            else:
                tempo.append(tmp)
                tmp = []
                nt = i[0].get_valor()
                tmp.append(i[0])
                for j in range(1,len(i)):
                    for k in range(0,len(i[j])):
                        tmp.append(i[j][k])
                    if i == listaR[len(listaR)-1]:
                        tempo.append(tmp)
        listaR = tempo[1:]
        print()
        for i in range(0,len(listaR)-1):
            j = i+1
            if j<= len(listaR)-1:
                while j <= (len(listaR)-1):
                    if listaR[i][0].get_valor() == listaR[j][0].get_valor():
                        l = 1
                        for k in listaR[j]:
                            if l<= len(listaR[j])-1: 
                                listaR[i].append(listaR[j][l])
                                l = l+1
                            
                        listaR.pop(j)
                    j = j+1
                    
                
                
        self.grammarN.set_pcN(listaR)
        

        for i in listaR:
            for j in i:
                print()
                print(j.get_valor())
        return listaR
    
    def get_listaFormateada(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista formateada por el método formatear.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = El valor del no terminal del cual retornara la lista de producciones.        
        __________________________________________________________________________________
        '''
        lista = self.grammarN.get_pcN()
        listaR = []   
        for i in lista:
            if i[0].get_valor()==nombre:
                listaR = i[1:]
                break        
        return listaR
    
    def get_listaFormateadaLetras(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de solicitar y guardar no terminales.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        lista = self.grammarN.get_pcN()
        listaR = []   
        for i in lista:
            if i[0].get_valor()==nombre:
                temporal = []
                for j in i[1]:
                    if j != "-":
                        temporal.append(j.get_valor())
                    else:
                        temporal.append(j)
                listaR.append(temporal)        
        return listaR    
    
    def guardar(self,tipo,nombreA):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de guardar la gramática o el afd en un archivo .grm o .afd.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • tipo = El tipo a guardar, ya sea gramática o afd.
        • nombreA = Nombre con el cual se guardará el archivo.
        __________________________________________________________________________________
        '''
        if tipo==0:
            #print("afd")
            #print(self.afdN.get_transiciones())
            texto = ""
            lista = self.afdN.get_transiciones()
            for i in range(0,len(lista)-1): #Ordenar las transiciones por estado inicial
                if lista[i][0] == self.afdN.get_estadoI():
                    temporal = lista[i]
                    lista[i] = lista[0]
                    lista[0] = temporal
                    break   
            for i in self.afdN.get_transiciones():
                i = i.replace(";",",")
                temporal = i.split(",")
                i = i+";"
                
                if temporal[1] == "-" and temporal[0] in self.afdN.get_estadoA() and not temporal[1] in self.afdN.get_estadoA() :
                    i = i+"true,false"
                #elif temporal[0] in self.afdN.get_estadoA() and temporal[1]=="-":
                    #i = i+"true"
                elif temporal[1] != "-" and temporal[0] in self.afdN.get_estadoA() and temporal[1] in self.afdN.get_estadoA() :
                    i = i+"true,true"   
                elif temporal[1] != "-" and temporal[0] in self.afdN.get_estadoA() and not temporal[1] in self.afdN.get_estadoA() :
                    i = i+"true,false"
                elif temporal[1] != "-" and not temporal[0] in self.afdN.get_estadoA() and not temporal[1] in self.afdN.get_estadoA() :
                    i = i+"false,false"
                elif temporal[1] != "-" and not temporal[0] in self.afdN.get_estadoA() and temporal[1] in self.afdN.get_estadoA() :
                    i = i+"false,true"
                    
                texto = texto+i+"\n"
            archivo = open(nombreA+".afd","w")
            archivo.write(texto)
            archivo.close()
                
        else:
            #print("Gramática")
            #print(self.grammarN.get_guardar())
            texto = ""
            for i in self.grammarN.get_guardar():
                texto = texto+i+"\n"
            archivo = open(nombreA+".grm","w")
            archivo.write(texto)
            archivo.close()
            
    def agregar_cadenaV(self,cadena):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de agregar las cadenas válidas a self.cadenas_validas.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • cadena = La cadena a guardar.          
        __________________________________________________________________________________
        '''
        self.cadenas_validas.append(cadena)
    def agregar_cadenaI(self,cadena):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de agregar las cadenas inválidas a self.cadenas_invalidas.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • cadena = La cadena a guardar.            
        __________________________________________________________________________________
        '''
        self.cadenas_invalidas.append(cadena)

    def set_nombre(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de asignar un nombre al lenguaje.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = El valor a asignarle a la variable self.nombre.         
        __________________________________________________________________________________
        '''
        self.nombre = nombre
    def get_cadenaV(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista de cadenas válidas.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        return self.cadenas_validas
    def get_cadenaI(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista de cadenas inválidas.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        return self.cadenas_invalidas
    def get_gramatica (self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la gramática del lenguaje.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        return self.grammarN
    def get_afd (self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar el afd del lenguaje.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        return self.afdN
    def get_nombre(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar el nombre del lenguaje.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        return self.nombre      
    
    def get_evaluar(self):
        return self.evaluar
    def set_evaluar(self,cambio):
        self.evaluar = cambio  
        
        
        
        
    
        
        