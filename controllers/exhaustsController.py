from .databaseController import *
from .userController import *

class ExhaustsController(DatabaseController):
    def __init__(self):
        self.exhaustsModel = self.getOwnModel("exhausts")
        self.exhaustsView = QtGui.QDialog()
        self.setupView(self.exhaustsView,Ui_Para_Exhaust_Add_Dlg)
        self.textEdits=[1,2,3]
        self.lineFiles=[4,5,6]
        self.lineEditsDNEnabled = [1]
        self.selectablefield = [1,2,3]
    def initializeView(self):
        for t in self.lineEdits:
            t.clear()
    def beforeAdd(self):
        if not self.check_empty([1]):
            return False
        return True
    def generate(self):
        pass
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
        self.SConnectS(win.ui.btn_help,"clicked()",self.help)
        self.SConnectS(win.ui.btn_lineEdit4,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit4))
        self.SConnectS(win.ui.btn_lineEdit5,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit5))
        self.SConnectS(win.ui.btn_lineEdit6,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit6))