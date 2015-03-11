from .databaseController import *
from .dataController import *
from .userController import *

class MufflersController(DatabaseController):
    def __init__(self):
        self.mufflersModel = self.getOwnModel("mufflers")
        self.mufflersView = QtGui.QDialog()
        self.setupView(self.mufflersView,Ui_Para_Muffler_Add_Dlg)
        self.textEdits=[1,2,3,4,5,6]
        self.lineEditsDNEnabled = [1,2]
        self.selectablefield = [1,2,3,4]
        self.dataController = DataController()
    def initializeView(self):
        for t in self.lineEdits:
            if t.__class__ == QtGui.QComboBox:
                t.setCurrentIndex(0)
            else:
                t.clear()
        #self.testinputWidget()
    def beforeAdd(self):
        if not self.check_empty([1,2]):
            return False
        if not self.check_integer([2,4,5]):
            return False
        return True
    def afterAdd(self):
        self.dataController.setCurrentMuffler(self.lineEdits[0].text())
        self.dataController.insertToData(self.mufflersView.ui)
    def generate(self):
        pass
    def registerActions(self,magCtrl):
        self.dataController.setCurrentMuffler(magCtrl.condition[1])
        self.importDataAction= QtGui.QAction('import Data',magCtrl.ViewPanel,triggered=self.importData)
        self.show1000Action  = QtGui.QAction('show Data(1000)',magCtrl.ViewPanel,triggered=self.show1000Data)
        self.show3000Action  = QtGui.QAction('show Data(3000)',magCtrl.ViewPanel,triggered=self.show3000Data)
        return [self.importDataAction,self.show1000Action,self.show3000Action]
    def importMufflerData(self):
        self.dataController.showWidget()
        pass 
    def show1000Data(self):
        self.dataController.showData(1000)
        pass
    def show3000Data(self):
        self.dataController.showData(3000)
        pass
    def ConnectSlot(self,win):
        try:
            self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
            self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
            self.SConnectS(win.ui.btn_help,"clicked()",self.help)
            self.SConnectS(win.ui.box4_btn1,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit))
            self.SConnectS(win.ui.box4_btn2,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit_2))
            self.SConnectS(win.ui.box4_btn3,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit_3))
            self.SConnectS(win.ui.box4_btn4,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit_4))
            self.SConnectS(win.ui.box4_btn5,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit_5))
            self.SConnectS(win.ui.box4_btn6,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit_6))
            self.SConnectS(win.ui.box4_btn7,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit_7))
            self.SConnectS(win.ui.box5_btn1,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit_21))
            self.SConnectS(win.ui.box5_btn2,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit_22))
            self.SConnectS(win.ui.box5_btn3,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit_23))
            self.SConnectS(win.ui.box6_btn_import,"clicked()",lambda:self.picTab_exportBtnClick(win.ui))
        except Exception,e:
            QtGui.QMessageBox.about(None,"about",str(e))