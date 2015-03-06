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
        self.textEdits = []
        self.lineFiles = []
        self.lineEditsCompleter = None
        self.current_value = None
        self.lineEditsDNEnabled = []
        self.selectablefield = None
        return self.model
    def setupView(self,ownview,Ui_View):
        ownview.ui = Ui_View()
        ownview.ui.setupUi(ownview)
        self.view = ownview
    def setupAttributeListView(self,condition,attrmodel,attrs=None):# attrs = ['projectname',...]  res = ['LH-1-3-1',...]
        attrsList = attrs if attrs else self.model.curstom_field
        res = self.model.getAttrsWithSpecialCondition(condition,attrsList)
        self.setupListViewModel(attrmodel,attrsList,res)
    def getAllLineEdits(self,parent):
        lineEdits = []
        if len(parent.children()):
            for obj in parent.children():
                if type(obj) == QtGui.QLineEdit:
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
        if self.textEdits:
            for index in self.textEdits:
                current_value += [self.lineEdits[index-1].text() if self.lineEdits[index-1].text() else '']
        if self.lineFiles:
            for index in self.lineFiles:
                current_value += [self.readValueFromFile(self.lineEdits[index-1])]
        return current_value
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
        