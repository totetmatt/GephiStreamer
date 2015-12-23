# Basic import
from gephistreamer import graph
from gephistreamer import streamer

import itertools
import random
import time

# Same code as GephiREST, but it creates a Websocket client that keep connectivity until the script exits
# Much faster than REST method
stream = streamer.Streamer(streamer.GephiWS())
test =  [x for x in itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 2) ]
random.shuffle(test)
for source, target in test:
    
    node_source = graph.Node(source)
    node_target = graph.Node(target)

    stream.add_node(node_source,node_target)
    # time.sleep(0.5) # Make it slower :D
    stream.add_edge(graph.Edge(node_source,node_target))

time.sleep(1) #It might be possible the script runs too fast and last action anr't sent properly


