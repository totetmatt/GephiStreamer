#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['GephiREST','GephiWS','Streamer']

import json
from enum import Enum

import requests

from .graph import Node, Edge
class Action(Enum):
    ADD_NODE = "an"
    CHANGE_NODE = "cn"
    DELETE_NODE = "dn"
    
    ADD_EDGE = "ae"
    CHANGE_EDGE = "ce"
    DELETE_EDGE = "de"  
class Streamer:
    
   
    def __init__(self,streamer,auto_commit=False):
        self.stream_method  = streamer

        
        self.add_node       = StackManager(Node,Action.ADD_NODE,streamer,auto_commit)
        self.change_node    = StackManager(Node,Action.CHANGE_NODE,streamer,auto_commit)
        self.delete_node    = StackManager(Node,Action.DELETE_NODE,streamer,auto_commit)
    
        self.add_edge       = StackManager(Edge,Action.ADD_EDGE,streamer,auto_commit)
        self.change_edge    = StackManager(Edge,Action.CHANGE_EDGE,streamer,auto_commit)
        self.delete_edge    = StackManager(Edge,Action.DELETE_EDGE,streamer,auto_commit)

        self.COMMIT_FLOW    = [ self.add_node,
                                self.add_edge,
                                self.change_edge,
                                self.change_node,
                                self.delete_edge,
                                self.delete_node
                              ]

    def commit(self):
        for action in self.COMMIT_FLOW:
            action.commit(self.stream_method.send)
            # self.stream_method.send(action.action())
            # action.reset()

class StreamError(Exception):
    pass
    
class StackManager:
        def __init__(self,entity_type,action,stream_method,auto_commit=False):
            self.type          = entity_type
            self.stack         = list()
            self.header        = action
            self.stream_method = stream_method
            self.auto_commit   = auto_commit

        def __call__(self, *args):
            for entity in args:
                if type(entity) == self.type:
                    self.stack.append(entity)
                else:
                    raise StreamError("Should pass a {type}".format(type=self.type))
                if self.auto_commit:
                    self.commit()
        def reset(self):
            del self.stack[:]

        def action(self):
            action_json  = {}
            for action in self.stack:
                action_json.update(action.json())
            return {self.header.value:action_json}
        def commit(self,auto_reset=True):
            self.stream_method.send(self.action())
            if auto_reset:
                self.reset()
        def json(self):
            return json.dumps({self.header:dict(self.stack)})

class GephiREST:
    def __init__(self, hostname="localhost", port=8080, workspace="workspace0"):
        self.hostname  = hostname
        self.port      = port
        self.workspace = workspace

    def _generate_url(self):
        return "http://{hostname}:{port}/{workspace}?operation=updateGraph".format(hostname=self.hostname,
                                                                                   port=self.port,
                                                                                   workspace=self.workspace)
    def send(self,action):
        url = self._generate_url()
        requests.post(url, data=json.dumps(action))


class GephiWS:
    def __init__(self, hostname="localhost", port=8080, workspace="workspace0"):
        from websocket import create_connection

        self.hostname  = hostname
        self.port      = port
        self.workspace = workspace
        self.websocket = create_connection(self._generate_url())

    def _generate_url(self):
        return "ws://{hostname}:{port}/{workspace}?operation=updateGraph".format(hostname=self.hostname,
                                                                                   port=self.port,
                                                                                   workspace=self.workspace)
    def send(self,action):
        self.websocket.send(json.dumps(action))    
        self.websocket.recv()