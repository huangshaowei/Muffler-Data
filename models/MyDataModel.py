from ..lib import myxmlparser
from ..mysql import MySQLOperation
from ..tools import *
import MySQLdb
from PyQt4 import QtGui,QtCore
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
        self.curstom_field_len=len(self.curstom_field)
        self.attr = tuple(["`"+item.text + '` '+item.attr['type']+"," for item in self.node.getChildren("field")])
        pass 
    def save(self):
        MySQLOperation.save(self)
        if self._successor:
            self._successor.save()
        pass
    def addNewRecord(self,attrData):
        try:
            sqlword="insert into "+ self.__name__+" value(id,"
            for i in range(0,len(attrData)):
                sqlword += get_str(attrData[i])
                if i < len(attrData)-1:
                    sqlword +=','
                else:
                    sqlword +=')'
        except Exception,e:
            QtGui.QMessageBox.about(None,"about sqlword",str(e))
        MySQLOperation.mysql_exec(sqlword)
    def deleteRecored(self,index):
        try:
            sqlword="delete * from "+self.__name__+" where id=%d"%(index)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about sqlword",str(e))
        MySQLOperation.mysql_exec(sqlword)
    def getAllRecored(self):
        sqlword="select * from "+self.__name__
        return MySQLOperation.mysql_exec_res_all(sqlword)
    def updateOneReCord(self,index,attrData):
        try:
            sqlword="update "+ self.__name__+" set "
            for i in range(0,len(attrData)):
                sqlword += "`%s`=%s"%(self.curstom_field[i],get_str(attrData[i]))
                if i < len(attrData)-1:
                    sqlword +=','
                else:
                    sqlword +=' where id=%d'%(index)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about sqlword",str(e))
        print sqlword
        MySQLOperation.mysql_exec(sqlword)