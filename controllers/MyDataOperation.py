import MySQLdb
import os
import sys
from PyQt4 import QtGui


MyUserController = None

class MyDataOperation:
    def __init__(self):
        pass
    def Add(self):
        try:
            if not self.CheckCurrentUser():
                return 
            if not self.beforeAdd():
                return 
            if not self.addData():
                return 
            if not self.afterAdd():
                return 
            self.reflesh()
        except Exception,e:
            QtGui.QMessageBox.about(None,"about",str(e))
    def update(self,cons):
        if not self.CheckCurrentUser():
            return 
        if not self.beforeUpdate():
            return 
        if not self.updateData(cons):
            return 
        if not self.afterUpdate():
            return 
    def delete(self,num=None):
        if not self.CheckCurrentUser():
            return 
        if not self.beforeDelete():
            return 
        if not self.deleteData(num):
            return
        if not self.afterDelete():
            return 
        self.reflesh()
    def select(self,condition=None):#condition is dirt
        if not condition:
            condition = self.beforeSelect()
        res = self.SelectData(condition)
        if not self.afterSelect(res):
            return
        return res
    def create(self):
        pass
    def beforeAdd(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:beforeAdd")
        return True
    def addData(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:addData")
        return True
    def afterAdd(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:afterAdd")
        return True
    def beforeUpdate(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:addData")
        return True
    def updateData(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:updateData")
        return True
    def afterUpdate(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:afterUpdate")
        return True
    def beforeDelete(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:beforDelete")
        return True
    def deleteData(self ,num):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:deleteData")
        return True
    def afterDelete(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:afterDelete")
        return True
    def beforeSelect(self):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:beforeselect")
        return True
    def SelectData(self,condition):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:selectData")
        return True
    def afterSelect(self,res):
        QtGui.QMessageBox.about(None,"about","MyDataOperation:afterSelect")
        return True
    def registerUserController(self,controller):
        global MyUserController
        MyUserController = controller
    def CheckCurrentUser(self):
        global MyUserController
        if MyUserController:
            return MyUserController.check_authority()
    def getUserController(self):
        return MyUserController
    def help(self):
        os.startfile(sys.path[0]+"\\Database\\images\\help.doc")
    def fileDialogOpen(self,ui):
        FDialog = QtGui.QFileDialog()
        filename = FDialog.getOpenFileName(None,"file name","./","Allfile(*.*)")
        ui.setText(filename)
    def reflesh(self):
        pass 
    def check_empty(self,nums):
        for num in nums:
            if not self.lineEdits[self.textEdits[num-1]-1].text():
                QtGui.QMessageBox.about(None,"about sqlword",self.projectModel.curstom_field[num-1]+" is empty!")
                return False
        return True
    def check_integer(self,nums):
        for num in nums:
            if not self.lineEdits[self.textEdits[num-1]-1].text().toInt()[1]:
                QtGui.QMessageBox.about(None,"about sqlword",self.projectModel.curstom_field[num-1]+" has to write integer!")
                return False 
        return True 