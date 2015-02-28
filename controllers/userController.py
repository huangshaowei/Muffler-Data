from .databaseController import *

class UserController(DatabaseController):
    def __init__(self):
        DatabaseController.__init__(self)
        self.userModel = self.getOwnModel("users")
        self.loginView = QtGui.QDialog()
        self.setupView(self.loginView,Ui_System_User_Login_Dlg)
        self.ConnectSlot(self.loginView)
        self.AddUserView = QtGui.QDialog()
        self.setupView(self.AddUserView,Ui_System_User_Add_Dlg)
        self.registerAuthrityFun(self.check_authority)
    def login(self):
        name = {'field':self.userModel.curstom_field[self.userModel.name_field_num],'value':str(self.loginView.ui.lineEdit1.text())}
        passwd = {'field':self.userModel.curstom_field[self.userModel.passwd_field_num],'value':str(self.loginView.ui.lineEdit2.text())}
        if self.userModel.check_currentUser(name,passwd):
            self.loginView.accept()
        else:
            QtGui.QMessageBox.warning(self.loginView,"about Login","username or password is wrong!",QtGui.QMessageBox.Ok)
        # set userpanel
        pass
    def check_login(self):
        if self.userModel.current_user.hadLogin():
            return True
        else:
            if QtGui.QDialog.Accepted == self.loginView.exec_():
                return True
            return False
    def check_authority(self):
        if self.check_login():
            if self.userModel.check_authority() == "admin":
                return True
        return False
    def ConnectSlot(self,win):
        self.SConnectS(win.ui.btn_cancel,"clicked()",win.reject)
        self.SConnectS(win.ui.btn_ok,"clicked()",self.login)
    

