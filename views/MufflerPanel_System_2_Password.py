# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\freecad-8-26-all-success\Mod\Muffler\MufflerData\views\MufflerPanel_System_2_Password.ui'
#
# Created: Fri Mar 06 11:16:42 2015
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

class Ui_System_Password_Dlg(object):
    def setupUi(self, System_Password_Dlg):
        System_Password_Dlg.setObjectName(_fromUtf8("System_Password_Dlg"))
        System_Password_Dlg.resize(315, 234)
        System_Password_Dlg.setMinimumSize(QtCore.QSize(315, 234))
        System_Password_Dlg.setMaximumSize(QtCore.QSize(315, 234))
        System_Password_Dlg.setModal(False)
        self.btn_ok = QtGui.QPushButton(System_Password_Dlg)
        self.btn_ok.setGeometry(QtCore.QRect(70, 180, 75, 23))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_cancel = QtGui.QPushButton(System_Password_Dlg)
        self.btn_cancel.setGeometry(QtCore.QRect(170, 180, 75, 23))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lineEdit1 = QtGui.QLineEdit(System_Password_Dlg)
        self.lineEdit1.setGeometry(QtCore.QRect(120, 40, 161, 20))
        self.lineEdit1.setText(_fromUtf8(""))
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.label1 = QtGui.QLabel(System_Password_Dlg)
        self.label1.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.label1.setStyleSheet(_fromUtf8(""))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.lineEdit2 = QtGui.QLineEdit(System_Password_Dlg)
        self.lineEdit2.setGeometry(QtCore.QRect(120, 80, 161, 20))
        self.lineEdit2.setText(_fromUtf8(""))
        self.lineEdit2.setObjectName(_fromUtf8("lineEdit2"))
        self.label2 = QtGui.QLabel(System_Password_Dlg)
        self.label2.setGeometry(QtCore.QRect(40, 80, 71, 16))
        self.label2.setStyleSheet(_fromUtf8(""))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.label3 = QtGui.QLabel(System_Password_Dlg)
        self.label3.setGeometry(QtCore.QRect(40, 120, 71, 16))
        self.label3.setStyleSheet(_fromUtf8(""))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.lineEdit3 = QtGui.QLineEdit(System_Password_Dlg)
        self.lineEdit3.setGeometry(QtCore.QRect(120, 120, 161, 20))
        self.lineEdit3.setText(_fromUtf8(""))
        self.lineEdit3.setObjectName(_fromUtf8("lineEdit3"))

        self.retranslateUi(System_Password_Dlg)
        QtCore.QMetaObject.connectSlotsByName(System_Password_Dlg)

    def retranslateUi(self, System_Password_Dlg):
        System_Password_Dlg.setWindowTitle(_translate("System_Password_Dlg", "密码管理界面", None))
        self.btn_ok.setText(_translate("System_Password_Dlg", "更改", None))
        self.btn_cancel.setText(_translate("System_Password_Dlg", "取消", None))
        self.label1.setText(_translate("System_Password_Dlg", "用户名", None))
        self.label2.setText(_translate("System_Password_Dlg", "新密码", None))
        self.label3.setText(_translate("System_Password_Dlg", "确认新密码", None))

