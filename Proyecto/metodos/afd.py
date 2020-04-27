#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from nodos.Nodo import Nodo
import os
import time

class afd(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase AFD encargada de crear los afd del programa.
    __________________________________________________________________________________
    '''
    patronTransicion = "[A-Z]+,[A-Z|-]+;[\w|-]+"
    patronTransicion2 = "[a-z]+[,]?"
    patronTransicion3 = "[A-Z]+[,]?"
    patronTransicion4 = ";|,"
    separador = ",|;"


    def __init__(self,nombre):
        '''
        __________________________________________________________________________________
        ► Parámetros:
        
        • nombre = el nombre del objeto asignado a la nueva instancia.
        __________________________________________________________________________________
        ► Variables:
        
        • self.nombre = Recibe el valor de nombre.
        • self.estados =  Lista que guarda los estados del afd.
        • self.estadosN = Lista que guarda los Nodos tipo estado del afn.
        • self.simbolos = Lista que guarda los símbolos del afd.
        • self.simbolosN =  Lista que guarda los Nodos tipo símbolo del afd.
        • self.estado_inicial = Guarda el estado inicial del afd.
        • self.estado_inicialN = Guarda el Nodo con estado inicial = True del afd.
        • self.estados_aceptacion =  Lista que guarda los estados de aceptación del afd.
        • self.estados_aceptacionN = Lista que guarda los nodos con estado aceptación = True.
        • self.transiciones = Lista que guarda las transiciones del afd.
        • self.transicionesN = Lista que guarda transiciones de Nodos dle afd.
        
        ► Estáticas:
        
        • separador = Patrón utilizado por el módulo re para el ingreso de datos.
        • patronTransicion = Patrón utilizado por el módulo re para el ingreso de datos.
        • patronTransicion2 =  Patrón utilizado por el módulo re para el ingreso de datos.
        • patronTransicion3 = Patrón utilizado por el módulo re para el ingreso de datos.  
        • patronTransicion4 = Patrón utilizado por el módulo re para el ingreso de datos.     
        __________________________________________________________________________________
        '''
        self.nombre = nombre
        self.estados = []
        self.estadosN = []
        self.simbolos = []
        self.simbolosN = []
        self.estado_inicial = ""
        self.estado_inicialN = ""
        self.estados_aceptacion= []
        self.estados_aceptacionN = []
        self.transiciones=[]
        self.transicionesN=[]
        
        
    
    def ingresar_estados(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de solicitar y guardar estados.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        while (True):
            os.system("cls")
            print ('Ingrese el estado deseado:')
            print(">> ", end="")
            estado = input()
            if estado.isupper():
                if estado in self.estados:
                    print('Estado repetido.')
                    time.sleep(2)
                elif estado== "":
                    print (self.estados)
                    break
                else:
                    #self.estados.append(estado)
                    self.agregar_estados(estado)
            elif estado == "":
                print("Estados ingresados.")
                time.sleep(2)
                break
            else:
                print("Error, los estados tienen que ir en mayúscula.")
                time.sleep(2)
                
            
    def ingresar_gramatica(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado solicitar y guardar los símbolos del afd.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        while (True):
            os.system("cls")
            print('Ingrese el símbolo deseado:')
            print(">> ", end="")
            simbolo = input()
            if simbolo.islower() or re.search("[0-9]+",simbolo):
                if simbolo in self.simbolos:
                    print('Símbolo repetido.')
                    time.sleep(2)
                elif simbolo== "":
                    print (self.simbolos)
                    break
                else:
                    #self.simbolos.append(simbolo)   
                    self.agregar_simbolos(simbolo)
                      
            elif simbolo == "":
                print("Símbolos ingresados.")
                time.sleep(2)
                break
            else:
                print("Error, los símbolos tienen que ir en minúscula o ser números.")   
                time.sleep(2)
     
    def festado_inicial(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de solicitar y asignar el estado inicial.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        while (True):
            os.system("cls")
            print('Ingrese el estado deseado:')
            print(">> ", end="")
            estado = input()
            if estado.isupper():
                if estado in self.estados:
                    #self.estado_inicial = estado
                    self.agregar_estadoI(estado)
                    print("Estado ingresado.")
                    time.sleep(2)
                    break
                elif estado == "":
                    print("No se ingreso ningún estado inicial.")
                    time.sleep(2)
                else:
                    print ("El estado: ",estado," no existe \
                    \n Intentelo de nuevo con otro estado que exista.")
                    time.sleep(2)
            elif estado =="":
                break
            else:
                print("Error, el estado tiene que estar escrito en mayúsucla.")
                time.sleep(2)
            
    def festado_aceptacion(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de solicitar y guardar los estados de aceptación.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        while (True):
            os.system("cls")
            print('Ingrese el estado deseado:\n')
            print(">> ", end="")
            estado = input()
            if estado.isupper():
                if estado in self.estados and not estado in self.estados_aceptacion:
                    #self.estados_aceptacion.append(estado)
                    self.agregar_estadoA(estado)
                elif estado == "":
                    print("\n")
                else:
                    print ("El estado: ",estado," no existe o ya es de aceptación \
                    \n Intentelo de nuevo con otro estado que exista.")   
                    time.sleep(2)
            elif estado == "":
                print("Estados ingresados.")
                time.sleep(2)
                break
            else:
                print("Error, el estado tiene que estar escrito en mayúscula.") 
                time.sleep(2)    
                                
    
    def ingresar_transicion(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de solicitar y guardar las transiciones del afd.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        os.system("cls")
        print("Seleccione el modo de ingreso de datos 1|2")
        print(">> ", end="")
        opcion = int(input())
        if opcion==1:
            while (True):
                os.system("cls")
                print("Ingrese la transición:")
                print(">> ", end="")
                cadena = input()
                transicion = re.findall(self.patronTransicion,cadena)
                if re.search(self.patronTransicion,cadena):
                    print ("Patrón correcto.")
                    #print(cadena)
                    repetido = False
                    temp = re.split(self.separador,cadena)
                    if temp[0] in self.estados and (temp[1] in self.estados or temp[1]=="-" )\
                    and (temp[2] in self.simbolos or temp[1]=="-"):
                        for i in self.transiciones:
                            #print(i)
                            t = i.replace(";",",")
                            t = t.split(",")
                            if temp[0]==t[0] and temp[1]==t[1] and temp[2]==t[2]:
                                print("Transición repetida.")
                                time.sleep(2)
                                repetido = True
                                break
                            else:
                                continue
                        if not repetido:
                            self.transiciones.append(cadena)
                            nodo1 = self.buscar_nodo(temp[0])
                            nodo2 = self.buscar_nodo(temp[1])
                            nodo3 = self.buscar_nodo(temp[2])
                            self.agregar_transicionesN([nodo1,nodo2,nodo3])
                            print("Agregado.")
                            time.sleep(2)
                            #print(self.transiciones)
                        else:
                            continue
                            
                    else:
                        print("Los símbolos ingresados no pertenecen a la gramática o a los estados existentes.")
                        time.sleep(3)
                        os.system("cls")
                elif cadena == "":
                    #print(self.transiciones)
                    print("Transiciones ingresadas.")
                    time.sleep(2)
                    break
                else:
                    print("Patrón ingresado incorrecto.")
                    time.sleep(2)
        elif opcion==2:
            lista = ""
            print("Ingrese terminales")
            print(">> ", end="")
            ingreso = input()
            terminales = re.findall(self.patronTransicion2,ingreso)
            for s in range(0,len(terminales)):
                terminales[s] = terminales[s].replace(",","") 
            print("Ingrese no terminales")
            print(">> ", end="")       
            ingreso = input()
            no_terminales = re.findall(self.patronTransicion3,ingreso)
            for s in range(0,len(no_terminales)):
                no_terminales[s] = no_terminales[s].replace(",","")              
            while True:
                print("Ingrese símbolos de destino")
                print(">> ", end="")
                ingreso = input()
                simbol = re.split(self.patronTransicion4,ingreso)
                lista = lista+"".join(simbol)
                #if len(simbol)%2==0:
                if len(terminales)*len(no_terminales)==len(simbol):
                    break
                else:
                    print("Error, el formato es inválido.")
                    time.sleep(2)
            #simbol = re.split(self.separador, lista)
            #for i in range(0,len(simbol)):
            #    if simbol[i]=="":
            #        simbol.pop(i)                                       
            if self.validar_transicion(terminales,0):
                print("Validados los terminales.")
                if self.validar_transicion(no_terminales, 1):
                    print("Validados los no terminales.")
                    if self.validar_transicion(simbol, 2):
                        #print(simbol)
                        print("Transiciones válidas.")
                        self.convertir_transicion(no_terminales, terminales, simbol)
                        
                    else:
                        print("Transiciones no válidas.")
                else:
                    print("No terminales inválidos.")
            else:
                print("Terminales no válidos.")
            #print(lista)
            #print(simbol)
            #print(self.estados)
            #print(self.estado_inicial)
            #print(self.estados_aceptacion)
                    
            
        else:
            print("Opción no disponible.")
            time.sleep(2)
      
      
            
    def convertir_transicion(self,nt,t,tran):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de convertir las transiciones al formato (A,A;a)
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nt: El estado padre.                                                 
        • t: El terminal.
        • tran: El estado hijo.
        __________________________________________________________________________________
        '''
        contador = 0
        temp = tran
        lista = []
        for i in nt:
            conversion = i+","
            nodo1 = self.buscar_nodo(i)
            for j in temp:
                if contador == len(t):
                    temp = temp[contador:]
                    break
                else:
                    lista.append(conversion+j+";"+t[contador])  
                    nodo2 = self.buscar_nodo(j)
                    nodo3 = self.buscar_nodo(t[contador])
                    self.transiciones.append(conversion+j+";"+t[contador])
                    self.agregar_transicionesN([nodo1,nodo2,nodo3])
                    contador = contador+1
            contador = 0
        print (lista)
                
            
        
    def validar_transicion(self,lista,tipo):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de validar si las transiciones son correctas.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • lista: La lista con todos las transiciones del afd.                                                 
        • tipo: El tipo de objeto, ya sea estado o símbolo.
        __________________________________________________________________________________
        '''
        contador = 0
        if tipo==0:
            for ob in lista:
                for ob2 in self.simbolos:
                    if ob == ob2:
                        contador +=1           
        elif tipo==1:
            for ob in lista:
                for ob2 in self.estados:
                    if ob == ob2:
                        contador +=1
        else:
            for ob in lista:
                for ob2 in self.estados:
                    if ob == ob2 or ob == "-":
                        contador +=1
                        break
        if contador == len(lista):
            return True
        else:
            return False
     
    def get_transicion(self,inicio,fin):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna las transiciones solicitadas en una lista (Ep,Ei,S)
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • inicio: El estado padre.                                                   
        • fin: El estado hijo.
        __________________________________________________________________________________
        '''
        for i in self.transiciones:
            j = i.replace(";",",")
            j = j.split(",")
            if j[0]==inicio and fin in j[2] :
                return i.replace(";",",")+";"
            if inicio == "" and fin in j[2]:
                return i.replace(";",",")+";"
        return False
       
    def agregar_simbolos(self,simbolo):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de agregar nuevos símbolos.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • simbolo = Valor a agregar.
        __________________________________________________________________________________
        '''
        self.simbolos.append(simbolo)
        nodo = Nodo(simbolo,3)
        self.simbolosN.append(nodo)
    def get_simbolos(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista de símbolos del afd.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        return self.simbolos
    def get_simbolosN(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista de Nodos tipo símbolo del afd.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        return self.simbolosN
    def get_estados(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista de estados del afd.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        return self.estados
    def get_estadosN(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista de nodos tipo estado del afd.             
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        return self.estadosN
    def get_transiciones(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista de transiciones del afd.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        return self.transiciones
    def get_transcicionesN(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista de transiciones de nodos del afd.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        return self.transicionesN
    def get_estadoI(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar el estado inicial del afd.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        return self.estado_inicial
    def get_estadoIN(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar el nodo con el valor de estado inicial del afd.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        return self.estado_inicialN
    def get_estadoA(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista con los estados de aceptación del afd.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        return self.estados_aceptacion
    def get_estadoAN(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar la lista de nodos con valor de estado de aceptación.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        return self.estados_aceptacionN
    def get_nombre(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar el nombre del afd.             
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        return self.nombre
    def set_nombre(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de asignar un nombre al afd.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = Nuevo valor a asignar.
        __________________________________________________________________________________
        '''
        self.nombre = nombre
    def agregar_estados(self,estado):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de agregar nuevos estados al afd.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • estado = Nuevo valor a agregar.
        __________________________________________________________________________________
        '''
        self.estados.append(estado)
        nodo = Nodo(estado,2)
        self.estadosN.append(nodo)
    def agregar_estadoI(self,estado):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de asignar un nuevo estado Inicial.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • estado = Estado a asignar a estado inicial.
        __________________________________________________________________________________
        '''
        self.estado_inicial = estado
        nodo = self.buscar_nodo(estado)
        self.estado_inicialN = nodo 
    def agregar_estadoA(self,estado):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de agregar nuevos estados de aceptación.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • estado = Estado a agregar a la lista de estados de aceptación.
        __________________________________________________________________________________
        '''
        self.estados_aceptacion.append(estado)
        nodo = self.buscar_nodo(estado)
        self.estados_aceptacionN.append(nodo)
    def agregar_transiciones(self,transicion):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de agregar nuevas transiciones.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • transicion = Nueva transición a agregar.
        __________________________________________________________________________________
        '''
        self.transiciones.append(transicion)
    def agregar_transicionesN(self,lista):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de agregar una nueva transición en formato de Nodos.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • lista = Lista de las transiciones en formato Nodo.
        __________________________________________________________________________________
        '''
        self.transicionesN.append(lista)
    def buscar_nodo(self,estado):  
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de retornar un nodo buscado.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • lista = lista con todos los nodos existentes.
        __________________________________________________________________________________
        '''
        for i in self.estadosN:
            if i.get_valor()==estado:
                return i 
        return False
    def set_transiciones(self,lista,listaN):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de asignar un nuevo valor a self.transiciones y su versión Nodo.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • lista = Lista con las nuevas transiciones.
        • listaN = Lista con las nuevas transiciones en formato Nodo.
        __________________________________________________________________________________
        '''
        self.transiciones=lista
        self.transicionesN=listaN
    def actualizar_estado(self,estado):
        print()
        