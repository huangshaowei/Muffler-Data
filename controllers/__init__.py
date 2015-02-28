import MyDataOperation
from PyQt4 import QtGui,QtCore
from .projectController import ProjectController
from .userController import UserController
from .databaseController import *

controllers = [UserController,ProjectController]

class ManagerController(DatabaseController):
    def __init__(self):
        self.ViewPanel = QtGui.QDockWidget()
        self.setupView(self.ViewPanel,Ui_MufflerDataPanel)
        self.instanceOfControllers  = { 0:UserController(),1: ProjectController()}
        self.currentItem = -1
        self.ConnectSlot(self.ViewPanel)
        ####actions####
        self.delAction = QtGui.QAction('Delete',self.ViewPanel,triggered=self.delete)
        self.addAction = QtGui.QAction('Add',self.ViewPanel,triggered=self.Add)
        self.DetAction = QtGui.QAction('Detail',self.ViewPanel,triggered=self.show)
        
    def subjectChange(self,num):
        try:
            res = self.instanceOfControllers[num].getAllRecoredWithOneFiled()
            self.currentItem = num
            InsertItems(self.ViewPanel.ui.listView,res)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
        pass
    def itemsChange(self,s):
        try:
            res = self.instanceOfControllers[self.currentItem].getAllRecoredWithFuzzyQuery(s)
            InsertItems(self.ViewPanel.ui.listView,res)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about res....",str(e))
        pass
    def OnlvOpRighBtn(self,point):
        popupmenu = QtGui.QMenu(self.ViewPanel.ui.listView)
        index = self.ViewPanel.ui.listView.indexAt(point)
        if index.isValid():
            popupmenu.addAction(self.delAction)
        popupmenu.addAction(self.addAction)
        popupmenu.addAction(self.DetAction)
        popupmenu.exec_(self.ViewPanel.ui.listView.mapToGlobal(point))
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.comboBox,"currentIndexChanged(int)",self.subjectChange)
        win.ui.listView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.SConnectS(win.ui.listView,"customContextMenuRequested (const QPoint&)",self.OnlvOpRighBtn)
        self.SConnectS(win.ui.lineEdit,"textChanged (const QString&)",self.itemsChange)
    def show(self):
        pass
    def addData(self):
        self.instanceOfControllers[self.currentItem].showWidget()

MController = ManagerController()
def getMController():
    return MController


