from ..lib import myxmlparser
from ..mysql import MySQLOperation
import MySQLdb

class MyDataModel:
    def __init__(self):
        self.node = None
        self.tables = None
        curstom_field = []
        
    def Parser(self,data):
        if data == None:
            return
        p = myxmlparser.MyElementTree(data,"utf8")
        self.node = p.parser()
        self.tables = self.node.getChildren("table")
        pass 
    def initialise(self,data=None):
        if not data:
            data = self.tables
        for node in data:
            if node.attr["name"] == self.__name__:
                self.node = node
                break
        data.remove(node)
        if self._successor:
            self._successor.initialise(data)
        self.curstom_field = [item.text for item in self.node.getChildren("field")]
        self.attr = tuple(["`"+item.text + '` '+item.attr['type']+"," for item in self.node.getChildren("field")])
        pass 
    def save(self):
        MySQLOperation.save(self)
        if self._successor:
            self._successor.save()