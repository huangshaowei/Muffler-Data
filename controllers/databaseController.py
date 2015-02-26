from ..models import *
from ..views import *
from ..tools import *
from MyDataOperation import *
#########################
from PyQt4 import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

#####################
class DatabaseController(MyDataOperation):
    def __init__(self):
        self.Initialize()
        pass
    def Initialize(self):
        self.mol = ModelsManager(os.getcwd()+"\\..\\Mod\\Database\\MufflerData\\config\\database.xml")
        self.mol.Establish()
    def getOwnModel(self,name):
        check_type(str,name)
        return self.mol.getCorrespondenceModel(name)
    def setupView(self,ownview,Ui_View):
        ownview.ui = Ui_View()
        ownview.ui.setupUi(ownview)
    def SConnectS(self,ui,signal,slot):
        QtCore.QObject.connect(ui,QtCore.SIGNAL(_fromUtf8(signal)),slot)
    def readValueFromFile(self,ui):
        if check_empty(ui):
            return ''
        try:
            fileofUI = QtCore.QFile(ui.text())
            if not fileofUI.open(QtCore.QFile.ReadOnly):
                raise Exception("databaseController: readValueFromFile, the file can be open!")
            fileContent = fileofUI.readAll()
            filetype=ui.text[ui.text.rindex("."):]
            return fileContent.toHex().append(filetype)
        except Exception,e:
            QtGui.QMessageBox.about(None,"about readfile",str(e))
    def getCurrentValue(self):
        current_value = []
        for ui in self.lineEdits:
            current_value +=ui.text()
        for ui in self.lineFiles:
            current_value +=self.readValueFromFile(ui)
        return current_value