'''
Created on 18 mars 2013

@author: Totetmatt
'''
from Node import Node
from Edge import Edge
from GephiStreamerManager import GephiStreamerManager
if __name__ == '__main__':
    t = GephiStreamerManager()
    a = Node("A", red=1)
    a.property['category']= '1'
    t.add_node(a)
    for i in range(1,10000):
        b = Node("B%s"%i,blue=1)
        b.property['category']= '2'
        e = Edge('A',b,True)
        
        t.add_node(b)
        t.add_edge(e)
    t.commit()
