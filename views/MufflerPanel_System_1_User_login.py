# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\freecad-8-26-all-success\Mod\Muffler\MufflerData\views\MufflerPanel_System_1_User_login.ui'
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

class Ui_System_User_Login_Dlg(object):
    def setupUi(self, System_User_Login_Dlg):
        System_User_Login_Dlg.setObjectName(_fromUtf8("System_User_Login_Dlg"))
        System_User_Login_Dlg.resize(400, 300)
        System_User_Login_Dlg.setMinimumSize(QtCore.QSize(400, 300))
        System_User_Login_Dlg.setMaximumSize(QtCore.QSize(400, 300))
        System_User_Login_Dlg.setModal(False)
        self.btn_ok = QtGui.QPushButton(System_User_Login_Dlg)
        self.btn_ok.setGeometry(QtCore.QRect(60, 220, 75, 23))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_cancel = QtGui.QPushButton(System_User_Login_Dlg)
        self.btn_cancel.setGeometry(QtCore.QRect(150, 220, 75, 23))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lineEdit1 = QtGui.QLineEdit(System_User_Login_Dlg)
        self.lineEdit1.setGeometry(QtCore.QRect(140, 70, 171, 20))
        self.lineEdit1.setText(_fromUtf8(""))
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.label2 = QtGui.QLabel(System_User_Login_Dlg)
        self.label2.setGeometry(QtCore.QRect(70, 70, 61, 16))
        self.label2.setStyleSheet(_fromUtf8(""))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.label3 = QtGui.QLabel(System_User_Login_Dlg)
        self.label3.setGeometry(QtCore.QRect(70, 140, 61, 16))
        self.label3.setStyleSheet(_fromUtf8(""))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.lineEdit2 = QtGui.QLineEdit(System_User_Login_Dlg)
        self.lineEdit2.setGeometry(QtCore.QRect(140, 140, 171, 20))
        self.lineEdit2.setText(_fromUtf8(""))
        self.lineEdit2.setObjectName(_fromUtf8("lineEdit2"))
        self.btn_help = QtGui.QPushButton(System_User_Login_Dlg)
        self.btn_help.setGeometry(QtCore.QRect(240, 220, 75, 23))
        self.btn_help.setObjectName(_fromUtf8("btn_help"))

        self.retranslateUi(System_User_Login_Dlg)
        QtCore.QMetaObject.connectSlotsByName(System_User_Login_Dlg)

    def retranslateUi(self, System_User_Login_Dlg):
        System_User_Login_Dlg.setWindowTitle(_translate("System_User_Login_Dlg", "用户登录", None))
        self.btn_ok.setText(_translate("System_User_Login_Dlg", "确定", None))
        self.btn_cancel.setText(_translate("System_User_Login_Dlg", "取消", None))
        self.label2.setText(_translate("System_User_Login_Dlg", "用户名称", None))
        self.label3.setText(_translate("System_User_Login_Dlg", "密码", None))
        self.btn_help.setText(_translate("System_User_Login_Dlg", "帮助", None))

