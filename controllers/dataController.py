from .databaseController import *
from .userController import *


class DataController(DatabaseController):
    def __init__(self):
        self.dataModel = self.getOwnModel('data')
        self.dataView = QtGui.QDialog()
        self.setupView(self.dataView,Ui_Para_MufflerData_Add_Dlg)
    def initializeView(self):
        for t in self.lineEdits:
            if t.__class__ == QtGui.QComboBox:
                t.setCurrentIndex(0)
            else:
                t.clear()
    def addData(self):
        win = self.dataView.ui
        return self.insertToData(win)
    def insertToData(self,win):
        num = win.box6_tableWidget1.rowCount()
        for i in range(0,num):
            try:
                item1 = win.box6_tableWidget1.item(i,0)
                item2 = win.box6_tableWidget1.item(i,1)
            except Exception,e:
                QtGui.QMessageBox.about(None,"about",str(e))
                return False
            self.dataModel.addNewRecord([self.current_muffler,1000,item1.text(),item2.text()])
        num = win.box6_tableWidget2.rowCount()
        for i in range(0,num):
            try:
                item1 = win.box6_tableWidget2.item(i,0)
                item2 = win.box6_tableWidget2.item(i,1)
            except Exception,e:
                QtGui.QMessageBox.about(None,"about",str(e))
                return False
            self.dataModel.addNewRecord([self.current_muffler,3000,item1.text(),item2.text()])
        return True
    def showData(self,freq):
        try:
            attr = [3,4]
            condition = "`%s`='%s' and `%s`='%s'"%(self.dataModel.curstom_field[0],self.current_muffler,self.dataModel.curstom_field[1],freq)
            res = self.dataModel.getAllRecordWithCondition(condition,attr)
            if len(res) == 0:
                QtGui.QMessageBox.about(None,"about","No Data")
                return False
            DrawDiagram(res)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about",str(e))
    def setCurrentMuffler(self,value):
        self.current_muffler = value
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
        self.SConnectS(win.ui.btn_help,"clicked()",self.help)
        self.SConnectS(win.ui.box6_btn_import,"clicked()",lambda:self.picTab_exportBtnClick(win.ui))