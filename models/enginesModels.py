from MyDataModel import *

class Engines(MyDataModel):
    def __init__(self,_successor = None):
        self._successor = _successor
        self.__name__="engines"