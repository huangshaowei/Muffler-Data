import hashlib
from PyQt4 import QtGui,QtCore
################################ some functions use in global ################


def check_type(prototype,target):
    if not isinstance(target,prototype):
        raise BaseException("find:index is not a " +str(type(prototype())))
        

def check_empty(target): #str
    if target.text() == '':
        return True
        

def check_empty_l(target):
    if len(target) == 0:
        return True
    else:
        return False

def compare_value_and_encry(value,target):
    if encryption(value) == target:
        return True
    else:
        return False

def encryption(target):
    check_type(str,target)
    return hashlib.md5(target.lower()).hexdigest()

def get_str(target):
    return " '%s'"%(target)
    


################################some functions concern about qt widget #######

def InsertItems(listView,items):
    slm = QtGui.QStringListModel(items)
    listView.setModel(slm)
    
