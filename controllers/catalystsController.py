from .databaseController import *
from .userController import *

class CatalystsController(DatabaseController):
    def __init__(self):
        self.catalystsModel = self.getOwnModel("catalysts")
        self.catalystsView  = QtGui.QDialog()
        self.setupView(self.catalystsView,Ui_Para_Catalyst_Add_Dlg)
        self.textEdits = [1,2,3]
        self.lineEditsDNEnabled=[1]
        self.selectablefield = [1,2,3]
    def initializeView(self):
        for lineEdit in self.lineEdits:
            lineEdit.clear()
        pass
    def beforeAdd(self):
        if not self.check_empty([1,2]):
            return False
        if not self.check_primary(1):
            return False
        return True
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_help,"clicked()",self.help)
        self.SConnectS(win.ui.btn_lineEdit4,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit4))
        self.SConnectS(win.ui.btn_lineEdit5,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit5))
        self.SConnectS(win.ui.btn_lineEdit6,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit6))
        self.SConnectS(win.ui.btn_lineEdit7,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit7))
        