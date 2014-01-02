GephiStreamer
=============

Python classes for streaming graph to gephi
Install
======

Download and unzip in your python project in %base%/GephiStreamer/

/!\ Requests module  is needed  (http://docs.python-requests.org/en/latest/#) /!\

Quick use
======

```python
from GephiStreamer import Node,Edge,GephiStreamerManager

a = Node("A", red=1) 		# Create a node
a.property['category']= '1'  	# add a property 
b = Node("B",blue=1)		# Create a node
b.property['category']= '2'	# add a property 
e = Edge('A',b,True)		# Create edge, can use Node type or Id of node for Source and Destination
t = GephiStreamerManager()  # Streamer Manager (default http://localhost:8080/workspace0)
t.add_node(a)				
t.add_node(b)
t.add_edge(e)
t.commit()					# Send everything > Group streaming by action (e.g if you have 1000 nodes to add, it will send only one message to gephi)
""" Or Alternative
t.send(GephiStreamerManager.ADD_NODE,a)					# send a to gephi
t.send(GephiStreamerManager.ADD_NODE,b)					# send b to gephi
t.send(GephiStreamerManager.ADD_EDGE,e)					# send e to gephi

"""
```
Direct Send Mode 
=====
Direct Send Mode use the GephiStreamerManager.send method to send one action immediatly.
```python
from GephiStreamer import Node,Edge,GephiStreamerManager
t = GephiStreamerManager()  # Streamer Manager (default http://localhost:8080/workspace0)

a = Node("A", red=1)   
t.send(GephiStreamerManager.ADD_NODE,a)  				
b = Node("B",blue=1)		
e = Edge('A',b,True)		


t.send(GephiStreamerManager.ADD_NODE,b)    			# send b to gephi
t.send(GephiStreamerManager.ADD_EDGE,e)    			# send e to gephi

```
This mode is usefull for quick implementation.


Transaction Mode
=====
The transaction mode store all the action to perform and will send only at commit GephiStreamerManager.call
```python
from GephiStreamer import Node,Edge,GephiStreamerManager
t = GephiStreamerManager()  # Streamer Manager (default http://localhost:8080/workspace0)

a = Node("A", red=1)   	# Create a node
b = Node("B",blue=1)		# Create a node
e = Edge('A',b,True)	

t.add_node(a)				
t.add_node(b)
t.add_edge(e)
t.commit()				

```
The advantage to use this mode is that it will pack all same actions into one gephi call, whereas the Driect Send Mode do one call per entity.
It's should be faster for creating large set of entities in "one shot"

Example: I want to create 1 node that have a edge to 10 000 other nodes

* Direct Send Mode : will operate 20 001 calls (10 001 calls for nodes, 10 000 for edges)
* Transaction Mode : will operate 2 calls (1 for add 10 001 nodes, 1 for add 10 000 edges)

Gephi Instance
=====
Default Gephi instance targeted is localhost on port 8080
```python
t = GephiStreamerManager()
```

To stream a remote Gephi instance use the argument iGephiUrl
```python
t = GephiStreamerManager(iGephiUrl='ip_or_machine_name:myport')
```

To stream to a different workspace, usr the argument iGephiWorkspace
```python
t = GephiStreamerManager(iGephiWorkspace='workspace1')
```
