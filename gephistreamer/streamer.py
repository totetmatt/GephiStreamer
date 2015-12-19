#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['GephiREST','Streamer']

import json

import requests

from .graph import Node, Edge

class Streamer:
    ADD_NODE = "an"
    CHANGE_NODE = "cn"
    DELETE_NODE = "dn"
    
    ADD_EDGE = "ae"
    CHANGE_EDGE = "ce"
    DELETE_EDGE = "de"  
   
    def __init__(self,streamer):
        self.stream_method  = streamer

        self.add_node       = StackManager(Node,self.ADD_NODE)
        self.change_node    = StackManager(Node,self.CHANGE_NODE)
        self.delete_node    = StackManager(Node,self.DELETE_NODE)
    
        self.add_edge       = StackManager(Edge,self.ADD_EDGE)
        self.change_edge    = StackManager(Edge,self.CHANGE_EDGE)
        self.delete_edge    = StackManager(Edge,self.DELETE_EDGE)

        self.COMMIT_FLOW    = [ self.add_node,
                                self.add_edge,
                                self.change_edge,
                                self.change_node,
                                self.delete_edge,
                                self.delete_node
                              ]

    def commit(self):
        for action in self.COMMIT_FLOW:
            self.stream_method.send(action.action())
            action.reset()

class StreamError(Exception):
    pass
    
class StackManager:
        def __init__(self,entity_type,action):
            self.type = entity_type
            self.stack = list()
            self.header = action

        def __call__(self, *args):
            for entity in args:
                if type(entity) == self.type:
                    self.stack.append(entity)
                else:
                    raise StreamError("Should pass a {type}".format(type=self.type))

        def send(self,send_method):
            if self.stack:
                send_method(self.header,dict(self.stack))
                del self.stack[:]

        def reset(self):
            del self.stack[:]

        def action(self):
            action_json  = {}
            for action in self.stack:
                action_json.update(action.json())
            return {self.header:action_json}

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
