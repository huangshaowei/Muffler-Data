from ..models import *
from ..views import *
from ..tools import *

import time
from MyDataOperation import *
#########################
from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

mol = None

#####################
class DatabaseController(MyDataOperation):
    def __init__(self):
        self.Initialize()
        pass
    def Initialize(self):
        global mol
        mol = ModelsManager(os.getcwd()+"\\..\\Mod\\Muffler\\MufflerData\\config\\database.xml")
        mol.Establish()
    def getOwnModel(self,name):
        check_type(str,name)
        global mol
        self.model = mol.getCorrespondenceModel(name)
        self.lineEditsCompleter = None
        self.current_value = None
        self.lineEditsDNEnabled = []
        self.selectablefield = None
        return self.model
    def setupView(self,ownview,Ui_View):
        ownview.ui = Ui_View()
        ownview.ui.setupUi(ownview)
        self.view = ownview
        self.lineEdits = self.getAllLineEdits(ownview)
        self.ConnectSlot(self.view)
    def setupAttributeListView(self,condition,attrmodel,attrs=None):# attrs = ['projectname',...]  res = ['LH-1-3-1',...]
        #attrsList = attrs if attrs else self.model.curstom_field
        attrsList = attrs if attrs else [self.model.curstom_field[num-1] for num in self.textEdits]
        res = self.model.getAttrsWithSpecialCondition(condition,attrsList)
        self.setupListViewModel(attrmodel,attrsList,res)
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
        self.SConnectS(win.ui.btn_help,"clicked()",self.help)
    def getAllLineEdits(self,parent):
        lineEdits = []
        if len(parent.children()):
            for obj in parent.children():
                if type(obj) == QtGui.QLineEdit or type(obj) == QtGui.QComboBox or type(obj) == QtGui.QPlainTextEdit:
                    lineEdits += [obj]
                else:
                    lineEdits += self.getAllLineEdits(obj)
            return lineEdits
        else:
            return []
    def setupListViewModel(self,attrmodel,attrs,res):
        try:
            attrmodel.setRowCount(len(attrs))
            attrs_res = attrs + res
            row_len = attrmodel.rowCount()
            column_len = attrmodel.columnCount()
            for column in range(0,column_len):
                for row in range(0,row_len):
                    index = attrmodel.index(row,column,QtCore.QModelIndex())
                    attrmodel.setData(index,attrs_res[column*row_len+row])
        except Exception,e:
            QtGui.QMessageBox.about(None,"about sqlword",str(e))
    def updateData(self,cons):
        item = cons[0]
        condition = cons[1]
        try:
            self.model.updateOneField(item.row(),item.text(),condition)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about sqlword",str(e))
    def addData(self):
        if self.view:
            if self.view.accept() == QtGui.QDialog.Rejected:
                return False
        self.current_value= self.getCurrentValue()
        return self.model.addNewRecord(self.current_value)
    def deleteData(self,obj):
        index = self.model.getAttrsWithSpecialCondition(obj,['id'])
        return self.model.deleteRecored(index[0])
    def SelectData(self,condition):
        return self.model.getAllRecordWithCondition(condition,self.textEdits)
    def initializeAttributeListView(self,attrModel):#setup special field
        try:
            for index in self.lineEditsDNEnabled:
                item = attrModel.item(index-1,1)
                item.setEnabled(False)
                item.setSelectable(False)
            for index in range(0,attrModel.rowCount()):
                item = attrModel.item(index,0)
                item.setEnabled(False)
                item.setSelectable(False)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about sqlword",str(e))
    def SConnectS(self,ui,signal,slot):
        QtCore.QObject.connect(ui,QtCore.SIGNAL(_fromUtf8(signal)),slot)
    def readValueFromFile(self,ui):
        if check_empty(ui):
            return ''
        try:
            fileofUI = QtCore.QFile(ui.text())
            if not fileofUI.open(QtCore.QFile.ReadOnly):
                raise Exception("databaseController: readValueFromFile, the file can be open!")
            fileContent = fileofUI.readAll()
            filetype=ui.text()[ui.text().indexOf("."):]
            return fileContent.toHex().append(filetype)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about readfile",str(e))
    def getFieldNameFromCombox(self,index):
        return self.model.curstom_field[self.selectablefield[index-1]-1]
    def getCurrentValue(self):
        current_value = []
        for inputWidget in self.lineEdits:
            if inputWidget.__class__ == QtGui.QLineEdit:
                if inputWidget.toolTip() == "lineFiles":
                    current_value += ['' if inputWidget.text().isEmpty() else self.readValueFromFile(inputWidget)]
                else:
                    current_value += [inputWidget.text() if not inputWidget.text().isEmpty() else '']
            elif inputWidget.__class__ == QtGui.QComboBox:
                if inputWidget.toolTip() == "notfield":
                    continue
                current_value += [inputWidget.currentText()]
            elif inputWidget.__class__ == QtGui.QPlainTextEdit:
                current_value += [inputWidget.toPlainText()]
        #if self.textEdits:
        #    for index in self.textEdits:
        #        current_value += [self.lineEdits[index-1].text() if self.lineEdits[index-1].text() else '']
        #if self.lineFiles:
        #    for index in self.lineFiles:
        #        current_value += [self.readValueFromFile(self.lineEdits[index-1])]
        return current_value
    def getFileRecordWithCondition(self,condition,num):
        return self.model.getAttrsWithSpecialCondition(condition,[self.model.curstom_field[num]])
    def getAllRecord(self):
        return self.model.getAllRecored()
    def getAllRecoredWithOneFiled(self):
        return [item[0] for item in self.model.getAllRecoredWithOneFiled()]
    def getAllRecoredWithPatticularFiled(self,num):
        return [item[0] for item in self.model.getAllRecoredWithPatticularFiled(self.selectablefield[num-1])]
    def getAllRecoredWithFuzzyQuery(self,part,num=0):
        return [item[0] for item in self.model.getAllRecoredWithFuzzyQuery(str(part),num)]
    def showWidget(self):
        return self.view.exec_()
    def testinputWidget(self):
        for index in range(0,len(self.lineEdits)):
            if self.lineEdits[index].__class__ == QtGui.QLineEdit:
                if self.lineEdits[index].toolTip() == "lineFiles":
                    self.lineEdits[index].setText(QtCore.QString("lineFiles"+str(index)))
                else:
                    self.lineEdits[index].setText(QtCore.QString("linetext"+str(index)))
            elif self.lineEdits[index].__class__ == QtGui.QComboBox:
                self.lineEdits[index].setCurrentIndex(1)
    def picTab_exportBtnClick(self,taWidgets): #import xls
        filename = QtGui.QFileDialog.getOpenFileName(None,"Export Data","./","XLS(*xls)")
        if filename.isEmpty():
            return
        try:
            t = taWidgets.box6_comboBox.currentText()
            book = xlrd.open_workbook(filename.toAscii())
            sh = book.sheet_by_index(0)
            count = sh.nrows
            taWidgets.box6_progressBar.setMaximum(count-1)
            taWidgets.box6_tableWidget1.setHorizontalHeaderLabels([sh.cell_value(0,0),sh.cell_value(0,1)])
            taWidgets.box6_tableWidget2.setHorizontalHeaderLabels([sh.cell_value(0,0),sh.cell_value(0,1)])
            count1 = 0
            count2 = 0
            for i in range(1,count):
                t1 = sh.cell_value(i,0)
                t2 = sh.cell_value(i,1)
                if t == "3000":
                    taWidgets.box6_tableWidget2.insertRow(count1)
                    myitem1 = QtGui.QTableWidgetItem(_fromUtf8(str(t1)))
                    myitem2 = QtGui.QTableWidgetItem(_fromUtf8(str(t2)))
                    taWidgets.box6_tableWidget2.setItem(count1,0,myitem1)
                    taWidgets.box6_tableWidget2.setItem(count1,1,myitem2)
                    count1 += 1
                else:
                    taWidgets.box6_tableWidget1.insertRow(count2)
                    myitem1 = QtGui.QTableWidgetItem(_fromUtf8(str(t1)))
                    myitem2 = QtGui.QTableWidgetItem(_fromUtf8(str(t2)))
                    taWidgets.box6_tableWidget1.setItem(count2,0,myitem1)
                    taWidgets.box6_tableWidget1.setItem(count2,1,myitem2)
                    count2 += 1
                taWidgets.box6_progressBar.setValue(i)
            pass
        except Exception,e:
            QtGui.QMessageBox.about(None,"about picTab_exportBtnClick",str(e))
    def check_primary(self,num):
        res = self.getAllRecoredWithOneFiled()
        if res.__contains__(self.lineEdits[num-1].text()):
            QtGui.QMessageBox.about(None,"about integer",self.lineEdits[num-1].text()+" is exised!")
            return False
        return True
    def registerActions(self,magCtrl):
        return []
        