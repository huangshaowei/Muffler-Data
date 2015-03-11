# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\freecad-8-26-all-success\Mod\Muffler\MufflerData\views\MufflerPanel_System_1_User_Add.ui'
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

class Ui_System_User_Add_Dlg(object):
    def setupUi(self, System_User_Add_Dlg):
        System_User_Add_Dlg.setObjectName(_fromUtf8("System_User_Add_Dlg"))
        System_User_Add_Dlg.resize(315, 274)
        System_User_Add_Dlg.setMinimumSize(QtCore.QSize(315, 274))
        System_User_Add_Dlg.setMaximumSize(QtCore.QSize(315, 274))
        System_User_Add_Dlg.setModal(False)
        self.btn_ok = QtGui.QPushButton(System_User_Add_Dlg)
        self.btn_ok.setGeometry(QtCore.QRect(30, 220, 75, 23))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_cancel = QtGui.QPushButton(System_User_Add_Dlg)
        self.btn_cancel.setGeometry(QtCore.QRect(120, 220, 75, 23))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lineEdit1 = QtGui.QLineEdit(System_User_Add_Dlg)
        self.lineEdit1.setGeometry(QtCore.QRect(110, 30, 171, 20))
        self.lineEdit1.setText(_fromUtf8(""))
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.label1 = QtGui.QLabel(System_User_Add_Dlg)
        self.label1.setGeometry(QtCore.QRect(40, 30, 61, 16))
        self.label1.setStyleSheet(_fromUtf8(""))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.lineEdit2 = QtGui.QLineEdit(System_User_Add_Dlg)
        self.lineEdit2.setGeometry(QtCore.QRect(110, 70, 171, 20))
        self.lineEdit2.setText(_fromUtf8(""))
        self.lineEdit2.setObjectName(_fromUtf8("lineEdit2"))
        self.label2 = QtGui.QLabel(System_User_Add_Dlg)
        self.label2.setGeometry(QtCore.QRect(40, 70, 61, 16))
        self.label2.setStyleSheet(_fromUtf8(""))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.label3 = QtGui.QLabel(System_User_Add_Dlg)
        self.label3.setGeometry(QtCore.QRect(40, 110, 61, 16))
        self.label3.setStyleSheet(_fromUtf8(""))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.lineEdit3 = QtGui.QLineEdit(System_User_Add_Dlg)
        self.lineEdit3.setGeometry(QtCore.QRect(110, 110, 171, 20))
        self.lineEdit3.setText(_fromUtf8(""))
        self.lineEdit3.setObjectName(_fromUtf8("lineEdit3"))
        self.label4 = QtGui.QLabel(System_User_Add_Dlg)
        self.label4.setGeometry(QtCore.QRect(40, 150, 61, 16))
        self.label4.setStyleSheet(_fromUtf8(""))
        self.label4.setObjectName(_fromUtf8("label4"))
        self.btn_help = QtGui.QPushButton(System_User_Add_Dlg)
        self.btn_help.setGeometry(QtCore.QRect(210, 220, 75, 23))
        self.btn_help.setObjectName(_fromUtf8("btn_help"))
        self.comboBox = QtGui.QComboBox(System_User_Add_Dlg)
        self.comboBox.setGeometry(QtCore.QRect(110, 150, 171, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.retranslateUi(System_User_Add_Dlg)
        QtCore.QMetaObject.connectSlotsByName(System_User_Add_Dlg)

    def retranslateUi(self, System_User_Add_Dlg):
        System_User_Add_Dlg.setWindowTitle(_translate("System_User_Add_Dlg", "用户信息录入", None))
        self.btn_ok.setText(_translate("System_User_Add_Dlg", "确定", None))
        self.btn_cancel.setText(_translate("System_User_Add_Dlg", "取消", None))
        self.label1.setText(_translate("System_User_Add_Dlg", "用户编号", None))
        self.label2.setText(_translate("System_User_Add_Dlg", "用户名称", None))
        self.label3.setText(_translate("System_User_Add_Dlg", "密码", None))
        self.label4.setText(_translate("System_User_Add_Dlg", "用户级别", None))
        self.btn_help.setText(_translate("System_User_Add_Dlg", "帮助", None))
        self.comboBox.setItemText(0, _translate("System_User_Add_Dlg", "系统管理员", None))
        self.comboBox.setItemText(1, _translate("System_User_Add_Dlg", "数据维护员", None))
        self.comboBox.setItemText(2, _translate("System_User_Add_Dlg", "一般操作员", None))

