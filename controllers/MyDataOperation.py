import MySQLdb
import os
import sys
from PyQt4 import QtGui

CheckAuthority = None

class MyDataOperation:
    def __init__(self):
        pass
    def Add(self):
        try:
            if not self.CheckCurrentUser():
                return 
            self.beforeAdd()
            self.addData()
            self.afterAdd()
        except Exception,e:
            QtGui.QMessageBox.about(None,"about",str(e))
    def update(self):
        if not self.CheckCurrentUser():
            return 
        self.beforeUpdate()
        self.updateData()
        self.afterUpdate()
    def delete(self):
        if not self.CheckCurrentUser():
            return 
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
        QtGui.QMessageBox.about(None,"about","MyDataOperation:addData")
        pass
    def addData(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:addData")
        pass
    def afterAdd(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:afterAdd")
        pass
    def beforeUpdate(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:addData")
        pass
    def updateData(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:updateData")
        pass
    def afterUpdate(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:afterUpdate")
        pass
    def beforeDelete(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:addData")
        pass
    def deleteData(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:deleteData")
        pass
    def afterDelete(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:afterDelete")
        pass
    def beforeSelect(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:beforeselect")
        pass
    def SelectData(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:selectData")
        pass
    def afterSelect(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:afterSelect")
        pass
    def registerAuthrityFun(self,fun):
        global CheckAuthority
        CheckAuthority = fun
    def CheckCurrentUser(self):
        global CheckAuthority
        if CheckAuthority:
            return CheckAuthority()
    def help(self):
        os.startfile(sys.path[0]+"\\Database\\images\\help.doc")