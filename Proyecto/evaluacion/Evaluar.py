#!/usr/bin/python
# -*- coding: utf-8 -*-

from metodos.Lenguaje import Lenguaje
from metodos.afd import afd
from metodos.Gramatica import Gramatica
from tipos.Tipo import Tipo
from audioop import reverse



class Evaluar(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase encargada de llevar el control de la evaluaciones de cadenas.
    __________________________________________________________________________________
    '''
    contador = 0


    def __init__(self,cadena,lenguaje):
        '''
        __________________________________________________________________________________
        ► Parámetros:
        
        • cadena = El conjunto de caracteres a evaluar.
        • lenguaje = El objeto lenguaje que contiene toda la información necesaria para
            realizar las validaciones.
        __________________________________________________________________________________
        ► Variables:
        
        • self.cadena = Toma el valor de cadena.
        • self.lenguaje =  Toma el valor de lenguaje.
        • self.rutaAFD = Guarda la ruta seguida por el AFD en las validaciones.
        • self.rutaGra = Guarda la expansión de la gramática.
        __________________________________________________________________________________
        '''
        self.cadena = cadena
        self.lenguaje = lenguaje
        self.rutaAfd = ""
        self.rutaGra = ""

    def validarGramatica(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de validar una cadena mediante la gramática del lenguaje.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________

        '''
        
        simbolos = self.lenguaje.get_afd().get_simbolos()
        transiciones = self.lenguaje.get_afd().get_transiciones()
        estados = self.lenguaje.get_afd().get_estados()
        estadoI = self.lenguaje.get_afd().get_estadoI()
        estadoA = self.lenguaje.get_afd().get_estadoA()
        valido = True
        estadoA = 0
        leidos = 0
        direccion = ""
        for i in self.cadena:
            leidos = leidos+1
            if i not in simbolos:
                valido = False
                break
            else:
                for j in transiciones:
                    estadoT = j.replace(";",",")
                    estadoT = estadoT.split(",")
                    if i == estadoT[2]:
                        direccion = estadoT[1]
                        for k in range(0,len(transiciones)):
                            estadoT = transiciones[k].replace(";",",")
                            estadoT = estadoT.split(",")
                            if i == estadoT[2] and direccion == estadoT[1]:
                                valido == True
                                estadoA = k
                                self.rutaAfd = self.rutaAfd+" "+transiciones[k]
                                break
                            else:
                                valido == False
                                continue
                        if valido or valido==False:
                            break
                if not valido:
                    break
        if not valido:
            print("No válido")
        elif valido and (transiciones[2][1] in estadoA or transiciones[2][1]=="-"):
            print("Cadena válida") 
        else:
            print()
            
    def validarAutomata(self,afd):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de validar una cadena por medio del AFD del lenguaje.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • afd = Objeto AFD que contiene toda la información necesaria para la validación.          
        __________________________________________________________________________________
        '''
        estados = afd.get_estados()
        estadoI = afd.get_estadoI()
        estadoA = afd.get_estadoA()
        simbolos = afd.get_simbolos()
        transicion = afd.get_transiciones()
        cadena = self.cadena
        leidos = 0
        direccion = ""
        simbolo = ""
        estadoF = ""
        indice=0
        contador = 0   
        validar = True
        for i in cadena:
            if i in simbolos:
                continue
            else:
                validar = False  
                break   
        while validar:
            try:
                separado = transicion[indice].replace(";",",")
            except:
                break
            separado = separado.split(",")
            if separado[0]==estadoI and contador == 0:
                if separado[2]==cadena[leidos]:
                    leidos=leidos+1
                    direccion = separado[1]
                    indice=0
                    contador = contador+1
                else:
                    indice = indice+1
                    continue
            elif contador>0 and separado[0]==direccion:
                if separado[2] == cadena[leidos]:
                    leidos=leidos+1
                    direccion=separado[1]
                    indice=0
                    contador = contador+1
                else:
                    indice = indice+1
                    continue
            else:
                indice = indice+1
            if leidos == len(cadena) or contador == len(cadena):
                estadoF = separado[0]
                break
        if estadoF in estadoA:
            print("Válido")
        else:
            print("Inválido")
          


#--------------------------------------------------------------------


    def evaluar(self,lista_ini, cadena):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de evaluar cadenas.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • lista_ini: Lista con todas las producciones existentes de un no terminal.                                        
        • cadena: Conjunto de caracteres a evaluar.            
        __________________________________________________________________________________
        '''
        lista_aux = []
        i = 0 #character
        k = 0 #row
        ktemp = 0
        cont = 0
        encontrado = False
        terminalTemp = ""
        self.rutaAfd = "Ruta en AFD: -> "
        ntTemporal = ""
        posicion = 0
        self.rutaGra = "Expresión gramática"
        ultimoNT = ""
        while cont <= len(lista_ini):
            #print(self.rutaAfd)
            #if len(cadena)>i:   #chapus
            if not i == len(cadena):
                for j in range(0,len(lista_ini)-1):
                    if lista_ini[j].get_valor() == cadena[i]:
                        posicion = j
                        i +=1
                        break
                    else:
                        posicion = -1
                
                if posicion != -1:
                    k = posicion+1
                    terminalTempo = lista_ini[k-1].get_valor()
                    ntTemporal = lista_ini[k].get_valor()
                    if self.lenguaje.get_afd().get_transicion(ntTemporal,terminalTempo) == False:
                        self.rutaAfd = self.rutaAfd+self.lenguaje.get_afd().get_transicion("",terminalTempo)
                    else:
                        self.rutaAfd = self.rutaAfd+self.lenguaje.get_afd().get_transicion(ntTemporal,terminalTempo)
                else:
                    print("Cadena inválida")
                    input()
                    return False
            else:
                if ultimoNT in self.lenguaje.get_afd().get_estadoA():
                    print("Cadena válida")
                    input()
                    return True
                for j in lista_ini:
                    if j.get_tipo() == Tipo.EPSILON:
                        print("Cadena válida")
                        input()
                        return True                
                if len(lista_ini) > 1:
                    print ("Cadena inválida")
                    input()
                    return False
                for j in lista_ini:
                    if not j.get_tipo() == Tipo.NOTERMINAL:    
                        print("Cadena válida")
                        input()
                        return True
                    else:
                        print("Cadena inválida")
                        input()
                        return False
                
                

            if lista_ini[k].get_tipo() == Tipo.NOTERMINAL: #si es NT
                #if opt != 3:
                lista = self.lenguaje.get_listaFormateada(lista_ini[k].get_valor())
                ultimoNT = lista_ini[k].get_valor()
                #lista_aux.append(lista_ini) 
                #lista_aux.append(k) #guarda la posición en que se quedó
                lista_ini = lista
                k = 0
                #if opt == 3:
                #    opt = 2
                #else:
                #    opt += 1
                #nodoTemporal
                continue
            if lista_ini[k].get_tipo() == Tipo.TERMINAL: #si es T
                if i < len(cadena) and cadena[i] == lista_ini[k].get_valor():
                    #lista_ini = lista_aux
                    i += 1
                    if len(lista_ini) > 1: #si vienen mï¿½s posiciones en el actual /filas/
                        k += 1
                        cont = 0
                    elif i>=len(cadena):
                        print("Válida")
                        self.lenguaje.agregar_cadenaV(cadena) 
                    else:
                        #verifica si tiene elementos la pila auxiliar
                        if len(lista_aux) > 0:
                            k = lista_aux.pop()
                            lista_ini = lista_aux.pop() #se obtiene lo que tenga la pila
                            if k < len(lista_ini)-1:
                                k += 1   #se suma la siguiente posición en la columna       
                            cont = 0
                    cont += 1
                    continue
                else:
                    if lista_aux != []:
                        #verificar primero si la cadena ya se terminó de leer 
                        if i >= len(cadena):
                            #si la cadena ya terminó sin error entonces empezar a buscar épsilon.
                            ban = False
                            while k < len(lista_ini)-1 :
                                if lista_ini[len(lista_ini)-1].get_tipo()==Tipo.EPSILON:
                                    self.rutaAfd = self.rutaAfd[0:len(self.rutaAfd)-1]
                                    #print(self.rutaAfd)
                                    print("cadena válida.")
                                    ban = True;
                                    break;
                                else:
                                    k = k+1
                            if ban :
                                break;
                            else:
                                print("cadena inválida.")

                        elif len(lista_ini) > 1: #si vienen más posiciones en el actual /filas/
                            k += 1 #porque sino tiene que pasar al siguiente
                            #verificar si la lista auxiliar tiene el mismo NT que el que viene.
                            if lista_aux != [] : #si la lista no está vacío
                                k_tmp = lista_aux.pop() #saca el ultimo k ingresado.
                                lista_tmp = lista_aux.pop() #saca la última lista agregada. 
                                if lista_tmp[k_tmp].get_valor() == lista_ini[k].get_valor(): #es porque ya vino y necesita pasar a la siguiente producción del mismo nivel.
                                    if k_tmp < len(lista_tmp)-1: #se verifica si la lista es mayor a k
                                        k_tmp = k_tmp+1
                                    lista_ini = lista_tmp
                                    k = k_tmp
    #                            elif lista_ini[k].get_tipo() == Tipo.TERMINAL:
    #                                lista_aux.append(lista_tmp)
    #                                lista_aux.append(k_tmp)
    #                                k += 1
                            continue
                        elif len(lista_ini) == 1: #si es uno es porque es solo terminal
                            print("Cadena inválida.2")
                            break; #error 
                    else:
                        print("Cadena inválida.3")  
                        break            
            else:
                if i <= len(cadena) and lista_ini[k].get_tipo()==Tipo.EPSILON:
                    k_k = lista_aux.pop()
                    lista_tmp = lista_aux.pop() 
                    if k_k < len(lista_tmp)-1:
                        k_k = k_k+1          
                    if lista_tmp[k_k].get_valor() == lista_ini[k].get_valor(): #verifica si el NT coincide con el NT de la pila
                        k = k_k
                        lista_ini = lista_tmp  
                    if lista_ini[k].get_tipo() == Tipo.EPSILON and lista_aux == []:
                        k = k_k
                        lista_ini = lista_tmp       
                        
                else:
                    k_k = lista_aux.pop()
                    lista_ini = lista_aux.pop()
                    if k_k < len(lista_ini)-1:
                        k = k_k+1
                    else:
                        k = k_k  
                cont = 0
                continue
            #else:    #chapus
                #break

#----------------------------------------------------------------------
                        
    def get_rutaAFD(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la ruta del AFD generada en la validación.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        return self.rutaAfd
    def get_rutaGramatica(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna la ruta de la gramática generada en la validación.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        return self.rutaGra
    def set_rutas(self,texto):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que asigna un valor a la variable self.rutaAFD y self.rutaGra               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • texto: Variable que puede contener 2 posibles valores: válido o inválido.                                                                
        __________________________________________________________________________________
        '''
        self.rutaAfd = ""
        self.rutaGra = ""
        self.rutaAfd= "Ruta en AFD: -> "+texto
        self.rutaGra= "Expansión en la gramática: -> "+texto
        
    def crear_rutaGra(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método encargado de crear la ruta de la gramática generada por la validación.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        lista = self.rutaAfd.replace("Ruta en AFD: -> ","")
        lista = lista[0:len(lista)-1]
        lista = lista.split(";")
        resultado = ""
        produccion = ""
        tempProd = ""
        direccion = ""
        tempDir = "nadabueno"
        anterior = ""
        for i in lista:
            i = i.split(",")
            
            produccion = i[2]
            direccion = i[1]
            
            
            if (direccion == "-" and i[2][0].islower()) or (direccion == "-" and not i[2][0].isupper() and not i[2][0].islower()):
                if tempDir == "nadabueno":
                    resultado = i[2]
                    tempProd = i[2]
                else:
                    anterior = anterior.replace(tempDir,produccion)
                    resultado = resultado+"->"+anterior
                    
            elif direccion[0].isupper() and produccion[0].isupper() and tempDir in anterior:
                anterior = anterior.replace(tempDir,produccion)
                anterior = anterior.replace(produccion[0],"")
                resultado = resultado+"->"+anterior+i[1]
                anterior = anterior+i[1]
                tempDir = i[1]
                tempProd = i[2]
            elif direccion[0].isupper() and produccion[0].isupper() and not tempDir in anterior:
                i[2] = i[2].replace(produccion[0],tempProd)
                resultado = resultado+"->"+i[2]+i[1]
                anterior = i[2]+i[1]
                tempDir = i[1]       
                tempProd = i[2]        
            elif (direccion[0].isupper() and produccion[0].islower() and tempDir in anterior) or \
            ((not produccion[0].isupper() and not produccion[0].islower()) and direccion[0].isupper() and tempDir in anterior) :
                anterior = anterior.replace(tempDir,i[2])
                resultado = resultado+"->"+anterior+i[1]
                anterior = anterior+i[1]
                tempDir = i[1]       
                tempProd = i[2]         
            elif (direccion[0].isupper() and produccion[0].islower() and tempDir=="nadabueno") or \
            ((not produccion[0].isupper() and not produccion[0].islower()) and direccion[0].isupper() and tempDir=="nadabueno"):
                resultado = resultado+"->"+produccion+direccion
                anterior =produccion+direccion
                tempDir = i[1]
                tempProd= i[2]         
            elif (direccion[0].isupper() and produccion[0].islower() and not tempDir in anterior) or \
            ((not produccion[0].isupper() and not produccion[0].islower()) and direccion[0].isupper() and not tempDir in anterior): 
                anterior = anterior.replace(tempDir,i[2])
                resultado = resultado+"->"+anterior+i[1]
                anterior = anterior+i[1]
                tempDir = i[1]
                tempProd = i[2]
                
        
        if resultado[len(resultado)-1].isupper():
            resultado = resultado[0:len(resultado)-2]
        elif resultado[len(resultado)-1]=="'":
            resultado = resultado[0:len(resultado)-3]
        #print("Esta es la expasión de la gramática\n"+resultado)
        self.rutaGra = "Expansión en gramática: "+resultado
