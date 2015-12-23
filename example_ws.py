# Basic import
from gephistreamer import graph
from gephistreamer import streamer
import itertools
import random
import time

# Same code as GephiREST, but it creates a Websocket client that keep connectivity until the script exits
# Much faster than REST method
stream = streamer.Streamer(streamer.GephiWS())
for source, target in [x for x in itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 2) ]:
    node_source = graph.Node(source)
    node_target = graph.Node(target)


    stream.add_node(node_source,node_target)

    stream.add_edge(graph.Edge(node_source,node_target))

    stream.commit()

