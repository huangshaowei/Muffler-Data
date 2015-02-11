
from MyDataModel import *


class CarModels(MyDataModel):
    def __init__(self,_successor=None):
        self.node = None
        self.curstom_field = None
        self._successor = _successor
        self.__name__="models"