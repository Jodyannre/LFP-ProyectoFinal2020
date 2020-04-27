#!/usr/bin/python
# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from metodos.Lenguaje import Lenguaje







class Pdf(object):
    '''
    __________________________________________________________________________________
    ► Descripción:
    
    → Clase destinada al manejo de los archivos pdf.
    __________________________________________________________________________________
    '''


    def __init__(self,lenguaje):
        '''
        __________________________________________________________________________________
        ► Parámetros:
        
        • lenguaje = El lenguaje de donde se tomarán los datos para crear el pdf.
        __________________________________________________________________________________
        ► Variables:
        
        • self.lenguaje = Toma los datos del lenguaje entrante.
        __________________________________________________________________________________
        '''
        self.lenguaje = lenguaje
      
    def crear_reporte(self):
        '''
        Método que se encarga de escribir y crear un archivo pdf con toda la información contenida dentro del objeto lenguaje recibido.
        
        '''
        '''
        __________________________________________________________________________________      
        ► Descripción: 
        
        → Método que se encarga de escribir y crear un archivo pdf con toda la información 
            contenida dentro del objeto lenguaje recibido.                 
        __________________________________________________________________________________    
        ► Parámetros:                                                                      
                                                                                          
            (Sin parámetros)           
        __________________________________________________________________________________
        '''
        temporal = ""
        w,h = A4
        c = canvas.Canvas(self.lenguaje.get_nombre()+".pdf",A4)
        
        #----------------------------------AFD------------------------------------
        texto = c.beginText(50, h-50)
        c.setFont('Helvetica-Oblique',16)
        texto.textLine("AFD")
        texto.textLine("-----------------------------------------")
        texto.textLine("Estado inicial")
        texto.textLine("-----------------------------------------")
        c.setFont("Times-BoldItalic", 12)
        texto.textLines(self.lenguaje.get_afd().get_estadoI())
        texto.textLine("")
        c.setFont('Helvetica-Oblique',16)
        texto.textLine("-----------------------------------------")
        texto.textLine("Estados")
        texto.textLine("-----------------------------------------")
        c.setFont("Times-BoldItalic", 12)
        for i in self.lenguaje.get_afd().get_estados():
            if temporal != "":
                temporal = temporal+","+i
            else:
                temporal = i
        texto.textLines(temporal)
        temporal = ""
        texto.textLine("")
        c.setFont('Helvetica-Oblique',16)
        texto.textLine("-----------------------------------------")
        texto.textLine("Estados de aceptación")
        texto.textLine("-----------------------------------------")
        c.setFont("Times-BoldItalic", 12)
        for i in self.lenguaje.get_afd().get_estadoA():
            if temporal != "":
                temporal = temporal+","+i
            else:
                temporal = i
        texto.textLines(temporal)
        temporal = ""
        texto.textLine("")
        c.setFont('Helvetica-Oblique',16)
        texto.textLine("-----------------------------------------")
        texto.textLine("Alfabeto")
        texto.textLine("-----------------------------------------")
        c.setFont("Times-BoldItalic", 12)
        for i in self.lenguaje.get_afd().get_simbolos():
            if temporal != "":
                temporal = temporal+","+i
            else:
                temporal = i
        texto.textLines(temporal)
        temporal = ""
        texto.textLine("")
        c.setFont('Helvetica-Oblique',16)
        texto.textLine("-----------------------------------------")
        texto.textLine("Transiciones")
        texto.textLine("-----------------------------------------")
        c.setFont("Times-BoldItalic", 12)
        texto.textLines(self.lenguaje.get_afd().get_transiciones())
        texto.textLine("-----------------------------------------")
        c.drawText(texto)
        
        texto = c.beginText(300, h-50)
        c.setFont("Times-BoldItalic", 12)
        texto.textLine("Gramática")
        texto.textLine("-----------------------------------------")
        texto.textLine("No terminales")
        texto.textLine("-----------------------------------------")
        for i in self.lenguaje.get_gramatica().get_no_terminales():
            if temporal != "":
                temporal = temporal+","+i
            else:
                temporal = i
        texto.textLines(temporal)
        temporal = ""
        texto.textLine("")
        texto.textLine("-----------------------------------------")
        texto.textLine("Terminales")
        texto.textLine("-----------------------------------------")
        for i in self.lenguaje.get_gramatica().get_terminales():
            if temporal != "":
                temporal = temporal+","+i
            else:
                temporal = i
        texto.textLines(temporal)
        temporal = ""
        texto.textLine("")
        texto.textLine("-----------------------------------------")
        texto.textLine("NT Inicial")
        texto.textLine("-----------------------------------------")
        texto.textLine(self.lenguaje.get_gramatica().get_ntInicial())
        texto.textLine("")        
        if self.lenguaje.get_gramatica().get_izquierda():
            texto.textLine("-----------------------------------------")
            texto.textLine("Producciones con recursividad por izquierda")
            texto.textLine("-----------------------------------------")
            texto.textLines(self.lenguaje.get_gramatica().get_producciones())
            temporal = ""
            texto.textLine("")
            texto.textLine("-----------------------------------------")
            texto.textLine("Producciones sin recursividad")
            texto.textLine("-----------------------------------------")
            texto.textLines(self.lenguaje.get_gramatica().get_pReporte())
            temporal = ""
            texto.textLine("")
            texto.textLine("-----------------------------------------")
        else:
            texto.textLine("-----------------------------------------")
            texto.textLine("Producciones")
            texto.textLine("-----------------------------------------")
            texto.textLines(self.lenguaje.get_gramatica().get_guardar())
            temporal = ""
            texto.textLine("-----------------------------------------")
            texto.textLine("")
        c.drawText(texto)
        c.showPage()
        texto = c.beginText(180, h-50)
        c.setFont('Helvetica-Oblique',24)
        texto.textLine("Grafo del autómata:")
        c.drawText(texto)
        c.drawImage('Grafo_Automata.gv.png', 25, 480, 480, 270)
        c.showPage()
        texto = c.beginText(50, h-50)    
        c.setFont("Times-BoldItalic", 12)    
        texto.textLine("-----------------------------------------")
        texto.textLine("Cadenas válidas")
        texto.textLine("-----------------------------------------")
        contador = 0
        for i in self.lenguaje.get_cadenaV():
            contador = contador+1
            t = str(contador)+". "+i
            texto.textLine(t)
        temporal = ""
        texto.textLine("")
        c.drawText(texto)
        texto = c.beginText(300, h-50)    
        c.setFont("Times-BoldItalic", 12)    
        texto.textLine("-----------------------------------------")
        texto.textLine("Cadenas inválidas")
        texto.textLine("-----------------------------------------")
        contador = 0
        for i in self.lenguaje.get_cadenaI():
            contador = contador+1
            t = str(contador)+". "+i
            texto.textLine(t)
        temporal = ""
        texto.textLine("")
        c.drawText(texto)
        c.showPage()
        texto = c.beginText(50, h-50)    
        c.setFont("Times-BoldItalic", 12) 
        texto.textLine("-----------------------------------------")
        texto.textLine("Cadenas evaluadas")
        texto.textLine("-----------------------------------------")
        contador = 0
        for i in self.lenguaje.get_cadenaI():
            contador = contador+1
            t = str(contador)+". "+i+"--Inválida"
            texto.textLine(t)
        for i in self.lenguaje.get_cadenaV():
            contador = contador+1
            t = str(contador)+". "+i+"--Válida"
            texto.textLine(t)
        temporal = ""
        texto.textLine("")
        c.drawText(texto)
        c.save()
        print() 
        
        
        #-----------------------------GRAMATICA
        
      
#w,h = A4
#c = canvas.Canvas("hola_mundo.pdf",A4)
#c.setFont('Times-Bold',80)#
#c.drawString(50, h - 50, "Hola mundo")
#c.ShowPage()     #Pasar a la siguiente hoja
#texto = c.beginText(50, h-50)
#texto.textLines("Hola señores cómo les va?\nYo muy bien.\n sñdlkajsdñlkasdñlaksdjfñlskdjfñlaskj")
#c.drawText(texto)
#c.save()