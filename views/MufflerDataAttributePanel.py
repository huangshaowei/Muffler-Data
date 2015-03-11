# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\freecad-8-26-all-success\Mod\Muffler\MufflerData\views\MufflerDataAttributePanel.ui'
#
# Created: Tue Mar 10 16:28:17 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MufflerDataAttributePanel(object):
    def setupUi(self, MufflerDataAttributePanel):
        MufflerDataAttributePanel.setObjectName(_fromUtf8("MufflerDataAttributePanel"))
        MufflerDataAttributePanel.resize(361, 467)
        self.tableView = QtGui.QTableView(MufflerDataAttributePanel)
        self.tableView.setGeometry(QtCore.QRect(-10, 20, 371, 421))
        self.tableView.setObjectName(_fromUtf8("tableView"))

        self.retranslateUi(MufflerDataAttributePanel)
        QtCore.QMetaObject.connectSlotsByName(MufflerDataAttributePanel)

    def retranslateUi(self, MufflerDataAttributePanel):
        MufflerDataAttributePanel.setWindowTitle(_translate("MufflerDataAttributePanel", "属性", None))

