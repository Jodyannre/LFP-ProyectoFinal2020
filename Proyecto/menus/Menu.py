#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
import sys
from metodos.afd import afd
from metodos.Gramatica import Gramatica
from metodos.Lenguaje import Lenguaje
from evaluacion.Evaluar import Evaluar
from lectores.LectorLenguaje import LectorLenguaje
from reportes.Grafo import Grafo
from reportes.Pdf import Pdf
from metodos.GramaticaE import GramaticaE
from PIL import Image
from evaluacion.EvaluarT2 import EvaluarT2



class Menu(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase que contiene todos los menús principales del programa.
    __________________________________________________________________________________
    '''
    
    
    def __init__(self):
        '''
        __________________________________________________________________________________
        ► Parámetros:
        
            (Sin parámetros)
        __________________________________________________________________________________
        ► Variables:
        
        • self.gramatica = Lista que guarda todas las gramátias creadas.
        • self.afd =  Lista que guarda todos los AFD creados.
        • self.Lenguaje = Lista que guarda todos los lenguajes generados.
        • self.afdCargado = Booleano que indica si se encuentra cargado un AFD.
        • self.graCargado =  Booleano que indica si se encuentra cargada una gramática.
        • self.ValidacionCadena = Booleano que indica el estado de la validación de la ca-
            dena.
        • self.gramaticaE = Lista que guarda todas las gramáticas tipo 2.
        __________________________________________________________________________________
        '''
        self.gramaticas = []
        self.afd = []
        self.Lenguaje = []
        self.gramaticaE = []
        self.afdCargado = False
        self.graCargado = False
        self.validacionCadena = False
    
          
    def caratula(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Carátula del programa.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        os.system("cls")
        print("**********************************************") 
        print("*                                            *")
        print("*  Lenguajes formales y de programación      *")
        print("*              Sección: B+                   *")
        print("*              Carné: 201115018              *")
        print("**********************************************\n")
        print("        Presione enter para continuar         ")     
        print(">> ", end="")
        input()
        
    
    def menu_Inicio(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Menú principal.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        print("****************************************") 
        print("*                                      *")
        print("*  ¡Bienvenidos al menú principal      *")
        print("*                                      *")
        print("****************************************\n")
        print("Ingrese uno de las opciones para continuar\n")
        print("****************************************")
        print("*1 - Crear AFD                         *")
        print("*2 - Crear Gramática                   *")
        print("*3 - Evaluar cadenas                   *")
        print("*4 - Cargar archivo de entrada         *")
        print("*5 - Guardar                           *")
        print("*6 - Reportes                          *")                
        print("*7 - Salir                             *")
        print("*8 - Gramáticas tipo 2 y AP            *")        
        print("****************************************")        
        print(">> ", end="")
        a = input()
       
        return a
    
    def menu_AFD(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Menú del AFD. Utiliza los métodos de la clase AFD para operar.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        a = 0
        os.system("cls")
        print ("Ingrese el nombre para la AFD:")
        print(">> ", end="")
        nombre = input()
        gramatica = self.encontrar(nombre)
        if gramatica == False:
            iafd = afd(nombre)
            iLenguaje = Lenguaje(nombre)
            self.afd.append(iafd)
        else:
            iafd = gramatica.get_afd()
            print(iafd.get_estadoA())
            print(iafd.get_estadoI())
            print(iafd.get_estados())
            print(iafd.get_simbolos())
            print(iafd.get_transiciones())
        while (a!=7):
            os.system("cls")
            print("****************************************") 
            print("*                                      *")
            print("*             ¡Menú AFD                *")
            print("*                                      *")
            print("****************************************\n")
            print("Ingrese uno de las opciones para continuar\n")
            print("****************************************")
            print("*1 - Ingresar estados                  *")
            print("*2 - Ingresar alfabeto                 *")
            print("*3 - Estado inicial                    *")
            print("*4 - Estados de aceptación             *")
            print("*5 - Transiciones                      *")
            print("*6 - Ayuda                             *")        
            print("*7 - Regresar al menú principal        *")         
            print("****************************************")        
            print(">> ", end="")
            a = input()
            if a=="1":
                iafd.ingresar_estados()
            elif a=="2":
                iafd.ingresar_gramatica()
            elif a=="3":
                iafd.festado_inicial()
            elif a=="4":
                iafd.festado_aceptacion()
            elif a=="5":
                iafd.ingresar_transicion()
            elif a=="6":
                os.system("cls")
                print ("Lenguajes formales y de programación \nSección: B \nAuxiliar: José Véliz \n")
                input()
            elif a=="7":
                break
            else:
                print("Opción no disponible.")
                time.sleep(2)
        if gramatica == False:          
            iLenguaje.set_afd(iafd)      
            self.Lenguaje.append(iLenguaje)      
    
    def menu_Gramatica(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Menú gramática. Utiliza los métodos de la clase Gramatica par operar.              
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)
        __________________________________________________________________________________
        '''
        a = 0
        os.system("cls")
        print ("Ingrese el nombre para la gramática:")
        print(">> ", end="")
        nombre = input()
        gramatica = self.encontrar(nombre)
        if gramatica == False:
            igramar = Gramatica(nombre)
            iLenguaje = Lenguaje(nombre)
            self.gramaticas.append(igramar)  
        else:
            igramar = gramatica.get_gramatica()
        while (a!=7):
            os.system("cls")
            print("****************************************") 
            print("*                                      *")
            print("*           ¡Menú gramática            *")
            print("*                                      *")
            print("****************************************\n")
            print("Ingrese uno de las opciones para continuar\n")
            print("****************************************")
            print("*1 - Ingresar NT                       *")
            print("*2 - Ingresar terminales               *")
            print("*3 - NT inicial                        *")
            print("*4 - Producciones                      *")
            print("*5 - Mostrar gramática transformada    *")
            print("*6 - Ayuda                             *")   
            print("*7 - Regresar al menú principal        *")              
            print("****************************************")        
            print(">> ", end="")
            a = input()
            if a=="1":
                igramar.ingreso_no_terminales()
            elif a=="2":
                igramar.ingreso_terminales()
            elif a=="3":
                igramar.ingreso_ntInicial()
            elif a=="4":
                igramar.ingreso_producciones()
            elif a=="5":
                os.system("cls")
                if igramar.get_transformada():
                    if igramar.get_izquierda():
                        print("Gramática original")
                        print(igramar.get_producciones())   
                        print()
                        print("Gramática transformada")
                        print(igramar.get_pc())
                        input()
                    else:
                        print("Gramática original")
                        print(igramar.get_producciones())   
                        input()  
                
                else:        
                    igramar.convertirGramatica()
            elif a=="6":
                os.system("cls")
                print ("Lenguajes formales y de programación \nSección: B \nAuxiliar: José Véliz \n")
                input()
            elif a=="7":
                break
            else:
                print("Opción no disponibles.")
                time.sleep(2)
        if gramatica == False:
            iLenguaje.set_grammar(igramar)      
            self.Lenguaje.append(iLenguaje)      
    
    def menu_Evaluar_Cadena(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Menú evaluación de cadena. Utiliza los métodos de la clase Evaluar para operar.                
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)          
        __________________________________________________________________________________
        '''
        os.system("cls")
        a = 0
        salir= False
        while True:
            os.system("cls")
            print ("Ingrese el nombre de la gramática:")
            print(">> ", end="")
            nombre = input()
            gramatica = self.encontrar(nombre)
            if gramatica == False:
                print("Gramática inexistente.")
                time.sleep(2)
            else:
                if gramatica.get_evaluar()== False:
                    gramatica.obtener_lista_nt(gramatica.get_gramatica().get_ntInicial())
                    gramatica.set_evaluar(True)
                    break
                elif gramatica.get_evaluar()==True:
                    break
                else:
                    print("Error lamentable.")
            if nombre == "":
                salir = True
                break
        
        while (a!=7 and salir==False):
            os.system("cls")
            print("****************************************") 
            print("*                                      *")
            print("*   ¡Menú de evaluación de cadenas     *")
            print("*                                      *")
            print("****************************************\n")
            print("Ingrese uno de las opciones para continuar\n")
            print("****************************************")
            print("*1 - Solo validar                      *")
            print("*2 - Ruta de AFD                       *")
            print("*3 - Expandir con gramática            *")
            print("*4 - Ayuda                             *")
            print("*7 - Regresar al menú principal        *")                
            print("****************************************")        
            print("Ingrese una opción para continuar:")
            print(">> ", end="")
            a = input() 
            if a == "1":
                os.system("cls")
                print("Ingrese cadena para comprobar:")
                print(">> ", end="")
                cadena = input()
                e = Evaluar(cadena, gramatica)
                lista_ini= gramatica.get_listaFormateada(gramatica.get_gramatica().get_ntInicial())
                validacionCadena = e.evaluar(lista_ini, cadena) 
                if validacionCadena:
                    gramatica.agregar_cadenaV(cadena)
                else:
                    gramatica.agregar_cadenaI(cadena)   
                try:            
                    e.crear_rutaGra()
                except:
                    e.set_rutas("Inválido")
            elif a == "2":
                os.system("cls")
                if validacionCadena:
                    print(e.get_rutaAFD()+" --Válida")
                else:
                    print(e.get_rutaAFD()+" --Inválida")
                input()
            elif a == "3":
                os.system("cls")
                if validacionCadena:
                    print(e.get_rutaGramatica()+ " --Válida")
                else:
                    print(e.get_rutaGramatica()+ " --Inválida")
                input()
            elif a == "4":
                os.system("cls")
                print ("Lenguajes formales y de programación \nSección: B \nAuxiliar: José Véliz \n")
                input()
            elif a == "7":
                break
            else:
                os.system("cls")
                print("Opción no disponible.")
                time.sleep(2)
                


    def menu_Cargar_Archivo(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Menú carga de Archivos. Utiliza los métodos de la clase LectorLenguaje para ope-
            rar.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        a = 0
        while (a!=7):
            os.system("cls")
            print("****************************************") 
            print("*                                      *")
            print("*   ¡Menú de carga de archivos         *")
            print("*                                      *")
            print("****************************************\n")
            print("Ingrese uno de las opciones para continuar\n")
            print("****************************************")
            print("*1 - Cargar archivo AFD                *")
            print("*2 - Cargar archivo GMR                *")
            print("*3 - Cargar archivo GMR Tipo 2         *")
            print("*7 - Regresar al menú principal        *")        
            print("****************************************")        
            print("Ingrese una opción para continuar:")
            print(">> ", end="")
            a = input()
            if a== "1":
                iLenguaje = Lenguaje("nada")
                lector = LectorLenguaje("nuevo",self.Lenguaje)
                archivo = lector.cargar(0)
                if lector.get_afdAgregado():
                    iLenguaje.set_afd(lector.get_afd())    
                    iLenguaje.set_nombre(lector.get_afd().get_nombre())  
                    self.Lenguaje.append(iLenguaje)                      
            elif a == "2":
                iLenguaje = Lenguaje("nada")
                lector = LectorLenguaje("nuevo",self.Lenguaje)
                archivo = lector.cargar(1)      
                if lector.get_gramaticaAgregada():
                    iLenguaje.set_grammar(lector.get_gramatica()) 
                    iLenguaje.set_nombre(lector.get_gramatica().get_nombre())   
                    self.Lenguaje.append(iLenguaje)  
                    
                    #print("Obtener lista de producciones.")
                    #print(iLenguaje.obtener_lista_nt("A")) 
                    #print(iLenguaje.get_listaFormateada("A"))  
                    #print(iLenguaje.get_listaFormateada("A'")) 
                    #print(iLenguaje.get_listaFormateada("B")) 
                    #print(iLenguaje.get_listaFormateada("B'")) 
                    #print(iLenguaje.get_listaFormateada("D"))   
            elif a == "3":
                lector = LectorLenguaje("nuevo")
                lector.cargaTipo2()
                self.gramaticaE.append(lector.get_Tipo2())
                print("Gramática cargada con éxito.")
                input()
            elif a == "7":
                break
            else:
                os.system("cls")
                print("Opción no disponible.")  
                time.sleep(2)
 

    def menu_Guardar(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Menú guardar. Utiliza los métodos de la clase Guardar para operar.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        while True:
            os.system("cls")
            print("¿Qué desea guardar?\n 1.Gramática\n 2.AFD")
            print(">> ", end="")
            tipo = input()
    
            print ("Ingrese el nombre de la gramática o el AFD:")
            print(">> ", end="")
            nombre = input()
            
            print ("Ingrese el nombre que tendrá el archivo a guardar:")     
            print(">> ", end="")
            nombreArchivo = input()
            
            if tipo=="" or nombre=="" or nombreArchivo=="":
                time.sleep(1)
                break
            else:
                ilenguaje = self.encontrar(nombre)
                if ilenguaje != False:
                    if tipo == "1":
                        #print("Gramática")
                        ilenguaje.guardar(1,nombreArchivo)
                        print("Archivo guardado con éxito.")
                        time.sleep(2)
                        break
                    elif tipo == "2":
                        #print("AFD")
                        ilenguaje.guardar(0,nombreArchivo)
                        print("Archivo guardado con éxito.")
                        time.sleep(2)
                        break
                    elif tipo == "":
                        print("Regresando al menú.")
                        time.sleep(2)
                        break
                        
                    else:
                        os.system("cls")
                        print("Opción no disponible.")
                        time.sleep(2)
                else:
                    os.system("cls")
                    print("Esa gramática o AFD no existe.")
                    time.sleep(2)
                
        
    
    def menu_Reporte(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Menú reportes. Utiliza los métodos de la clase Reporte para operar.               
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)            
        __________________________________________________________________________________
        '''
        a = 0
        ilenguaje = Lenguaje("nada")
        afd = False
        gramatica = False
        encontrado = False
        os.system("cls")
        print("Qué desea utilizar para continuar: \n1.Gramática\n2.AFD")
        print(">> ", end="")
        a = input()
        while True:
            if a == "1":
                os.system("cls")
                print ("Ingrese el nombre de la gramática para continuar:")
                print(">> ", end="")
                nombre = input()      
                ilenguaje = self.encontrar(nombre) 
                gramatica = True  
                if ilenguaje == False and nombre != "":
                    print("La gramática no existe.") 
                    time.sleep(2) 
                elif ilenguaje ==False and nombre =="":
                    time.sleep(1)
                    return
                else:
                    encontrado = True
                    break     
            elif a == "2":
                os.system("cls")
                print("Ingrese el nombre del AFD para continuar:")
                print(">> ", end="")
                nombre = input()
                ilenguaje = self.encontrar(nombre)
                afd = True
                if ilenguaje == False and nombre !="":
                    print("El AFD no existe.")
                    time.sleep(2)
                elif ilenguaje ==False and nombre =="":
                    time.sleep(1)
                    return
                else:
                    encontrado = True
                    break                
            elif a == "":
                os.system("cls")
                print("Regresando al menú principal...")
                time.sleep(2)
                break
            else:
                os.system("cls")
                print("Opción no disponible")
                time.sleep(2)
        while (a!=7 and encontrado):
            os.system("cls")
            print("****************************************") 
            print("*                                      *")
            print("*         ¡Menú de reportes            *")
            print("*                                      *")
            print("****************************************\n")
            print("Ingrese uno de las opciones para continuar\n")
            print("****************************************")
            print("*1 - Ver detalle                       *")
            print("*2 - Generar reporte                   *")
            print("*3 - Ayuda                             *")    
            print("*7 - Regresar al menú principal        *")            
            print("****************************************")  
            objeto = ""
            if afd:
                objeto = ilenguaje.get_afd()
            else:
                objeto = ilenguaje.get_gramatica()
                      
            print("Ingrese una opción para continuar:")
            print(">> ", end="")
            a = input()
            
            if a == "1":
                if afd:
                    os.system("cls")
                    print("Detalles del afd :"+objeto.get_nombre())
                    print()
                    print("Alfabeto: ")
                    print(objeto.get_simbolos())
                    print()
                    print("Estados: ")
                    print(objeto.get_estados())
                    print()
                    print("Estado inicial: ")
                    print(objeto.get_estadoI())
                    print()
                    print("Estados de aceptación")
                    print(objeto.get_estadoA())
                    print()
                    print("Transiciones: ")
                    for i in objeto.get_transiciones():
                        print(i)
                    input()
                    
                elif gramatica:
                    os.system("cls")
                    print("Detalles de la gramática :"+objeto.get_nombre())
                    print()
                    print("No terminales: ")
                    print(objeto.get_terminales())
                    print()
                    print("Terminales: ")
                    print(objeto.get_no_terminales())
                    print()
                    print("Inicio: ")
                    print(objeto.get_ntInicial())
                    print()
                    print("Producciones: ")
                    for i in objeto.get_guardar():
                        print(i)
                    input()                
                else:
                    continue
            elif a == "2":
                os.system("cls")
                g = Grafo("nuevo")
                g.agregar_datos(ilenguaje.get_afd().get_transiciones(), ilenguaje.get_afd().get_estados() \
                                ,ilenguaje.get_afd().get_simbolos() , ilenguaje.get_afd().get_estadoA(), ilenguaje.get_afd().get_estadoI())
                g.graficar()
                print("Creando......")
                time.sleep(2)
                pdf = Pdf(ilenguaje)
                pdf.crear_reporte()
                print("Reporte creado con éxito.")
                time.sleep(2)
            elif a == "3":
                os.system("cls")
                print ("Lenguajes formales y de programación \nSección: B \nAuxiliar: José Véliz \n")
                input()
            elif a == "7":
                break
            else:
                os.system("cls")
                print("Opción no disponible.")
                time.sleep(2)
            
            
            
    def encontrar(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que busca y retorna un lenguaje que se encuentre dentro de la lista len-
            guajes.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = El nombre del lenguaje a buscar.            
        __________________________________________________________________________________
        '''
        for i in self.Lenguaje:
            if nombre == i.get_nombre():
                return i
            else:
                continue
        return False
    
    def repetido(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que valida si un nombre de gramática, AFD o lenguaje ya se encuentra en 
            uso.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre = El nombre a validar.          
        __________________________________________________________________________________
        '''
        for i in self.Lenguaje:
            if nombre == i.get_nombre():
                return True
            else:
                continue
        return False   
    
    def gramaticaTipo2(self):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que inicializa el menú de la gramática tipo 2.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • (Sin parámetros)          
        __________________________________________________________________________________
        '''
        os.system("cls")
        g = GramaticaE("nuevo")
        encontrada = False
        print("Ingrese nombre de la gramática")
        print(">> ", end="")
        nombre = input()
        for i in self.gramaticaE:
            if nombre == i.getNombre():
                g = i
                encontrada = True
                break
            else:
                continue
        if not encontrada:
            g.setNombre(nombre)
            self.gramaticaE.append(g)
        while (True):
            os.system("cls")
            print("****************************************") 
            print("*                                      *")
            print("*        ¡Menú gramática tipo 2        *")
            print("*                                      *")
            print("****************************************")
            print("Ingrese uno de las opciones para continuar")
            print("****************************************")
            print("*1 - Ingresar/modificar gramática      *")
            print("*2 - Generar autómata de pila          *")
            print("*3 - Visualizar autómata               *")
            print("*4 - Validar cadena                    *")
            print("*5 - Ayuda                             *")   
            print("*7 - Regresar al menú inicio           *")  
            print("*8 - Salir de la aplicación            *")            
            print("****************************************")        
            print(">> ", end="")
            a = input()  
            if a == "1":
                self.ingresarGramatica2(g)
            elif a == "2":
                os.system("cls")
                g.crearAutomata()
                g.getAutomata().getGrafo().graficar()
                time.sleep(1)
                print("Autómata creado.")
                print("Enter para continaur.")
                input()
            elif a == "3":
                os.system("cls")
                i = Image.open("./Grafo_Automata.gv.png")
                i.show()
                print("Estados:")
                print(g.getAutomata().get_estados())
                print("Estados finales:")
                print(g.getAutomata().get_estadoA())
                print("Estado inicial:")
                print(g.getAutomata().get_estadoI())
                print("Símbolos de pila:")
                print(g.getAutomata().get_simbolosPila())
                print("Alfabeto:")
                print(g.getAutomata().get_alfabeto())
                print("Transiciones:")
                print(g.getAutomata().get_transiciones())
                print()
                print("Enter para continuar.")
                input()
            elif a == "4":
                self.validarTipo2(g)
            elif a == "5":
                print()
            elif a == "7":
                break
            elif a == "8":
                sys.exit()
            else:
                print("Opción no disponibles")
                input()
                    
    def ingresarGramatica2(self,gramaticaE):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que inicializa el menú del ingreso o modificación de una gramática T2.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • gramaticaE = La gramática creada con el nombre ingresado en el inicio.          
        __________________________________________________________________________________
        '''
        while (True):
            os.system("cls")
            print("****************************************") 
            print("*                                      *")
            print("*    ¡Ingresar/modificar gramática     *")
            print("*                                      *")
            print("****************************************")
            print("Ingrese uno de las opciones para continuar")
            print("****************************************")
            print("*1 - Ingresar terminales               *")
            print("*2 - Ingresar no terminales            *")
            print("*3 - Ingresar producciones             *")
            print("*4 - Borrar producciones               *")
            print("*5 - No terminal inicial               *")   
            print("*7 - Regresar al menú inicio           *")  
            print("*8 - Salir de la aplicación            *")            
            print("****************************************")        
            print(">> ", end="")
            a = input()  
            if a == "1":
                gramaticaE.ingreso_terminales()
            elif a == "2":
                gramaticaE.ingreso_nt()
            elif a == "3":
                gramaticaE.ingreso_producciones()
            elif a == "4":
                gramaticaE.eliminar_producciones()
            elif a == "5":
                gramaticaE.ingreso_ntInicial()
            elif a == "7":
                break
            elif a == "8":
                sys.exit()
            else:
                print("Opción no disponibles")
                input()  
    def validarTipo2(self,gramatica):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que inicializa el menú para validación de gramática tipo 2.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • (Sin parámetros)          
        __________________________________________________________________________________
        '''
        os.system("cls")
        cadena = ""
#        while(True):
#            os.system("cls")
#            print("Ingrese nombre de la gramática")
#            print(">> ", end="")
#            nombre = input()
#            if nombre == "":
#                print("Regresando al menú anterior.")
#                time.sleep(2)
#                break
#            g = self.getGT2(nombre)
#            if g== False:
#                print("Gramática inexistente.")
#                input()
#            else:
#                print("Cargada la gramática:"+nombre)
#                input()
#                break
        while(True):
            os.system("cls")
            print("****************************************") 
            print("*                                      *")
            print("*         ¡Validar cadena              *")
            print("*                                      *")
            print("****************************************")
            print("Ingrese uno de las opciones para continuar")
            print("****************************************")
            print("*1 - Ingresar cadena                   *")
            print("*2 - Resultado                         *")
            print("*3 - Reporte                           *") 
            print("*7 - Regresar al menú anterior         *")            
            print("****************************************")        
            print(">> ", end="")
            a = input() 
            if a == "1":
                os.system("cls")
                print("Ingrese la cadena a evaluar:")
                print(">> ", end="")
                cadena = input() 
                print("Cadena ingresada.")
                input()
            elif a == "2":
                os.system("cls")
                e = EvaluarT2(gramatica,cadena)
                print (e.evaluar())
                input()
            elif a == "3":
                os.system("cls")
                j = Image.open("./arbol.gv.png")
                j.show()
                file = "start C:/Users/Jo/Documents/eclipse/Proyecto1_Lenguajes/Proyecto/tabla.csv"
                os.system(file)
                print("Enter para continuar.")
                input()
            elif a == "7":
                break
            else:
                print("Opción no disponibles")
                input()                
        
            
    def getGT2(self,nombre):
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que retorna una gramática tipo 2 buscada.
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
        • nombre: El nombre de la gramática a buscar.          
        __________________________________________________________________________________
        '''
        for i in self.gramaticaE:
            if nombre == i.getNombre():
                return i
        return False
        
        
        