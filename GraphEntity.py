'''
Created on 18 mars 2013

@author: Totetmatt
'''

class GraphEntity(object):
    '''
    Abstract Class for Nodes and Edges
    '''


    def __init__(self,eid, property):
        '''
        Constructor
        '''
        self.property = property
        self.object ={eid:self.property}
        
    def __str__(self):
        return "%s"%self.object  
      
    def colorHex(self,r=None,g=None,b=None):
        '''
        Change Color : Ask Hexa (more 'natural')
        '''
        if r : self.property['r']    =   float(r)/255
        if g : self.property['g']    =   float(g)/255
        if b : self.property['b']    =   float(b)/255
    
