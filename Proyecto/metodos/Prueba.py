#!/usr/bin/python
# -*- coding: utf-8 -*-
from metodos.Gramatica import Gramatica
from lectores.LectorLenguaje import LectorLenguaje
import sys


if __name__ == '__main__':
    pass

class Nodo:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

def obtenerLista(opt):
    lista_hijo = []
    lista_ini = []
    if opt == 1:
        lista_hijo.append(Nodo("d",1))
        lista_ini.append(lista_hijo)
    elif opt == 2:
        lista_hijo.append(Nodo("a", 1))
        lista_hijo.append(Nodo("A'",0))
        lista_ini.append(lista_hijo)
        lista_hijo = []
        lista_hijo.append(Nodo("b",1))
        lista_hijo.append(Nodo("A'", 0))
        lista_ini.append(lista_hijo)
        lista_hijo = []
        lista_hijo.append("-")
        lista_ini.append(lista_hijo)
    return lista_ini


def evaluar(lista_ini, cadena):
    lista_aux = []
    j = 0 #column
    i = 0 #character
    k = 0 #row
    cont = 0
    opt = 1
    while cont <= len(lista_ini):
        if lista_ini[j][k].tipo == 0: #si es NT
            #if opt != 3:
            lista = obtenerLista()
            lista_aux.append(lista_ini) 
            lista_aux.append(k) #guarda la posiciï¿½n en que se quedï¿½
            lista_ini = lista
            k = 0
            #if opt == 3:
            #    opt = 2
            #else:
            #    opt += 1
            continue
        if lista_ini[j][k].tipo == 1: #si es T
            if i < len(cadena) and cadena[i] == lista_ini[j][k].valor:
                #lista_ini = lista_aux
                i += 1
                if len(lista_ini[j]) > 1: #si vienen mï¿½s posiciones en el actual /filas/
                    k += 1
                    cont = 0
                else:
                    #verifica si tiene elementos la pila auxiliar
                    if len(lista_aux) > 0:
                        k = lista_aux.pop()
                        lista_ini = lista_aux.pop() #se obtiene lo que tenga la pila
                        k +=1 #se suma la siguiente posiciï¿½n en la columna
                        cont = 0
                cont += 1
                continue
            else:
                #verificar primero si la cadena ya se terminï¿½ de leer 
                if i < len(cadena):
                    #si la cadena ya terminï¿½ sin error entonces empezar a buscar epsilï¿½n.
                    k_tmp = lista_aux.pop()
                    lista_tmp = lista_aux.pop()
                    tam_tmp = len(lista_tmp)-1
                    while tam_tmp != 1 and k_tmp <= tam_tmp: #que no sea uno porque tiene el nodo padre.
                        if  lista_tmp[k_tmp][0] == '-': #si es epsilï¿½n entonces sacar el siguiente
                            k_tmp = lista_aux.pop()
                            lista_tmp = lista_aux.pop()
                            tam_tmp -=1
                            continue
                        k_tmp+=1
                    #verificar si el tamaï¿½o de la lista coincide con el nï¿½mero de k
                    if tam_tmp == k_tmp:
                        break; #terminï¿½ con ï¿½xito
                    else:
                        break; #error
                elif len(lista_ini[j]) > 1: #si vienen mï¿½s posiciones en el actual /filas/
                    k += 1 #porque sino tiene que pasar al siguiente
                    #verificar si la lista auxiliar tiene el mismo NT que el que viene.
                    if lista_aux != []: #si la lista no estï¿½ vacï¿½a
                        k_tmp = lista_aux.pop() #saca el ultimo k ingresado.
                        lista_tmp = lista_aux.pop() #saca la ï¿½ltima lista agregada.
                        if lista_tmp[j][k_tmp].valor == lista_ini[j][k].valor: #es porque ya vino estï¿½ necesita pasar a la siguiente producciï¿½n del mismo nivel.
                            j += 1
                            k = 0
                            lista_ini = lista_tmp
                    continue
        else:
            k = lista_aux.pop()
            lista_ini = lista_aux.pop()
            cont = 0

def main():
    i = 0
    j = 0
    k = 0
    cadena = "dbaabb"
    lista_ini = []
    evaluar(lista_ini, cadena)


main()       