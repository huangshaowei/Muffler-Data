from MyDataModel import *


class Mufflers(MyDataModel):
    def __init__(self,_successor=None):
        self._successor = _successor
        self.__name__="mufflers"