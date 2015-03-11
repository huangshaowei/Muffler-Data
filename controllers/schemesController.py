from .databaseController import *
from .userController import *

class SchemesModelController(DatabaseController):
    def __init__(self):
        self.schemesModel = self.getOwnModel("schemes")
        self.schemesView = QtGui.QDialog()
        self.setupView(self.schemesView,Ui_Para_Schemes_Add_Dlg)
        self.textEdits = [1,2,3,4]
        self.lineEditsDNEnabled = [1]
        self.lineEditsCompleter={3:"projects"}
        self.selectablefield = [1,2,3,4]
    def initializeView(self):
        for lineEdit in self.lineEdits:
            lineEdit.clear()
        pass
    def beforeAdd(self):
        if not self.check_empty([1,2,3]):
            return False
        if not self.check_primary(1):
            return False
        return True
    def generate(self):
        self.schemesView.ui.lineEdit.setText("sechme-kgb")
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_help,"clicked()",self.help)
        self.SConnectS(win.ui.pushButton,"clicked()",self.generate)