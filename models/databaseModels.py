from MyDataModel import *


class Database(MyDataModel):
     def __init__(self,_successor):
         self.node = None
         self.curstom_table = None
         self._successor = _successor
         self.attr = None
     def initialise(self):
        self.attr = self.node.attr
        self._successor.initialise(self.tables)
        global conn
        try:
            conn = MySQLdb.connect(host=self.attr['server'],user=self.attr['username'],passwd=self.attr['password'],db=self.attr['name'],charset='utf8')
            MySQLOperation.set_ConnValue(conn)
        except Exception,e:
            conn = MySQLdb.connect(host=self.attr['server'],user=self.attr['username'],passwd=self.attr['password'],charset='utf8')
            MySQLOperation.set_ConnValue(conn)
        self.save()
        pass 
     def save(self):
        MySQLOperation.initDatabase(self)
        self._successor.save()
        MySQLOperation.createFuzzyQuerryProc()
        MySQLOperation.createprocedure()
        MySQLOperation.createAttrQueryProc()
        ###create one admin user here
        #MySQLOperation.CreateAdminUser('admin','red')
