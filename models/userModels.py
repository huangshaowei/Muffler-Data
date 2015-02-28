from MyDataModel import *
from .currentUser import getCurrentUser

class Users(MyDataModel):
    def __init__(self,_successor=None):
        self.node = None
        self.curstom_field = None
        self._successor = _successor
        self.__name__="users"
        self.current_user = getCurrentUser()
        self.name_field_num = 1
        self.passwd_field_num = 2
    def check_currentUser(self,name,passwd):#name,passwd must be dirt , it must be use only in 
        if self.current_user.hadLogin():
            return True 
        try:
            sqlword = "select `%s`,`%s` from users where `%s` = '%s';"%(passwd['field'],self.curstom_field[3],name['field'],name['value'])
            res = [ str(item) for item in MySQLOperation.mysql_exec_res(sqlword)]
        except Exception,e:
            QtGui.QMessageBox.about(None,"about check users",str(e))
        if check_empty_l(res):
            return False 
        try:
            if compare_value_and_encry(passwd['value'],res[0]):
                self.current_user.login(name['value'],res[1])
                return True
        except Exception,e:
            QtGui.QMessageBox.about(None,"about login",str(e))
        return False 
    def check_authority(self): # needs the authority level
        if self.current_user.hadLogin():
            return self.current_user.check_authority()
        return 0