import MySQLdb
import os
import sys
from PyQt4 import QtGui
class MyDataOperation:
    def __init__(self):
        pass
    def Add(self):
        self.beforeAdd()
        self.addData()
        self.afterAdd()
    def update(self):
        self.beforeUpdate()
        self.updateData()
        self.afterUpdate()
    def delete(self):
        self.beforeDelete()
        self.deleteData()
        self.afterDelete()
    def select(self):
        self.beforeSelect()
        self.SelectData()
        self.afterSelect()
    def create(self):
        pass
    def beforeAdd(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:beforeAdd")
        pass
    def addData(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:addData")
        pass
    def afterAdd(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:afterAdd")
        pass
    def beforeUpdate(self):
        pass
    def updateData(self):
        pass
    def afterUpdate(self):
        pass
    def beforeDelete(self):
        pass
    def deleteData(self):
        pass
    def afterDelete(self):
        pass
    def beforeSelect(self):
        pass
    def SelectData(self):
        pass
    def afterSelect(self):
        pass
    def help(self):
        os.startfile(sys.path[0]+"\\Database\\images\\help.doc")