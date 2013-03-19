'''
Created on 18 mars 2013

@author: Totetmatt
'''
from GraphEntity import GraphEntity
from Node import Node
class Edge(GraphEntity):
    '''
    Node object
    kwargs [label, size, x, y, z, red, green, blue]
    '''
    KWARGS=[]
    
    def __init__(self, source, target, directed,eid=None, weight=1, label="", red=0.5, green=0.5, blue=0.5):
        '''
        Constructor
        '''
        if type(source)==Node:
            source=source.object.keys()[0]
        if type(target)==Node:   
            target=target.object.keys()[0]
            
        if not eid:
            if directed:
                eid="%s-->%s"%(source,target)
            else:
                eid="%s--%s%"(source,target)
        
        GraphEntity.__init__(self, eid,   {"source":source,"target":target,"weight":weight,"directed":directed,"label":label,"r":red,"g":green,"b":blue})    

   
if __name__ == '__main__': 
    pass