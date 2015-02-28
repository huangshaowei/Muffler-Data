
import time
class currentUser:
    def __init__(self):
        self.name = None
        self.authority = None
    def check_authority(self):
        return self.authority
    def login(self,name,authority):
        self.name = name
        self.authority = authority
        self.logintime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        pass
    def logout(self):
        self.name = None
        self.authority = None
        self.logouttime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        # log daily oper ...
    def hadLogin(self):
        if self.name == None:
            return False
        return True

current_user = currentUser()

def getCurrentUser():
    return current_user