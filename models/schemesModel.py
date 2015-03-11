from MyDataModel import *


class Schemes(MyDataModel):
    def __init__(self,_successor=None):
        self._successor = _successor
        self.__name__="schemes"