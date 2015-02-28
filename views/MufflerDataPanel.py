# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\freecad-8-26-all-success\Mod\Muffler\MufflerData\views\MufflerDataPanel.ui'
#
# Created: Fri Feb 27 10:56:45 2015
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

class Ui_MufflerDataPanel(object):
    def setupUi(self, MufflerDataPanel):
        MufflerDataPanel.setObjectName(_fromUtf8("MufflerDataPanel"))
        MufflerDataPanel.resize(356, 467)
        self.groupBox = QtGui.QGroupBox(MufflerDataPanel)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 331, 55))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 84, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(150, 20, 162, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.lineEdit = QtGui.QLineEdit(MufflerDataPanel)
        self.lineEdit.setGeometry(QtCore.QRect(10, 130, 331, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(MufflerDataPanel)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 72, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.listView = QtGui.QListView(MufflerDataPanel)
        self.listView.setGeometry(QtCore.QRect(10, 160, 331, 291))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listView.setFont(font)
        self.listView.setObjectName(_fromUtf8("listView"))

        self.retranslateUi(MufflerDataPanel)
        QtCore.QMetaObject.connectSlotsByName(MufflerDataPanel)

    def retranslateUi(self, MufflerDataPanel):
        MufflerDataPanel.setWindowTitle(_translate("MufflerDataPanel", "MufflerData", None))
        self.groupBox.setTitle(_translate("MufflerDataPanel", "选项", None))
        self.label_2.setText(_translate("MufflerDataPanel", "需要查询的内容", None))
        self.comboBox.setItemText(0, _translate("MufflerDataPanel", "项目信息管理", None))
        self.comboBox.setItemText(1, _translate("MufflerDataPanel", "子方案信息管理", None))
        self.comboBox.setItemText(2, _translate("MufflerDataPanel", "消声器信息管理", None))
        self.comboBox.setItemText(3, _translate("MufflerDataPanel", "车型信息管理", None))
        self.comboBox.setItemText(4, _translate("MufflerDataPanel", "发动机信息管理", None))
        self.comboBox.setItemText(5, _translate("MufflerDataPanel", "排气歧管信息管理", None))
        self.comboBox.setItemText(6, _translate("MufflerDataPanel", "催化器信息管理", None))
        self.comboBox.setItemText(7, _translate("MufflerDataPanel", "员工信息管理", None))
        self.label_3.setText(_translate("MufflerDataPanel", "输入关键字：", None))

