from .databaseController import *
from .userController import *

class PlansController(DatabaseController):
    def __init__(self):
        self.plansModel = self.getOwnModel("plans")
        self.plansView  = QtGui.QDialog()
        self.setupView(self.plansView,Ui_Para_Plan_Add_Dlg)
        self.textEdits = [1,2,3]
        self.lineFiles = [4,5,6,7]
        self.selectablefield = [1,2,3,4,5,6,7]
        self.lineEditsDNEnabled = [1]
        self.lineEditsCompleter = {3:"schemes",4:"exhausts",5:"catalysts",6:"mufflers",7:"mufflers",8:"mufflers"}
    def initializeView(self):
        for lineEdit in self.lineEdits:
            lineEdit.clear()
        #self.testinputWidget()
        pass
    def beforeAdd(self):
        if not self.check_empty([1,2]):
            return False
        if not self.check_primary(1):
            return False
        return True
    def generate(self):
        self.lineEdits[0].setText("new-child-plan")
        pass
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_help,"clicked()",self.help)
        self.SConnectS(win.ui.btn_lineEdit16,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit14))
        self.SConnectS(win.ui.btn_lineEdit17,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit15))
        self.SConnectS(win.ui.btn_generate1,"clicked()",self.generate)