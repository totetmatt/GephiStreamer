'''
Created on 18 mars 2013

@author: Totetmatt
'''

class GraphEntity(object):
    '''
    classdocs
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
        Change Color : Ask un Hexa (more 'natural')
        '''
        if r : self.params['r']    =   float(r)/255
        if g : self.params['g']    =   float(g)/255
        if b : self.params['b']    =   float(b)/255
    
