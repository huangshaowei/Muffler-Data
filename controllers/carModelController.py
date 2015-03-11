from .databaseController import *
from .userController import *

class CarModelController(DatabaseController):
    def __init__(self):
        self.carModel = self.getOwnModel("models")
        self.carModelView = QtGui.QDialog()
        self.setupView(self.carModelView,Ui_Para_MotoType_Add_Dlg)
        self.textEdits = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.lineEditsDNEnabled = [1]
        self.selectablefield = [1,2,3,4,5]
    def initializeView(self):
        for lineEdit in self.lineEdits:
            lineEdit.clear()
        pass
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_help,"clicked()",self.help)