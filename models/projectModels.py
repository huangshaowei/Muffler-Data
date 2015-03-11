from MyDataModel import *


class Projects(MyDataModel):
    def __init__(self,_successor=None):
        self._successor = _successor
        self.__name__="projects"