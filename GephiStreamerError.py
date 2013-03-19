'''
Created on 18 mars 2013

@author: Totetmatt
'''

class GephiStreamerError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        