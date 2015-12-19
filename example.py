# Basic import
from gephistreamer import graph
from gephistreamer import streamer

# Create a Streamer
# adapt if needed : streamer.GephiREST(hostname="localhost", port=8080, workspace="workspace0")
stream = streamer.Streamer(streamer.GephiREST())

# Create a node with a custom_property
node_a = graph.Node("A",custom_property=1)

# Create a node and then add the custom_property
node_b = graph.Node("B")
node_b.property['custom_property']=2

# Add the node to the stream
stream.add_node(node_a,node_b)

# Create edge 
# You can also use the id of the node :  graph.Edge("A","B",custom_property="hello")
edge_ab = graph.Edge(node_a,node_b,custom_property="hello")

# Add the edge to the stream
stream.add_edge(edge_ab)

# Send the current graph (it send the data to gephi and delete it)
stream.commit()