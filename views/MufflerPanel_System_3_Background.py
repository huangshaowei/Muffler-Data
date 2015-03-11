# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\freecad-8-26-all-success\Mod\Muffler\MufflerData\views\MufflerPanel_System_3_Background.ui'
#
# Created: Tue Mar 10 16:28:19 2015
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

class Ui_System_Background_Dlg(object):
    def setupUi(self, System_Background_Dlg):
        System_Background_Dlg.setObjectName(_fromUtf8("System_Background_Dlg"))
        System_Background_Dlg.resize(474, 142)
        System_Background_Dlg.setMinimumSize(QtCore.QSize(474, 142))
        System_Background_Dlg.setMaximumSize(QtCore.QSize(474, 142))
        System_Background_Dlg.setModal(False)
        self.btn_browse = QtGui.QPushButton(System_Background_Dlg)
        self.btn_browse.setGeometry(QtCore.QRect(270, 70, 75, 23))
        self.btn_browse.setObjectName(_fromUtf8("btn_browse"))
        self.btn_default = QtGui.QPushButton(System_Background_Dlg)
        self.btn_default.setGeometry(QtCore.QRect(360, 70, 75, 23))
        self.btn_default.setObjectName(_fromUtf8("btn_default"))
        self.lineEdit = QtGui.QLineEdit(System_Background_Dlg)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 211, 20))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(System_Background_Dlg)
        self.label.setGeometry(QtCore.QRect(40, 40, 121, 16))
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(System_Background_Dlg)
        QtCore.QMetaObject.connectSlotsByName(System_Background_Dlg)

    def retranslateUi(self, System_Background_Dlg):
        System_Background_Dlg.setWindowTitle(_translate("System_Background_Dlg", "更换图片/Change picture", None))
        self.btn_browse.setText(_translate("System_Background_Dlg", "浏览", None))
        self.btn_default.setText(_translate("System_Background_Dlg", "默认", None))
        self.label.setText(_translate("System_Background_Dlg", "设置主界面背景图片：", None))

