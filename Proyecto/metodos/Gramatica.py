#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import time
from metodos.nt import nt
from nodos.Nodo import Nodo







class Gramatica(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase Gramatica encargada de crear las gramáticas del programa.
    __________________________________________________________________________________
    '''
    prueba = "[|][a-z]+[A-Z]*|[|][A-Z]*[a-z]+"
    patronGramar = "[A-Z]>[a-z]+[A-Z]*"+prueba+"|"+"[A-Z]>[A-Z]*[a-z]+"+prueba
    patronGramar2 = "[A-Z]>[a-z]+[A-Z]*|[A-Z]>[A-Z]*[a-z]+"
    patronGramar3 = "[a-z]+[A-Z]+"
    

    def __init__(self,nombre):
        '''
        __________________________________________________________________________________
        ► Parámetros:
        
        • nombre = el nombre del objeto asignado a la nueva instancia.
        __________________________________________________________________________________
        ► Variables:
        
        • self.nombre = Recibe el valor de nombre.
        • self.no_terminales =  Lista que guarda los no terminales de la gramática.
        • self.terminales = Lista que guarda los terminales de la gramática.
        • self.ntInicial = Lista que guarda el nt inicial de la gramática.
        • self.producciones =  Lista que guarda las producciones ingresadas.
        • self.pReporte = Guarda las producciones a imprimir en el reporte.
        • self.p2Reporte = Guarda las producciones transformadas a imprimir en el reporte.
        • self.diccionario =  Lista que guarda los componentes de la gramática clasifica-
            dos en terminales o no terminales.
        • self.pc = Lista que guarda las producciones en texto.
        • self.pcN = Lista que guarda los nodos de producciones.
        • self.izquierda =  Booleano que determina si la gramática tiene recurisivdad por
            izquierda.
        • self.nodos = Guarda todos los nodos generados para la gramática.
        • self.guardar = Guarda la gramática original.
        • self.transformada =  Booleano que determina si la gramática fue transformada.
        
        ► Estáticas:
        
        • prueba = Patrón utilizado por el módulo re para el ingreso de datos.
        • patronGramar = Patrón utilizado por el módulo re para el ingreso de datos.
        • patronGramar2 =  Patrón utilizado por el módulo re para el ingreso de datos.
        • patronGramar3 = Patrón utilizado por el módulo re para el ingreso de datos.        
        __________________________________________________________________________________
        '''
        self.nombre = nombre
        self.no_terminalesT = []
        self.no_terminales = []
        self.terminales = []
        self.ntInicial = ""
        self.producciones = []
        self.pReporte = []
        self.p2Reporte = []
        self.diccionario = {} #Detectar tipo de recursividad
        self.pc = []  #Producciones convertidas
        self.pcN = [] #Produccioens convertidas Nodos
        self.izquierda = False
        self.nodos = []
        self.guardar = [] #Formato para guardar
        self.transformada = False
    
    def ingreso_no_terminales(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de solicitar y guardar no terminales.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        while (True):
            os.system("cls")
            print('Ingrese el no terminal:')
            print(">> ", end="")
            terminal = input() 
            if terminal.isupper():
                if terminal in self.no_terminales or terminal in self.terminales:
                    print('No terminal repetido o pertenece a los terminales.')
                    time.sleep(2)
                elif terminal== "":
                    #print (self.no_terminales)
                    break
                else:
                    self.no_terminales.append(terminal)
                    nuevoNodo = Nodo(terminal,0)
                    self.nodos.append(nuevoNodo)
            elif terminal == "":
                os.system("cls")
                print("Terminales ingresados")
                time.sleep(2)
                break
            else:
                print("Error, los no terminales tienen que ir en mayúscula.")
                time.sleep(2)
        
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
            print('Ingrese el no terminal:')
            print(">> ", end="")
            terminal = input() 
            if terminal.islower():
                if terminal in self.no_terminales or terminal in self.terminales:
                    print('No terminal repetido o pertenece a los terminales.')
                    time.sleep(2)
                elif terminal== "":
                    #print (self.terminales)
                    break
                else:
                    self.terminales.append(terminal)
                    nuevoNodo = Nodo(terminal,1)
                    self.nodos.append(nuevoNodo)
            elif terminal == "":
                break
            else:
                print("Error, los no terminales tienen que ir en mayúscula.")
                time.sleep(2)
        self.verificar()
    def verificar(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de verifica el tipo y valor de los nodos ingresados.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        for i in self.nodos:
            print("Valor: "+i.valor+" Tipo: ",i.tipo)
        
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
            if inicial.isupper():
                if inicial in self.no_terminales:
                    self.ntInicial = inicial
                    break
                else:
                    print ("El símbolo: ",inicial," no existe en el lenguaje \
                    \n Intentelo de nuevo con otro NT_inicial que exista.")
                    time.sleep(2)
            elif inicial =="":
                break
            else:
                print("Error, el NT_inicial tiene que estar escrito en mayúsucla.")
                time.sleep(2)
    
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
        simbolo = ""
        prod = ""
        terminal = True
        while(True):
            os.system("cls")
            print("Ingrese gramática:")
            print(">> ", end="")
            ingreso = input() 
            ingreso = ingreso.replace(" ","")
            if ingreso in self.producciones:
                print("Producción repetida")
                time.sleep(2)
            elif ingreso =="":
                break
            elif re.search(self.patronGramar, ingreso) or re.search(self.patronGramar2, ingreso):
                self.producciones.append(ingreso)
                for i in ingreso:
                    if i == ">":
                        break
                    else:
                        simbolo = simbolo+i

                prod = ingreso.split(">")
                prod.pop(0)
                prod = prod[0]
                for i in prod:
                    if i.isupper():
                        prod = prod.replace(i,"")
                        
                agregar = ingreso[len(simbolo)+1:(len(ingreso))]
                agregar = agregar.split("|")
                lista = prod.split("|")

                for i in lista:
                    
                    for j in i:
                        if j.isupper():
                            i.replace(j,"")
                    if i in self.terminales or i=="" or i=="épsilon" or i=="epsilon":
                        continue
                    else:
                        terminal = False
                        break        
                if simbolo in self.no_terminales and terminal==True:

                    print("Patrón correcto.")
                    time.sleep(2)
                    simbolo = ""
                    self.mostrar_gramatica(ingreso[0][0],ingreso)
                else:
                    print("El NT o el T no existe.")
                    time.sleep(2)
                    simbolo = ""
                    terminal = True
        
    def mostrar_gramatica(self,letra,ingreso):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de clasificar el tipo de producción entre recursiva por izqui-
            erda o recursiva por derecha.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • letra: El caracter que representa al nt inicial de la producción.                                                    
        • ingreso: La producción.           
        __________________________________________________________________________________
        '''
        nTerminales = self.no_terminales  #Lista con los no terminales
        terminales = self.terminales # Lista con los terminales
        temp = "" #Temporal para guardar las listas
        c1=False #solo no terminal
        c2=False #recursividad por derecha, solo un término
        c3=False #recursividad por derecha, varios términos, termina con no terminales
        c4=False #recursividad por derecha, varios términos, termina con terminal
        c5=False #recursividad por izquierda, solo un término
        c6=False #recursividad por izquierda, varios términos y el último con no terminales
        c7=False #recursividad por izquierda, varios términos y el último es terminal
        c8=False #solo un terminal
        c9=False #ninguna recursividad y varios términos
        c10=False #recursividad por derecha, varios términos, termina con épsilon
        cadena = ingreso.split(">")
        cadena = cadena[1] #Producciones
        if "|" in cadena:
            temp = cadena.split("|")
            primero = temp[0]
            ultimo = temp[len(temp)-1]
            if not "épsilon" in ultimo and not "epsilon" in ultimo:
                if primero[len(primero)-1].isupper(): #Primero mayúscula por derecha
                    if ultimo[len(ultimo)-1].isupper(): #Mayúsculas en el último por derecha
                        c3=True
                    else:
                        c4=True
                if primero[0].isupper(): #Primero mayúsucla por la izquierda
                    if ultimo[0].isupper(): #Mayúscula en el último por izquierda
                        c6=True
                    else:
                        c7=True 
            else:
                c10 = True    
        else:
            if cadena[0].isupper():
                c5=True
            if cadena[len(cadena)-1].isupper():
                c2=True
        if c5 or c6 or c7:
            #print ("Recursividad por izquierda detectada.")
            self.izquierda=True
            if c5==True: #recursividad por izquierda, solo un término
                self.transformarAformato(letra, cadena, 5)
            elif c6==True: #recursividad por izquierda, varios términos y el último con no terminales
                self.transformarAformato(letra, cadena, 6)
            else: #recursividad por izquierda, varios términos y el último es terminal
                self.transformarAformato(letra, cadena, 7)
            
        elif c2 or c3 or c4 or c9 or c10:
            #print ("No se ha detectado recursividad por izquierda.")
            if c2==True: #recursividad por derecha, varios términos, termina con no terminales
                self.transformarAformato(letra, cadena, 2)
            elif c3==True: #recursividad por derecha, varios términos, termina con terminal
                self.transformarAformato(letra, cadena, 3)
            elif c4==True: #recursividad por izquierda, solo un término
                self.transformarAformato(letra, cadena, 4)
            elif c9==True: #Sin recursividad y varios términos
                self.transformarAformato(letra, cadena, 9)
            elif c10==True: #Varios, recursividad por derecha y con épsilon
                self.transformarAformato(letra, cadena, 10)
        elif c2==c3==c4==c5==c6==c7==False:
            if "|" in cadena:
                c9=True
                self.transformarAformato(letra, cadena, 9)
            elif cadena.isupper():
                c1=True
                self.transformarAformato(letra, cadena, 1)
            else:
                c8=True
                self.transformarAformato(letra, cadena, 8)
            
    def transformarAformato(self,letra,producciones,tipo): #Al formato (A>aA) y agregado a pc
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de convertir la producción de la gramática al formato:
            (A,A;a)
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • letra: El caracter que representa al nt inicial.                                                   
        • producciones: Las producciones de un nt.
        • tipo: La clasificación del ingreso, recibiado por el método transformar.
        __________________________________________________________________________________
        '''
        direccion = producciones.split("|")
        if tipo==2:
            nuevo = letra+">"+producciones
            if not nuevo in self.pc:
                self.pc.append(nuevo)
            if not letra in self.diccionario:
                self.diccionario[letra]=0
        elif tipo==3 or tipo==4 or tipo==9:
            for i in direccion:
                nuevo = letra+">"+i
                if not nuevo in self.pc:
                    self.pc.append(nuevo)
            if not letra in self.diccionario:
                self.diccionario[letra]=0
        elif tipo==5:
            nuevo = letra+">"+producciones
            if not nuevo in self.pc:
                self.pc.append(nuevo)
            if not letra in self.diccionario:
                self.diccionario[letra]=1
        elif tipo==6 or tipo==7:
            for i in direccion:
                nuevo = letra+">"+i
                if not nuevo in self.pc:
                    self.pc.append(nuevo)  
                if not letra in self.diccionario:
                    self.diccionario[letra]=1
        elif tipo ==1 or tipo==8:
            nuevo = letra+">"+producciones
            if not nuevo in self.pc:
                self.pc.append(nuevo)
            if not letra in self.diccionario:
                self.diccionario[letra]=0     
        elif tipo==10:
            for i in direccion:
                nuevo = letra+">"+i
                if not nuevo in self.pc:
                    self.pc.append(nuevo)
                if not letra in self.diccionario:
                    self.diccionario[letra]=0       
        #print(self.pc)
        #print(self.diccionario)
                         
        
    def convertirGramatica(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de convertir una gramática recursiva por izquierda a una gra-
            mática recursiva por derecha.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        if self.izquierda == True:
            prod = self.pc
            #print(self.pc)
            listaI = []
            letraI = ""
            nuevo_simbolo = ""
            direccion = []
            ordenada = []
            produccion = ""
            convertidas = []
            for i in prod: #Agregar todas los estados de las producciones
                if not i[0] in listaI:
                    listaI.append(i[0])
            for i in listaI:
                nuevo_simbolo = i+"'"
                if not nuevo_simbolo in self.no_terminales:
                    self.no_terminales.append(nuevo_simbolo)
                    nuevoNodo = Nodo(nuevo_simbolo,0)
                    self.nodos.append(nuevoNodo)
                for j in prod:
                    if i in j[0]:
                        direccion.append(j)
                if self.diccionario[i]==1:
                    tempSin = []
                    tempCon = []                    
                    for j in direccion:
                        temp = j.split(">")

                        if not i in temp[1]:
                            tempSin.append(i+">"+temp[1]+nuevo_simbolo)
                        else:
                            tempCon.append(nuevo_simbolo+">"+temp[1].replace(i,"")+nuevo_simbolo)
                    tempCon.append(nuevo_simbolo+">"+"épsilon")
                    for j in tempSin:
                        convertidas.append(j) 
                    for j in tempCon:
                        convertidas.append(j)   
                else:
                    for i in direccion:
                        convertidas.append(i)
                direccion=[]
            print("Gramática original")
            print(self.producciones)
            print("Gramática transformada")
            self.pc=convertidas
            self.guardar=convertidas
            self.pReporte=convertidas
            print(self.pc)
            self.guardar=self.pc
            input()
            self.transformada = True
        else:
            os.system("cls")
            print("La gramática no posee recursividad por la izquierda")
            self.guardar = self.pc
            print(self.pc)
            input()
            self.transformada = True
    
    def buscar_nodo(self,valor):  
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que busca y retorna un objeto Nodo.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                               
        • valor: El valor que guarda el objeto Nodo.            
        __________________________________________________________________________________
        '''
        if len(valor)>1 and "'" not in valor:
            lista = []
            simbolo = ""
            if "'" in valor:
                simbolo = valor[len(valor)-2]+valor[len(valor)-1]
                valor = valor.replace(simbolo,"")
            for i in valor:
                for j in self.nodos:
                    if i == j.get_valor():
                        lista.append(j)
            return lista
        else:                               
            for i in self.nodos:
                if valor == i.get_valor():
                    return i
                else:
                    continue
        return False
    def get_produccion(self,nt,direccion):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna las producciones de la gramática.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nt: El nt inicial de la producción.                                                    
        • direccion: El nt final de la producción.
        __________________________________________________________________________________
        '''
        for i in self.producciones:
            if nt == i[0] and direccion == i[2]:
                return i 
        return False
                
        
              
    def get_pc(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la lista self.pc                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.pc
    def get_pcN(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la lista self_pcN.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.pcN
    def get_producciones(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la lista self.producciones.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.producciones
    def get_no_terminales(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la lista self_no_terminales.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.no_terminales
    def get_no_terminalesO(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la lista self_no_terminales.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.no_terminales
    def get_nombre(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna el nombre de la gramática.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.nombre
    def get_terminales(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la lista self.terminales.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.terminales
    def get_izquierda(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna el booleano self.izquierda.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.izquierda
    def set_izquierda(self,valor):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que asigna un valor a la variable self.izquierda.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                                                                            
        • valor: Booleano a asignar a la variable.           
        __________________________________________________________________________________
        '''
        self.izquierda=valor
    def get_ntInicial(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la variable self.ntInicial.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.ntInicial
    def get_guardar(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la lista self.guardar.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.guardar
    def get_pReporte(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la lista self.pReporte.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.pReporte
    def get_p2Reportes(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la lista self.p2Reporte.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.p2Reporte
    def agregar_no_terminales(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de agregar nuevos no terminales.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = El valor del no terminal.           
        __________________________________________________________________________________
        '''
        #nuevo = nt(nombre)
        self.no_terminales.append(nombre)
        nuevoNodo = Nodo(nombre,0)
        self.nodos.append(nuevoNodo)
    def agregar_terminal(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de agregar nuevos terminales.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre: El valor del terminal.         
        __________________________________________________________________________________
        '''
        self.terminales.append(nombre)
        nuevoNodo = Nodo(nombre,1)
        self.nodos.append(nuevoNodo)
    def agreger_nt_inicial(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de asignar un nuevo valor a la variable self.ntInicial.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = Nuevo valor a asignar.            
        __________________________________________________________________________________
        '''
        self.ntInicial = nombre
    def agregar_produccion(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de agregar nuevas producciones.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = El valor de la nueva producción.            
        __________________________________________________________________________________
        '''
        self.producciones.append(nombre)
    def agregar_nodo(self,nodo):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de agregar nuevos Nodos.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nodo = El nuevo nodo a agregar.          
        __________________________________________________________________________________
        '''
        self.nodos.append(nodo)
    def set_nombre(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de asignar un nuevo valor al nombre de la gramática.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = Nuevo valor a asignar.          
        __________________________________________________________________________________
        '''
        self.nombre=nombre
    def set_pcN(self,pcn):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de asignarle una nueva lista a self.pcN                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • pcn = Nueva lista a asignar.          
        __________________________________________________________________________________
        '''
        self.pcN = pcn
    def set_producciones(self,producciones):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de asignar una nueva lista a self.producciones.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • producciones = Nueva lista a asignar.           
        __________________________________________________________________________________
        '''
        self.producciones=producciones
    def set_guardar(self,lista):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de asignar una nueva lista a self.guardar.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • lista = Nueva lista a asignar.           
        __________________________________________________________________________________
        '''
        self.guardar=lista
    def get_transformada(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la lista de producciones transformadas.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        return self.transformada     