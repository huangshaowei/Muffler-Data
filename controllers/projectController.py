from .databaseController import *

class ProjectController(DatabaseController):
    def __init__(self):# signal and slot
        DatabaseController.__init__(self)
        self.projectModel = self.getOwnModel("projects")
        self.projectView = QtGui.QDialog()
        self.setupView(self.projectView,Ui_Para_Project_Add_Dlg)
        self.ConnectSlot(self.projectView)
        self.lineEdits=[self.projectView.ui.lineEdit1,self.projectView.ui.lineEdit2,self.projectView.ui.lineEdit3,
                        self.projectView.ui.lineEdit4,self.projectView.ui.lineEdit5,self.projectView.ui.lineEdit6,
                        self.projectView.ui.lineEdit7] #text
        self.lineFiles=[self.projectView.ui.lineEdit8,self.projectView.ui.lineEdit9] #file for read
        self.current_value=None
        pass
    def show(self):
        self.projectView.show()
        pass
    def beforeAdd(self):
        pass
    def addData(self):
        self.current_value= self.getCurrentValue()
        self.projectModel.addNewRecord(self.current_value)
        pass
        
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_ok,"clicked()",self.Add)
        self.SConnectS(win.ui.btn_help,"clicked()",self.help)
        