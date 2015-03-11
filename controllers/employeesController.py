from .databaseController import *
from .userController import *

class EmployeesController(DatabaseController):
    def __init__(self):
        self.employeesModel = self.getOwnModel("employees")
        self.employeeView = QtGui.QDialog()
        self.setupView(self.employeeView,Ui_Para_Employee_Add_Dlg)
        self.ConnectSlot(self.employeesModel)
        self.textEdits=[1,2,3,4,5,6]
        self.lineEditsDNEnabled = [1,2]
        self.selectablefield = [1,2,3,4]
    def initializeView(self):
        for t in self.lineEdits:
            t.clear()
    def beforeAdd(self):
        if not self.check_empty([1,2]):
            return False
        return True
    def generate(self):
        pass
    def ConnecSlot(self,win):
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
        self.SConnectS(win.ui.btn_help,"clicked()",self.help)