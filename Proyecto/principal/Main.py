#!/usr/bin/python
# -*- coding: utf-8 -*-

from menus.Menu import Menu
import os
import time

if __name__ == '__main__':
    pass

def main():
    entrada = 0
    menu = Menu()
    menu.caratula()
    
    while (entrada != 7):
        os.system("cls")
        entrada = int(menu.menu_Inicio())
        if entrada==1:
            time.sleep(0.6)
            menu.menu_AFD()
        elif entrada==2:
            time.sleep(0.6)
            menu.menu_Gramatica()
        elif entrada==3:
            time.sleep(0.6)
            menu.menu_Evaluar_Cadena()
        elif entrada==4:
            time.sleep(0.6)
            menu.menu_Cargar_Archivo()
        elif entrada==5:
            time.sleep(0.6)
            menu.menu_Guardar()
        elif entrada==6:
            time.sleep(0.6)
            menu.menu_Reporte()    
        elif entrada==8:
            menu.gramaticaTipo2()
            
main()