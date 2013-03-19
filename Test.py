'''
Created on 18 mars 2013

@author: Totetmatt
'''
from Node import Node
from Edge import Edge
from GephiStreamerManager import GephiStreamerManager
if __name__ == '__main__':
    a = Node("A", red=1)
    a.property['category']= '1'
    b = Node("B",blue=1)
    b.property['category']= '2'
    e = Edge('A',b,True)
    t = GephiStreamerManager()
    t.add_node(a)
    t.add_node(b)
    t.add_edge(e)
    t.commit()
