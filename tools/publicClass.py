from PyQt4 import QtGui,QtCore


class SpinBoxDelegate(QtGui.QItemDelegate):
    def __init__(self,parent=None):
        super(SpinBoxDelegate,self).__init__(parent)
    def createEditor(self,parent,option,index):
        editor = QtGui.QPushButton(parent) #QtGui.QSpinBox(parent)
        #editor.setMinimum(0)
        #editor.setMaximum(100)
        editor.setText("X")
        return editor
    def setEditorData(self,editor,index):
        value = index.model().data(index,QtCore.Qt.EditRole).toInt()
        editor.setValue(value)
    def setModelData(self,editor,model,index):
        spinBox.interpretText()
        value = spinBox.value()
        model.setData(index,value,QtCore.Qt.EditRole)
    def updateEditorGeometry(self,editor,option,index):
        editor.setGeometry(rect)





model = QtGui.QStandardItemModel(4,2)
tableView = QtGui.QTableView()
tableView.setModel(model)
delegate = SpinBoxDelegate()
tableView.setItemDelegate(delegate)
tableView.horizontalHeader().setStretchLastSection(True)

for row in range(0,4):
    for column in range(0,2):
        index = model.index(row,column,QtCore.QModelIndex())
        model.setData(index,QtCore.QVariant((row+1)*(column+1)))




tableView.setWindowTitle("Spin Box Delegate")
tableView.show()