import MyDataModel
import MyParser
import MyElementParser


class Project(MyDataModel):
    def __init__(self,_successor):
        self.node = None
        self.curstom_field = None
        self._successor = _successor;
    def __init__(self):
        self.node = None
        self.curstom_field = None
        self._successor = None
        pass
    def initialise(self,data=None):
        if data:
            data = self.tables
        self.node = data[__name__]
        self.curstom_field = data.getChildren("table")
        data.remove
        if self._successor:
            self._successor(data)
        pass 
        