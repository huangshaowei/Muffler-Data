import MyDataOperation
from PyQt4 import QtGui,QtCore
from .projectController import ProjectController
from .userController import UserController
from .carModelController import CarModelController
from .exhaustsController import ExhaustsController
from .employeesController import EmployeesController
from .mufflersController import MufflersController
from .enginesController import EnginesController
from .catalystsController import CatalystsController
from .plansController import PlansController
from .schemesController import SchemesModelController
from .databaseController import *
import os
controllers = [UserController,ProjectController,CarModelController]

class ManagerController(DatabaseController):
    def __init__(self):
        self.ViewPanel = QtGui.QDockWidget()
        self.attributeModel  = QtGui.QStandardItemModel()
        self.setupView(self.ViewPanel,Ui_MufflerDataPanel)
        self.instanceOfControllers  = { 0:UserController(),1: ProjectController(),2:SchemesModelController(),3:PlansController(),4:MufflersController(),5:CarModelController(),6:EnginesController(),7:ExhaustsController(),8:CatalystsController()}#,4:EmployeesController,6:EnginesController}
        self.currentItem = -1
        ####actions####
        self.delAction = QtGui.QAction('Delete',self.ViewPanel,triggered=self.delete)
        self.addAction = QtGui.QAction('Add',self.ViewPanel,triggered=self.Add)
        self.DetAction = QtGui.QAction('Detail',self.ViewPanel,triggered=self.show)
        self.RefAction = QtGui.QAction('reflesh',self.ViewPanel,triggered=self.reflesh)
        ####end #######
        self.treeviewModel = QtGui.QStandardItemModel()
        self.ViewPanel.ui.treeView.setModel(self.treeviewModel)
        ##############
        self.attributeWidget = None 
        InitStandardItemModel(self.attributeModel)
        #self.attributeModel.setColumnCount(2)
        #self.attributeModel.setHorizontalHeaderLabels(['property','value'])
        self.attributeListView = QtGui.QTableView()
        self.attributeListView.setModel(self.attributeModel)
        self.attributeListView.horizontalHeader().setStretchLastSection(True)
        self.selectedRow = None
        self.ConnectSlotBetweenControls()
    def registerAttributeWidget(self,widget):#widget with QListView
        self.attributeWidget = widget
        self.attributeListView.setParent(widget)
    def subjectChange(self,num):
        try:
            #res = self.instanceOfControllers[num].getAllRecoredWithOneFiled()
            self.currentItem = num
            #self.stringListModel = QtGui.QStringListModel(res)
            #self.ViewPanel.ui.listView.setModel(self.stringListModel)
            #InitStandardItemModel(self.attributeModel)
            win = self.ViewPanel.ui
            if num == 0:
                win.pushButton_3.setEnabled(False)
                win.pushButton_4.setEnabled(False)
            else:
                win.pushButton_3.setEnabled(True)
            self.initComBox = True
            InitComBox([win.comboBox2,win.comboBox3,win.comboBox4],self.instanceOfControllers[num])
            self.initComBox = False
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
        pass
    def subjectChange_combox2(self,num):
        self.subjectChange_sub(self.ViewPanel.ui.lineEdit,num)
    def subjectChange_combox3(self,num):
        try:
            self.subjectChange_sub(self.ViewPanel.ui.lineEdit2,num)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
    def subjectChange_combox4(self,num):
        self.subjectChange_sub(self.ViewPanel.ui.lineEdit3,num)
    def subjectChange_sub(self,lineEdit,num):
        if self.initComBox or num == 0:
            return 
        try:
            res = self.instanceOfControllers[self.currentItem].getAllRecoredWithPatticularFiled(num)
            model = QtGui.QStringListModel(res)
            completer = QtGui.QCompleter()
            completer.setModel(model)
            lineEdit.setCompleter(completer)
            lineEdit.tag = num
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
    def Edit_lineEdit(self,s):
        self.itemsChange(self.ViewPanel.ui.lineEdit,s)
    def Edit_lineEdit2(self,s):
        try:
            self.itemsChange(self.ViewPanel.ui.lineEdit2,s)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
    def Edit_lineEdit3(self,s):
        self.itemsChange(self.ViewPanel.ui.lineEdit3,s)
    def itemsChange(self,lineEdit,s):
        try:
            num = lineEdit.tag
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....","please choose one culumn")
            return 
        try:
            res = self.instanceOfControllers[self.currentItem].getAllRecoredWithFuzzyQuery(s,num)
            completer = lineEdit.completer()
            string_list_model = QtGui.QStringListModel(res)
            completer.setModel(string_list_model)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
        pass
    def OnlvOpRighBtn(self,point):
        try:
            popupmenu = QtGui.QMenu(self.ViewPanel.ui.treeView)
            #popupmenu.addAction(self.addAction)
            index = self.ViewPanel.ui.treeView.indexAt(point)
            if index.isValid():
                model = self.ViewPanel.ui.treeView.model()
                self.condition = model.itemFromIndex(index).tag
                popupmenu.addAction(self.delAction)
                if len(self.condition) > 2:
                    popupmenu.addAction(self.DetAction)
            actions = [self.addAction,self.RefAction]
            actions += self.instanceOfControllers[self.currentItem].registerActions(self)
            for action in actions:
                popupmenu.addAction(action)
            #popupmenu.addAction(self.RefAction)
            popupmenu.exec_(self.ViewPanel.ui.treeView.mapToGlobal(point))
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
    def itemChoosed(self,index):#index: QModelIndex
        #self.selectRow = index.row()
        try:
            model = self.ViewPanel.ui.treeView.model()
            self.condition = model.itemFromIndex(index).tag
            if len(self.condition) > 2:
                res = self.instanceOfControllers[self.currentItem].getFileRecordWithCondition(self.condition[1],self.condition[0])[0]
                file = writeFilewithValue(res)
                if file[0]:
                    os.startfile(file[1])
                return 
            self.ViewPanel.ui.pushButton_5.setEnabled(True)
            self.initAttributeModel = True
            self.instanceOfControllers[self.currentItem].setupAttributeListView(self.condition[1],self.attributeModel)
            self.instanceOfControllers[self.currentItem].initializeAttributeListView(self.attributeModel)
            self.initAttributeModel = False
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.comboBox,"currentIndexChanged(int)",self.subjectChange)
        self.SConnectS(win.ui.comboBox2,"currentIndexChanged(int)",self.subjectChange_combox2)
        self.SConnectS(win.ui.comboBox3,"currentIndexChanged(int)",self.subjectChange_combox3)
        self.SConnectS(win.ui.comboBox4,"currentIndexChanged(int)",self.subjectChange_combox4)
        win.ui.comboBox2.tag = win.ui.lineEdit
        win.ui.comboBox3.tag = win.ui.lineEdit2
        win.ui.comboBox4.tag = win.ui.lineEdit3
        #win.ui.listView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.SConnectS(win.ui.listView,"customContextMenuRequested (const QPoint&)",self.OnlvOpRighBtn)
        #self.SConnectS(win.ui.listView,"clicked (const QModelIndex&)",self.itemChoosed)
        self.SConnectS(win.ui.lineEdit,"textChanged (const QString&)",self.Edit_lineEdit)
        self.SConnectS(win.ui.lineEdit2,"textChanged (const QString&)",self.Edit_lineEdit2)
        self.SConnectS(win.ui.lineEdit3,"textChanged (const QString&)",self.Edit_lineEdit3)
        self.SConnectS(self.attributeModel,"itemChanged (QStandardItem *)",self.updateItemFromAttributeModel)
        self.SConnectS(win.ui.pushButton,"clicked()",self.select)
        self.SConnectS(win.ui.treeView,"customContextMenuRequested (const QPoint&)",self.OnlvOpRighBtn)
        self.SConnectS(win.ui.treeView,"clicked (const QModelIndex&)",self.itemChoosed)
        self.SConnectS(win.ui.pushButton_3,"clicked()",self.Add)
        self.SConnectS(win.ui.pushButton_4,"clicked()",self.Add)
        self.SConnectS(win.ui.pushButton_5,"clicked()",self.delete)
    def ConnectSlotBetweenControls(self):
        try:
            for controller in self.instanceOfControllers:
                if self.instanceOfControllers[controller].lineEditsCompleter:
                    for key in self.instanceOfControllers[controller].lineEditsCompleter:
                        connetController = self.getControllerWithModelName(self.instanceOfControllers[controller].lineEditsCompleter[key])
                        if connetController:
                            res = connetController.getAllRecoredWithOneFiled()
                            string_list_model = QtGui.QStringListModel(res)
                            completer = QtGui.QCompleter()
                            completer.setModel(string_list_model)
                            self.instanceOfControllers[controller].lineEdits[key-1].setCompleter(completer)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
    def show(self):
            
        pass
    def beforeSelect(self):
        try:
            win = self.ViewPanel.ui
            comboxs = [win.comboBox2,win.comboBox5,win.comboBox3,win.comboBox6,win.comboBox4]
            condition = QtCore.QStringList()
            for combox in comboxs:
                if not combox.currentText().compare("AND") or not combox.currentText().compare("OR"):
                        condition.append(" %s "%(combox.currentText()))
                else:
                    if combox.currentIndex() > 0:
                        field = self.instanceOfControllers[self.currentItem].getFieldNameFromCombox(combox.currentIndex())
                        value = combox.tag.text()
                        if value.isEmpty():
                            if len(condition) > 0:
                                condition.takeLast()
                            break
                        condition.append(" `%s`='%s' "%(field,value))
                    else:
                        if len(condition) > 0:
                            condition.takeLast()
                        break
            QtGui.QMessageBox.about(None,"about res....",str(condition.isEmpty()))
            return "".join([unicode(s) for s in condition])
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
    def SelectData(self,condition):
        res = self.instanceOfControllers[self.currentItem].select(condition)
        return res
    def afterSelect(self,res):
        InitTreeViewModel(self.treeviewModel,self.instanceOfControllers[self.currentItem].model.curstom_field,res,len(res))
        self.ViewPanel.ui.tabWidget.setCurrentIndex(1)
        self.ViewPanel.ui.pushButton_4.setEnabled(True)
    def addData(self):
        self.instanceOfControllers[self.currentItem].initializeView()
        return self.instanceOfControllers[self.currentItem].showWidget()
    def deleteData(self,num):
        try:
            #condition = self.stringListModel.stringList().takeAt(self.selectRow)
            self.instanceOfControllers[self.currentItem].delete(self.condition[1])
            self.reflesh()
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
        return True
    def updateItemFromAttributeModel(self,item):
        if not self.initAttributeModel:
            self.instanceOfControllers[self.currentItem].update([item,self.condition[1]])
    def reflesh(self):
        #self.subjectChange(self.currentItem)
        self.select()
        self.ViewPanel.ui.pushButton_5.setEnabled(False)
    def getControllerWithModelName(self,name):
        for controller in self.instanceOfControllers:
            if self.instanceOfControllers[controller].model.__name__ == name:
                return self.instanceOfControllers[controller]
        return None


MController = ManagerController()
def getMController():
    return MController


