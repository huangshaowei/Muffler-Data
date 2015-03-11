import hashlib
import os
from PyQt4 import QtGui,QtCore
import pyqtgraph as pg
################################ some functions use in global ################
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
        

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

def readValueFromFile(ui):
    if ui.text().isEmpty():
        return 
    try:
        fileofUI = QtCore.QFile(ui.text())
        if not fileofUI.open(QtCore.QFile.ReadOnly):
            raise Exception("databaseController: readValueFromFile, the file can be open!")
        fileContent = fileofUI.readAll()
        filetype=ui.text()[ui.text().indexOf("."):]
        return fileContent.toHex().append(filetype)
    except Exception,e:
        QtGui.QMessageBox.about(None,"about readfile",str(e))

def writeFilewithValue(text):
    try:
        fileName = os.getcwd()+"\\..\\Mod\\Muffler\\MufflerData\\config\\temp"+text[text.index("."):]
        filecontent = QtCore.QByteArray(text[:text.index(".")])
        file = QtCore.QFile(fileName)
        if not file.open(QtCore.QFile.WriteOnly):
            QtGui.QMessageBox.about(None,"about",_fromUtf8("file show faild"))
            file.close()
            return [False,""]
        file.write(QtCore.QByteArray.fromHex(filecontent))
        file.close()
        return [True,fileName]
    except Exception,e:
        QtGui.QMessageBox.about(None,"about res....",str(e))

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
                            child.tag = [i,"%s"%(field_value[r][0])]
                            child.setEditable(False)
                            item.appendRow( child )
                        if len(field_value[r]) < len(custom_field):
                            for i in range(len(field_value[r]),len(custom_field)):
                                child = QtGui.QStandardItem("%s -- %s"%(custom_field[i],"file"))
                                child.tag = [i,"%s"%(field_value[r][0]),"file"]
                                child.setEditable(False)
                                item.appendRow( child )
                    model.setItem(r,c,item)
    except Exception,e:
        QtGui.QMessageBox.about(None,"InitTreeViewModel",str(e))


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



designCenterWindow = None
designImageWindow = None
def getWindowFromObjectName(parentWindow,objectName,flag=False):
  global designCenterWindow
  global designImageWindow
  try:        
    if objectName == "DesignCenter" :
        list = parentWindow.subWindowList()
        subWin = None
        if list != []:
            for li in list:
                if li.widget().objectName() == objectName:
                    subWin =  li
                    break
        if subWin == None:
            subWin = QtGui.QMdiSubWindow()
            parentWindow.addSubWindow(subWin)
            subWin.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
            designCenterWindow = QtGui.QTableWidget()
            designCenterWindow.setObjectName(objectName)
            designImageWindow = pg.GraphicsWindow(title = objectName)
            designImageWindow.setBackground('w')
            designImageWindow.setObjectName(objectName)
            designImageWindow.hide()
        if flag==False:  
            subWin.setWidget(designCenterWindow)
            subWin.setWindowTitle(objectName)
        else:             
            subWin.setWidget(designImageWindow)
            subWin.setWindowTitle(objectName)
        subWin.show()
        parentWindow.setActiveSubWindow(subWin)
        return subWin
    elif objectName == "imageCenter":
        list = parentWindow.subWindowList()
        if list != []:
           for li in list:
               if li.widget().objectName() == objectName:
                    parentWindow.setActiveSubWindow(li)
                    return   li
  except Exception,e:
    QtGui.QMessageBox.about(None,"about",str(e))

m_plot = []
color_id = 0
def DrawDiagram(res):
    global m_plot,color_id
    x = []
    y = []
    num = len(res)
    for i in range(0,num):
        x += [float(res[i][0])]
        y += [float(res[i][1])]
    Mdi = getMdiArea()
    subwin = getWindowFromObjectName(Mdi,"DesignCenter",True).widget()
    subwin.show()
    color = ['b','r','g','y',(0,255,255),(255,0,255),(0,0,0)]
    if m_plot == []:
        p = subwin.addPlot(0,0)
        p.setLabel('left','TL[dB]')
        p.setLabel('bottom','FREQ[Hz]')
        m_plot += [p]
    m_plot[0].plot(x,y,pen=color[color_id])
    color_id += 1
    if color_id == 7:
        color_id = 0



################################some function comes from FreeCAD##############3
def getMainWindow():
    topLevels = QtGui.qApp.topLevelWidgets()
    for i in topLevels:
        if i.metaObject().className() == "Gui::MainWindow":
            return i
    raise  Exception("No main window found")

mw = QtGui.QApplication.activeWindow()

def getMdiArea():
    for i in mw.children():
        if i.metaObject().className() == "QMdiArea":
            return i
    raise  Exception("No MdiArea found")