'''
Created on 13/03/2020

@author: Jo
'''

class nt(object):
    '''
    classdocs
    '''


    def __init__(self, nombre):
        '''
        Constructor
        '''
        self.producciones = []
        self.original = []
        self.nombre = nombre
        self.log = ""
        
    def agregar_produccion(self,prod):
        self.producciones.append(prod)
        self.original.append(prod)
        
    def get_nombre(self):
        return self.nombre
    
    def get_producciones(self):
        return self.producciones
    
    def set_log(self,log):
        set.log = log
        