# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\freecad-8-26-all-success\Mod\Muffler\MufflerData\views\MufflerPanel_Para_8_Employee_Add.ui'
#
# Created: Fri Feb 27 10:56:46 2015
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

class Ui_Para_Employee_Add_Dlg(object):
    def setupUi(self, Para_Employee_Add_Dlg):
        Para_Employee_Add_Dlg.setObjectName(_fromUtf8("Para_Employee_Add_Dlg"))
        Para_Employee_Add_Dlg.resize(371, 341)
        Para_Employee_Add_Dlg.setMinimumSize(QtCore.QSize(371, 341))
        Para_Employee_Add_Dlg.setMaximumSize(QtCore.QSize(371, 341))
        Para_Employee_Add_Dlg.setModal(False)
        self.lineEdit1 = QtGui.QLineEdit(Para_Employee_Add_Dlg)
        self.lineEdit1.setEnabled(False)
        self.lineEdit1.setGeometry(QtCore.QRect(140, 30, 171, 20))
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.btn_ok = QtGui.QPushButton(Para_Employee_Add_Dlg)
        self.btn_ok.setGeometry(QtCore.QRect(50, 290, 75, 23))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_cancel = QtGui.QPushButton(Para_Employee_Add_Dlg)
        self.btn_cancel.setGeometry(QtCore.QRect(150, 290, 75, 23))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.label1 = QtGui.QLabel(Para_Employee_Add_Dlg)
        self.label1.setGeometry(QtCore.QRect(50, 30, 81, 16))
        self.label1.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0)"))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.lineEdit2 = QtGui.QLineEdit(Para_Employee_Add_Dlg)
        self.lineEdit2.setGeometry(QtCore.QRect(140, 70, 171, 20))
        self.lineEdit2.setObjectName(_fromUtf8("lineEdit2"))
        self.label2 = QtGui.QLabel(Para_Employee_Add_Dlg)
        self.label2.setGeometry(QtCore.QRect(50, 70, 81, 16))
        self.label2.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0)"))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.lineEdit3 = QtGui.QLineEdit(Para_Employee_Add_Dlg)
        self.lineEdit3.setGeometry(QtCore.QRect(140, 110, 171, 20))
        self.lineEdit3.setText(_fromUtf8(""))
        self.lineEdit3.setObjectName(_fromUtf8("lineEdit3"))
        self.label3 = QtGui.QLabel(Para_Employee_Add_Dlg)
        self.label3.setGeometry(QtCore.QRect(50, 110, 81, 16))
        self.label3.setStyleSheet(_fromUtf8(""))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.lineEdit4 = QtGui.QLineEdit(Para_Employee_Add_Dlg)
        self.lineEdit4.setGeometry(QtCore.QRect(140, 150, 171, 20))
        self.lineEdit4.setText(_fromUtf8(""))
        self.lineEdit4.setObjectName(_fromUtf8("lineEdit4"))
        self.label4 = QtGui.QLabel(Para_Employee_Add_Dlg)
        self.label4.setGeometry(QtCore.QRect(50, 150, 81, 16))
        self.label4.setStyleSheet(_fromUtf8(""))
        self.label4.setObjectName(_fromUtf8("label4"))
        self.label5 = QtGui.QLabel(Para_Employee_Add_Dlg)
        self.label5.setGeometry(QtCore.QRect(50, 190, 81, 16))
        self.label5.setStyleSheet(_fromUtf8(""))
        self.label5.setObjectName(_fromUtf8("label5"))
        self.lineEdit5 = QtGui.QLineEdit(Para_Employee_Add_Dlg)
        self.lineEdit5.setGeometry(QtCore.QRect(140, 190, 171, 20))
        self.lineEdit5.setText(_fromUtf8(""))
        self.lineEdit5.setObjectName(_fromUtf8("lineEdit5"))
        self.label6 = QtGui.QLabel(Para_Employee_Add_Dlg)
        self.label6.setGeometry(QtCore.QRect(50, 230, 81, 16))
        self.label6.setStyleSheet(_fromUtf8(""))
        self.label6.setObjectName(_fromUtf8("label6"))
        self.lineEdit6 = QtGui.QLineEdit(Para_Employee_Add_Dlg)
        self.lineEdit6.setGeometry(QtCore.QRect(140, 230, 171, 20))
        self.lineEdit6.setText(_fromUtf8(""))
        self.lineEdit6.setObjectName(_fromUtf8("lineEdit6"))
        self.btn_help = QtGui.QPushButton(Para_Employee_Add_Dlg)
        self.btn_help.setGeometry(QtCore.QRect(250, 290, 75, 23))
        self.btn_help.setObjectName(_fromUtf8("btn_help"))

        self.retranslateUi(Para_Employee_Add_Dlg)
        QtCore.QMetaObject.connectSlotsByName(Para_Employee_Add_Dlg)

    def retranslateUi(self, Para_Employee_Add_Dlg):
        Para_Employee_Add_Dlg.setWindowTitle(_translate("Para_Employee_Add_Dlg", "添加员工信息", None))
        self.btn_ok.setText(_translate("Para_Employee_Add_Dlg", "确定", None))
        self.btn_cancel.setText(_translate("Para_Employee_Add_Dlg", "取消", None))
        self.label1.setText(_translate("Para_Employee_Add_Dlg", "员工编号*", None))
        self.label2.setText(_translate("Para_Employee_Add_Dlg", "员工姓名*", None))
        self.label3.setText(_translate("Para_Employee_Add_Dlg", "员工部门", None))
        self.label4.setText(_translate("Para_Employee_Add_Dlg", "员工职务", None))
        self.label5.setText(_translate("Para_Employee_Add_Dlg", "员工联系方式", None))
        self.label6.setText(_translate("Para_Employee_Add_Dlg", "员工电子邮箱", None))
        self.btn_help.setText(_translate("Para_Employee_Add_Dlg", "帮助", None))

