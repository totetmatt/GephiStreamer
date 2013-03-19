'''
Created on 18 mars 2013

@author: Totetmatt
'''
from GraphEntity import GraphEntity
class Node(GraphEntity):
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

if __name__ == '__main__': 
    n=  Node('testId',size=10)
    print n
    
    n.params['hello']='world'
    print n