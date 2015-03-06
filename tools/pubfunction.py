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
    

def InitStandardItemModel(model):# model is standardItemModel
    model.clear()
    model.setColumnCount(2)
    model.setHorizontalHeaderLabels(['property','value'])
    

def InitTreeViewModel(model,custom_field,field_value,num):
    try:
        model.clear()
        model.setRowCount(num)
        model.setHorizontalHeaderItem( 0, QtGui.QStandardItem(custom_field[0]) )
        for r in range(0,num):
            item = QtGui.QStandardItem("%s -- %s"%(custom_field[0],field_value[r][0]))
            item.tag = [0,"%s"%(field_value[r][0])]
            for c in range(0,2):
                    if c == 0:
                        for i in range(1,len(field_value[r])):
                            child = QtGui.QStandardItem("%s -- %s"%(custom_field[i],field_value[r][i]))
                            child.tag = [i,"%s"%(field_value[r][i])]
                            child.setEditable(False)
                            item.appendRow( child )
                    model.setItem(r,c,item)
    except Exception,e:
        QtGui.QMessageBox.about(None,"InitComBox",str(e))


def InitComBox(comboxs,controller):
    [combox.clear() for combox in comboxs]
    if not controller.selectablefield:
        return 
    try:
        for combox in comboxs:
            combox.addItem("")
            for item in controller.selectablefield:
                combox.addItem(controller.model.curstom_field[item-1])
    except Exception,e:
        QtGui.QMessageBox.about(None,"InitComBox",str(e))