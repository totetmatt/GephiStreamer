class Entity(object):
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
      
    def color_hex(self,r=None,g=None,b=None):
        '''
        Change Color : Ask Hexa (more 'natural')
        '''
        if r : self.property['r']    =   float(r)/255
        if g : self.property['g']    =   float(g)/255
        if b : self.property['b']    =   float(b)/255

class Node(Entity):
    '''
    Node object
    '''
    def __init__(self,eid,label=None, size=1, x=0, y=0, z=0, red=0.5, green=0.5, blue=0.5):
        '''
        Constructor
        '''
        if not label:
            label = eid
        GraphEntity.__init__(self, eid,  {"label":label,"size":size,"x":x,"y":y,"z":z,"r":red,"g":green,"b":blue})    

class Edge(GraphEntity):
    '''
    Edge object
    kwargs [label, size, x, y, z, red, green, blue]
    '''
    def __init__(self, source, target, directed,eid=None, weight=1, label="", red=0.5, green=0.5, blue=0.5):
        '''
        Constructor
        '''
        if type(source)==Node:
            source=next(iter(source.object.keys()))
        if type(target)==Node:   
            target=next(iter(target.object.keys()))
            
        if not eid:
            eid = self._generate_id(source,target,directed)
        
        GraphEntity.__init__(self, eid,   {"source":source,"target":target,"weight":weight,"directed":directed,"label":label,"r":red,"g":green,"b":blue})    
    
    def _generate_id(self,source,target,directed):
        return "{source}--{direction}{target}".format(source=source,
                                                      target=target,
                                                      direction=directed and ">" or "-")
