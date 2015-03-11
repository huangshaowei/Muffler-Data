from ..lib import *
from ..mysql import MySQLOperation
from ..tools import *
import MySQLdb
import datetime
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
        self.curstom_field_with_type = {}
        for item in  self.node.getChildren("field"):
            self.curstom_field_with_type.update({item.text:item.attr['type']})
        pass 
    def save(self):
        MySQLOperation.save(self)
        if self._successor:
            self._successor.save()
        pass
    def addNewRecord(self,attrData):
        try:
            sqlword="insert into "+ self.__name__+" values(id,"
            for i in range(0,len(attrData)):
                sqlword += get_str(attrData[i])
                if i < len(attrData)-1:
                    sqlword +=','
                else:
                    sqlword +=')'
        except Exception,e:
            QtGui.QMessageBox.about(None,"about sqlword",str(e))
            return False
        QtGui.QMessageBox.about(None,"about sqlword",sqlword)
        return MySQLOperation.mysql_exec(sqlword)
    def deleteRecored(self,index):
        try:
            sqlword="delete from "+self.__name__+" where id=%d"%(index)
            QtGui.QMessageBox.about(None,"about sqlword",sqlword)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about sqlword",str(e))
            return False
        return MySQLOperation.mysql_exec(sqlword)
    def updateOneField(self,index,str_text,condition):
        try:
            sqlword = "update `%s` set `%s`='%s' where `%s` = '%s'"%(self.__name__,self.curstom_field[index],str_text,self.curstom_field[0],condition)
            QtGui.QMessageBox.about(None,"about sqlword",sqlword)
            MySQLOperation.mysql_exec(sqlword)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about sqlword",str(e))
    def getAllRecored(self):
        sqlword="select * from "+self.__name__
        return MySQLOperation.mysql_exec_res_all(sqlword)
    def getAllRecoredWithOneFiled(self):
        sqlword="call getAllRecordWithOneField('%s','%s')"%(self.curstom_field[0],self.__name__)
        return MySQLOperation.mysql_exec_res_all(sqlword)
    def getAllRecoredWithPatticularFiled(self,field):
        sqlword="call getAllRecordWithOneField('%s','%s')"%(self.curstom_field[field-1],self.__name__)
        return MySQLOperation.mysql_exec_res_all(sqlword)
    def getAllRecoredWithFuzzyQuery(self,part,field = 0):
        sqlword="call proc_fuzzyQuery('%s','%s','%s')"%(part,self.curstom_field[field-1],self.__name__)
        return MySQLOperation.mysql_exec_res_all(sqlword)
    def getAttrsWithSpecialCondition(self,condition,attrs):
        try:
            attrQuery = "".join([ "`"+item+'`,' for item in attrs])[:-1]
            sqlword="call proc_attrQuery('%s','%s','%s')"%(attrQuery,'`%s`="%s"'%(self.curstom_field[0],condition),self.__name__)
            return [ items if not type(items) == datetime.datetime else items.strftime("%Y-%m-%d %H:%M:%S") for items in MySQLOperation.mysql_exec_res_all(sqlword)[0]]
        except Exception,e:
            QtGui.QMessageBox.about(None,"about sqlword",str(e))
    def getAllRecordWithCondition(self,condition,attr):
        try:
            attrQuery = ""
            for item in attr:
                attrQuery +="`%s`,"%self.curstom_field[item-1]
            sqlword = """call proc_attrQuery("%s","%s","%s")"""%(attrQuery[:-1],condition,self.__name__)
            QtGui.QMessageBox.about(None,"about res....",sqlword)
            return MySQLOperation.mysql_exec_res_all(sqlword)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about sqlword",str(e))
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
        MySQLOperation.mysql_exec(sqlword)