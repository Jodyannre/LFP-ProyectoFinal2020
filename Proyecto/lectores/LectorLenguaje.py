#!/usr/bin/python
# -*- coding: utf-8 -*-

from metodos.afd import afd
from metodos.Gramatica import Gramatica
from nodos.Nodo import Nodo
from metodos.GramaticaE import GramaticaE
import time
import os

class LectorLenguaje(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase destinada a crear lectores de archivos de entrada.
    __________________________________________________________________________________
    '''


    def __init__(self,nombre,lenguajes=None):
        '''
        __________________________________________________________________________________
        ► Parámetros:
        
        • nombre = el nombre del objeto asignado a la nueva instancia.
        • lenguaje = El lenguaje a retornar creado por los archivos de entrada.
        __________________________________________________________________________________
        ► Variables:
        
        • self.nombre = El nombre representativo del nuevo objeto.
        • self.gramarN =  La nueva gramática creada por los archivos de entrada.
        • self.gramatica = Booleano que valida si la entrada es una gramática.
        • self.afd = Booleano que valida si la entrada es un afd.
        • self.lenguajes =  Recibe el lenguaje de entrada.

        __________________________________________________________________________________
        '''
        self.afdN = afd(nombre)
        self.gramarN = Gramatica(nombre)
        self.gramatica = False
        self.afd = False
        if not lenguajes == None:
            self.lenguajes = lenguajes
        self.gramaticaT2 = GramaticaE(nombre)
        
        
        
    def cargar(self,tipo):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de validar si los datos de entrada son correctos.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • tipo = El tipo de los datos de entrada. (Gramática o afd)            
        __________________________________________________________________________________
        '''
        os.system("cls")
        if tipo==0:  
            while True:    
                print("Ingrese el nombre del archivo .afd")
                print(">> ", end="")
                nombre = input()                
                if ".afd" in nombre:
                    try:
                        lista = self.leerArchivo(nombre)
                        eliminar = []
                        for i in range(0,len(lista)):
                            if lista[i]=="":
                                eliminar.append(i)
                        for i in reversed(eliminar):
                            lista.pop(i)
                        nombre = nombre.replace(".afd","")
                        temporal = 0
                        for i in reversed(nombre):
                            if i.isupper() or i.islower() or i!="\\":
                                temporal = temporal+1
                            else:
                                break
                        temporal = len(nombre)-temporal
                        nombre = nombre[temporal:]   
                        for i in self.lenguajes:
                            if i.get_nombre()==nombre:
                                print("Ese afd ya existe.")
                                input()
                                return                     
                        self.afdN.set_nombre(nombre)
                        self.crearAfd(lista)
                        self.afd = True
                        break
                    except Exception as e: print(e)
                    #except:
                        #print("Error, el archivo no existe")
                else:
                    print("Error, tipo de dato no permitido.")
                if nombre == "":
                    break
                
            else:
                print("Error, tipo de dato no permitido")
            #print(self.afdN.get_estadoA())
            #print(self.afdN.get_estadoI())
            #print(self.afdN.get_estados())
            #print(self.afdN.get_simbolos())
            #print(self.afdN.get_transiciones())
        else:
            while True:
                print("Ingrese el nombre del archivo .grm")
                print(">> ", end="")
                nombre = input() 
                if ".grm" in nombre:
                    try:
                        lista = self.leerArchivo(nombre)
                        eliminar = []
                        for i in range(0,len(lista)):
                            if lista[i]=="":
                                eliminar.append(i)
                        for i in reversed(eliminar):
                            lista.pop(i)
                        nombre = nombre.replace(".grm","")
                        temporal = 0
                        for i in reversed(nombre):
                            if i.isupper() or i.islower() or i!="\\":
                                temporal = temporal+1
                            else:
                                break
                        temporal = len(nombre)-temporal
                        nombre = nombre[temporal:]
                        for i in self.lenguajes:
                            if i.get_nombre()==nombre:
                                print("Esa gramática ya existe.")
                                input()
                                return 
                        #nombre = nombre[len(nombre)-1]
                        self.gramarN.set_nombre(nombre)
                        self.crearGramatica(lista)
                        self.gramarN.convertirGramatica()
                        self.gramatica = True
                        break
                    except Exception as e:
                        print(e)
                        print("Error, el archivo no existe.")
                else:
                    print("Error, tipo de dato no permitido.")
                if nombre == "":
                    break
        
        
    def leerArchivo(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de leer el archivo .grm o .afd.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = Nombre del archivo de entrada.         
        __________________________________________________________________________________
        '''
        archivo = open(nombre,"tr")
        t = archivo.read()
        t = t.replace(" ","")
        t = t.split("\n")   
        archivo.close()
        return t
        
    def crearGramatica(self,lista):   
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de crear una gramática a partir del archivo de entrada.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • lista = Lista de todos los elementos de la gramática en el archivo de entrada.           
        __________________________________________________________________________________
        '''
        for i in lista:
            i = i.replace(" ","")
            terminal = ""
            nt = ""
            inicial = ""
            final = ""
            temporal = ""
            if "|" in i:
                temporal = i.split("|")
                for j in temporal:
                    if ">" in j:
                        inicial = j.split(">")
                        final = inicial[1]
                        inicial = inicial[0]
                    else:
                        final = j
                    if len(self.gramarN.get_no_terminales())==0:
                        self.gramarN.agreger_nt_inicial(inicial)
                    if not inicial in self.gramarN.get_no_terminales():
                        self.gramarN.agregar_no_terminales(inicial)
                        nodo = Nodo(inicial,0) #Agregar no terminales y sus nodos
                        self.gramarN.agregar_nodo(nodo)
                    if final!="épsilon" and final!="epsilon":
                        for k in final:
                            if not k in self.gramarN.get_terminales() and k.islower():
                                self.gramarN.agregar_terminal(k) #Agregar terminales y sus nodos
                                nodo = Nodo(k,1)
                                self.gramarN.agregar_nodo(nodo)
                            elif k.isupper() and not k in self.gramarN.get_no_terminales():
                                self.gramarN.agregar_no_terminales(k) #Agregar no terminales y sus nodos
                                nodo = Nodo(k,0)
                                self.gramarN.agregar_nodo(nodo)
                            elif not k in ["'","\\","-"] and not k in self.gramarN.get_terminales() and not j in self.gramarN.get_no_terminales():
                                self.gramarN.agregar_terminal(k) #Agregar terminales y sus nodos
                                nodo = Nodo(k,1)
                                self.gramarN.agregar_nodo(nodo)                            
                    produccion = inicial+">"+final
                    if not produccion in self.gramarN.get_producciones():
                        self.gramarN.agregar_produccion(produccion) #Agregar producciones
          
            else:
                i = i.replace(" ","")    
                temporal = i.split(">")
                inicial = temporal[0]
                final = temporal[1]
                if len(self.gramarN.get_no_terminales())==0:
                    self.gramarN.agreger_nt_inicial(inicial)
                if not inicial in self.gramarN.get_no_terminales():
                    self.gramarN.agregar_no_terminales(inicial) #Agregar no terminales y nodos
                    nodo = Nodo(inicial,0)
                    self.gramarN.agregar_nodo(nodo)
                if final!="épsilon" and final!="epsilon":
                    for j in final:
                        if j.isupper() and not j in self.gramarN.get_no_terminales():
                            self.gramarN.agregar_no_terminales(j) #Agregar no terminales y nodos
                            nodo = Nodo(j,0)
                            self.gramarN.agregar_nodo(nodo)
                        if j.islower() and not j in self.gramarN.get_terminales():
                            self.gramarN.agregar_terminal(j)
                            nodo = Nodo(j,1)
                            self.gramarN.agregar_nodo(nodo)
                        if not j in ["'","\\","-"] and not j in self.gramarN.get_terminales() and not j in self.gramarN.get_no_terminales():
                            self.gramarN.agregar_terminal(j) #Agregar terminales y sus nodos
                            nodo = Nodo(j,1)
                            self.gramarN.agregar_nodo(nodo)  
                        
                if not i in self.gramarN.get_producciones():
                    self.gramarN.agregar_produccion(i) #Agregar producciones
            self.gramarN.mostrar_gramatica(i[0], i)
        #print(self.gramarN.get_no_terminales())
        #print(self.gramarN.get_terminales())
        #print(self.gramarN.get_ntInicial())
        #print(self.gramarN.get_producciones()) 
        

                
    def crearAfd(self,lista):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de crear un afd a partir de los datos de entrada.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • lista = Lista con todos los elementos del afd en el archivo de entrada.           
        __________________________________________________________________________________
        '''
        nt1= ""
        nt2= ""
        sim= ""
        ntA= ""
        transicion = ""
        validacion = ""
        validacion2 = ""
        for i in lista:
            i = i.replace(" ","")
            validacion = i.split(";")
            transicion = validacion[0]
            validacion = validacion[1].split(",")
            validacion2 = validacion[1]
            validacion = validacion[0]
            i = i.replace(";",",")
            i = i.split(",")
            nt1 = i[0]
            nt2 = i[1]
            sim = i[2]
            ntA = i[3]
            ntA2 = i[4]
            if not nt1 in self.afdN.get_estados():
                self.afdN.agregar_estados(nt1)
            if not nt2 in self.afdN.get_estados() and nt2!="-" :
                self.afdN.agregar_estados(nt2)
            if not sim in self.afdN.get_simbolos():
                self.afdN.agregar_simbolos(sim) 
            if not transicion in self.afdN.get_transiciones():
                self.afdN.agregar_transiciones(nt1+","+nt2+";"+sim)
                nodo1 = Nodo(nt1,2)
                nodo2 = Nodo(nt2,2)
                nodo3 = Nodo(sim,3)
                self.afdN.agregar_transicionesN([nodo1,nodo2,nodo3])
                if validacion.lower() == "true" and not nt1 in self.afdN.get_estadoA():
                    self.afdN.agregar_estadoA(nt1)
                elif validacion.lower() == "false" and nt1 in self.afdN.get_estadoA():
                    nodo = self.afdN.buscar_nodo(nt1)
                    self.afdN.get_estadoA().remove(nt1)
                    self.afdN.get_estadoAN().remove(nodo)
                # Validaciones para nt2
                if validacion2.lower() == "true" and not nt2 in self.afdN.get_estadoA():
                    self.afdN.agregar_estadoA(nt2)
                elif validacion.lower() == "false" and nt2 in self.afdN.get_estadoA():
                    nodo = self.afdN.buscar_nodo(nt2)
                    self.afdN.get_estadoA().remove(nt2)
                    self.afdN.get_estadoAN().remove(nodo)     
                               
        self.afdN.agregar_estadoI(self.afdN.get_estados()[0])
        self.afd = True
            
        
    def get_gramatica(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Retorna el gramática creada.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)       
        __________________________________________________________________________________
        '''
        return self.gramarN
    def get_afd(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Retorna el afd creado.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        return self.afdN
    def get_gramaticaAgregada(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Retorna la gramática agregada al lenguaje.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)        
        __________________________________________________________________________________
        '''
        return self.gramatica
    def get_afdAgregado(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Retorna el afd agregado a la gramática.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        return self.afd
    def get_Tipo2(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Retorna la gramática cargada tipo 2.             
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        return self.gramaticaT2
        
    def cargaTipo2(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de cargar una gramática tipo 2.             
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = El nombre de la gramática.
        __________________________________________________________________________________
        '''
        os.system("cls")
  
        while True:    
            print("Ingrese el nombre del archivo .grm")
            print(">> ", end="")
            nombre = input()   
            
            if ".grm" in nombre:
                break
            else:
                print("Nombre de gramática incorrecto. Vuelva a intentarlo")
                input()

        temporal = 0
        lista = self.leerArchivo(nombre)
        nombre = nombre.replace(".grm","")
        for i in reversed(nombre):
           if i.isupper() or i.islower() or i!="\\":
               temporal = temporal+1
           else:
               break       
        temporal = len(nombre)-temporal
        nombre = nombre[temporal:] 
        self.gramaticaT2.agregarDatos_Masivo(nombre,lista)
        