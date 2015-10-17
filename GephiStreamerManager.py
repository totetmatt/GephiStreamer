'''
Created on 18 mars 2013

@author: Totetmatt
'''
import json
import urllib
from GephiStreamerError import GephiStreamerError
from Node import Node
from Edge import Edge
import requests
from GraphEntity import GraphEntity
class StackManager(object):

        def __init__(self,iType,iHeaderAction):
            self.type = iType
            self.stack = list()
            self.header = iHeaderAction
        def __call__(self, iGraphEntity):
            if type(iGraphEntity) == self.type:
                self.stack.append(next(iter(iGraphEntity.object.items())))
            else:
                raise GephiStreamerError("Should pass a %s"%self.type)
        def send(self,iSendMethod):
            if self.stack:
                iSendMethod(self.header,dict(self.stack))

                del self.stack[:]
        def reset(self):
            del self.stack[:]
        def action(self):
            return {self.header:dict(self.stack)}
class GephiStreamerManager(object):
    
    '''
    Stream Manager for One Gephi instance (host + workspace)
    '''
    ADD_NODE = "an"
    CHANGE_NODE = "cn"
    DELETE_NODE = "dn"
    
    ADD_EDGE = "ae"
    CHANGE_EDGE = "ce"
    DELETE_EDGE = "de"
    
    add_node = StackManager(Node,ADD_NODE)
    change_node = StackManager(Node,CHANGE_NODE)
    delete_node = StackManager(Node,DELETE_NODE)
    
    add_edge = StackManager(Edge,ADD_EDGE)
    change_edge = StackManager(Edge,CHANGE_EDGE)
    delete_edge = StackManager(Edge,DELETE_EDGE)
    
    def name(self):
        return "http://%s/%s?operation=updateGraph"%(self.GEPHI_STREAM_URL,self.GEPHI_STREAM_WORKSPACE)
    def ___str__(self):
        return self.name()
    def __unicode__(self):
        return self.name()
    def __init__(self,iGephiUrl='localhost:8080',iGephiWorkspace='workspace0'):
        '''
        Constructor
        '''
        self.GEPHI_STREAM_URL=iGephiUrl
        self.GEPHI_STREAM_WORKSPACE=iGephiWorkspace
        self.proxies = {}
        self.commit_flow = [self.add_node,self.add_edge,self.change_edge,self.change_node,self.delete_edge,self.delete_node]
    def commit(self):
        metaAction = {}
        for s in self.commit_flow:
            metaAction.update(s.action())
            s.reset() 
        self.send(metaAction)    
            
    def send(self,action):
        params = json.dumps(action)
        aSendURL = self.name()
        
        if "127.0.0.1" in self.GEPHI_STREAM_URL or 'localhost' in self.GEPHI_STREAM_URL:
            r= requests.post(aSendURL, data=params)
        else:
            r= requests.post(aSendURL, data=params)
    def sendEntityAction(self,action,iGraphEntity):
        if type(iGraphEntity) == Node or type(iGraphEntity) == Edge:
            postAction = {action:iGraphEntity.object}
        else:
            postAction = {action:iGraphEntity}
        
        self.send(postAction)
            
if __name__ == '__main__':     
    a = Node("A", red=1)        # Create a node
    a.property['category']= '1'     # add a property 
    b = Node("B",blue=1)        # Create a node
    b.property['category']= '2' # add a property 
    e = Edge('A',b,True)        # Create edge, can use Node type or Id of node for Source and Destination
    t = GephiStreamerManager()  # Streamer Manager (default http://localhost:8080/workspace0)
    t.add_node(a)               
    t.add_node(b)
    t.add_edge(e)
    t.commit()     