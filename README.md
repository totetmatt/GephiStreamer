GephiStreamer
=============

Python classes for streaming graph to gephi

Quick use
======

```python
from Node import Node
from Edge import Edge
from GephiStreamerManager import GephiStreamerManager

a = Node("A", red=1) 		# Create a node
a.params['category']= '1'  	# add a property 
b = Node("B",blue=1)		# Create a node
b.params['category']= '2'	# add a property 
e = Edge('A',b,True)		# Create edge, can use Node type or Id of node for Source and Destination
t = GephiStreamerManager()  # Streamer Manager (default http://localhost:8080/workspace0)
t.add_node(a)				
t.add_node(b)
t.add_edge(e)
t.commit()					# Send everything > Group streaming by action (e.g if you have 1000 node to ad, it will send only one message to gephi)
""" Or Alternative
t.send(a)					# send a to gephi
t.send(b)					# send b to gephi
t.send(e)					# send e to gephi

"""
```