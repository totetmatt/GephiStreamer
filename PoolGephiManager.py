'''
Created on 19 mars 2013

@author: Totetmatt
'''
from GephiStreamerError  import GephiStreamerError 
from GephiStreamerManager import GephiStreamerManager
class PoolGephiManager(object):
    '''
    classdocs
    '''

    MANAGERS_STACK = []
    ID = 0
    def __init__(self):
        '''
        Constructor
       '''
    def add(self,iGephiManager):
        if type(iGephiManager) != GephiStreamerManager:
            raise GephiStreamerError('Adding a non-GephiStreamerManager type')
        self.MANAGERS_STACK.append(iGephiManager)
        self.ID +=1
    def remove(self,index):
        del self.MANAGERS_STACK[index]
    def commit(self):
        for manager in self.MANAGERS_STACK : manager.commit()   
    def send(self,aAction,aEntity):
        for manager in self.MANAGERS_STACK : manager.send(aAction,aEntity) 
        
    def add_node (self,entity):
        for manager in self.MANAGERS_STACK : manager.add_node(entity)
    def change_node(self,entity):
        for manager in self.MANAGERS_STACK : manager.change_node(entity)
    def delete_node (self,entity):
        for manager in self.MANAGERS_STACK : manager.delete_node(entity)
    
    def add_edge(self,entity):
        for manager in self.MANAGERS_STACK : manager.add_edge(entity)
    def change_edge(self,entity):
        for manager in self.MANAGERS_STACK : manager.change_edge(entity)
    def delete_edge (self,entity):
        for manager in self.MANAGERS_STACK : manager.delete_edge(entity)