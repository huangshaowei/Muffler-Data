from .databaseController import *
from .userController import *

class EnginesController(DatabaseController):
    def __init__(self):
        self.enginesModel = self.getOwnModel("engines")
        self.enginesView  = QtGui.QDialog()
        self.setupView(self.enginesView,Ui_Para_Engine_Add_Dlg)
        self.textEdits = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
        self.selectablefield = [1,2,3]
        self.lineEditsDNEnabled = [1]
        #self.lineFiles = [4,5,6,7]
        self.lineEdits = self.getAllLineEdits(self.enginesView)
    def initializeView(self):
        for lineEdit in self.lineEdits:
            lineEdit.clear()
        pass
    def beforeAdd(self):
        if not self.check_empty([1,2]):
            return False
        if not self.check_integer([2,3,9,10,12,13,14,15,16,17,18,19,20,21,22,23]):
            return False
        return True
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_help,"clicked()",self.help)