'''
Created on 18 mars 2013

@author: Totetmatt
'''

class GraphEntity(object):
    '''
    classdocs
    '''


    def __init__(self,eid, params):
        '''
        Constructor
        '''
        self.params = params
        self.object ={eid:self.params}
        
    def __str__(self):
        return "%s"%self.object  
      
    def colorHex(self,r=None,g=None,b=None):
        '''
        Change Color : Ask un Hexa (more 'natural')
        '''
        if r : self.params['r']    =   float(r)/255
        if g : self.params['g']    =   float(g)/255
        if b : self.params['b']    =   float(b)/255
    
