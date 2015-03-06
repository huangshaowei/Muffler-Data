from .databaseController import *
from .userController import *

class ProjectController(DatabaseController):
    def __init__(self):# signal and slot
        self.projectModel = self.getOwnModel("projects")
        self.projectView = QtGui.QDialog()
        self.setupView(self.projectView,Ui_Para_Project_Add_Dlg)
        self.ConnectSlot(self.projectView)
        self.textEdits=[1,2,3,4,5,6,7] #text
        self.lineFiles=[8,9] #file for read
        self.lineEditsDNEnabled = [ 1,5,6] #lineEdit can't be change in update
        self.lineEditsCompleter = {3:"models"} #lineEdit can complete the text
        self.selectablefield = [1,2,3,4,5]
        self.current_value=None
        self.lineEdits= self.getAllLineEdits(self.projectView)
        pass
    def initializeView(self):
        for t in self.lineEdits:
            t.clear()
        self.lineEdits[self.textEdits[4]].setText(self.getUserController().userModel.current_user.name)
        self.lineEdits[self.textEdits[5]].setText(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
    def beforeAdd(self):
        if not self.check_empty([1,2,5]):
            return False
        if not self.check_integer([5]):
            return False
        self.projectView.accept()
        return True
    def generate(self):
        self.lineEdits[self.textEdits[0]-1].setText("LH-1-4-1")
        pass
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
        self.SConnectS(win.ui.btn_help,"clicked()",self.help)
        self.SConnectS(win.ui.btn_generate,"clicked()",self.generate)
        self.SConnectS(win.ui.btn_lineEdit8,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit8))
        self.SConnectS(win.ui.btn_lineEdit9,"clicked()",lambda:self.fileDialogOpen(win.ui.lineEdit9))