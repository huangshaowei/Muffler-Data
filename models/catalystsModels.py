from MyDataModel import *


class Catalysts(MyDataModel):
    def __init__(self,_successor=None):
        self._successor = _successor
        self.__name__="catalysts"