import json

import requests

class Streamer:
    ADD_NODE = "an"
    CHANGE_NODE = "cn"
    DELETE_NODE = "dn"
    
    ADD_EDGE = "ae"
    CHANGE_EDGE = "ce"
    DELETE_EDGE = "de"  
   
    def __init__(self,streamer):
        self.stream_method = streamer

        self.add_node = StackManager(Node,ADD_NODE)
        self.change_node = StackManager(Node,CHANGE_NODE)
        self.delete_node = StackManager(Node,DELETE_NODE)
    
        self.add_edge = StackManager(Edge,ADD_EDGE)
        self.change_edge = StackManager(Edge,CHANGE_EDGE)
        self.delete_edge = StackManager(Edge,DELETE_EDGE)

        self.COMMIT_FLOW = [self.add_node,self.add_edge,self.change_edge,self.change_node,self.delete_edge,self.delete_node]

    def commit(self):
        for action in self.COMMIT_FLOW:
            self.streamer.json(action.action())
            action.reset()


class StackManager:
        def __init__(self,entity_type,action):
            self.type = entity_type
            self.stack = list()
            self.header = action
        def __call__(self, entity_type):
            if type(entity_type) == self.type:
                self.stack.append(next(iter(iGraphEntity.object.items())))
            else:
                raise GephiStreamerError("Should pass a {type}".format(type=self.type))
        def send(self,iSendMethod):
            if self.stack:
                iSendMethod(self.header,dict(self.stack))
                del self.stack[:]
        def reset(self):
            del self.stack[:]
        def action(self):
            return {self.header:dict(self.stack)}
        def json(self):
            return json.dumps({self.header:dict(self.stack)})

class GephiREST:
    def __init__(self,hostname="localhost",port=8080,workspace="workspace0"):
        self.hostname  = hostname
        self.port      = port
        self.workspace = workspace

    def _generate_url(self):
        return "http://{hostname}:{port}/{workspace}?operation=updateGraph".format(hostname=self.hostname,
                                                                                   port=self.port,
                                                                                   workpace=self.workpace)
    def send(self,action):
        requests.post()
