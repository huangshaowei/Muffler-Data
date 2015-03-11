# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\freecad-8-26-all-success\Mod\Muffler\MufflerData\views\MufflerPanel_Para_2_Schemes_Add.ui'
#
# Created: Tue Mar 10 16:28:18 2015
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

class Ui_Para_Schemes_Add_Dlg(object):
    def setupUi(self, Para_Schemes_Add_Dlg):
        Para_Schemes_Add_Dlg.setObjectName(_fromUtf8("Para_Schemes_Add_Dlg"))
        Para_Schemes_Add_Dlg.resize(439, 505)
        Para_Schemes_Add_Dlg.setMinimumSize(QtCore.QSize(0, 0))
        Para_Schemes_Add_Dlg.setMaximumSize(QtCore.QSize(474, 614))
        Para_Schemes_Add_Dlg.setModal(False)
        self.btn_ok = QtGui.QPushButton(Para_Schemes_Add_Dlg)
        self.btn_ok.setGeometry(QtCore.QRect(40, 460, 75, 23))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_cancel = QtGui.QPushButton(Para_Schemes_Add_Dlg)
        self.btn_cancel.setGeometry(QtCore.QRect(160, 460, 75, 23))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.btn_help = QtGui.QPushButton(Para_Schemes_Add_Dlg)
        self.btn_help.setGeometry(QtCore.QRect(280, 460, 75, 23))
        self.btn_help.setObjectName(_fromUtf8("btn_help"))
        self.label = QtGui.QLabel(Para_Schemes_Add_Dlg)
        self.label.setGeometry(QtCore.QRect(30, 40, 61, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Para_Schemes_Add_Dlg)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 211, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Para_Schemes_Add_Dlg)
        self.pushButton.setGeometry(QtCore.QRect(340, 40, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(Para_Schemes_Add_Dlg)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Para_Schemes_Add_Dlg)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 80, 211, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(Para_Schemes_Add_Dlg)
        self.label_3.setGeometry(QtCore.QRect(33, 120, 51, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(Para_Schemes_Add_Dlg)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 120, 211, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_4 = QtGui.QLabel(Para_Schemes_Add_Dlg)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Para_Schemes_Add_Dlg)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 200, 381, 241))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))

        self.retranslateUi(Para_Schemes_Add_Dlg)
        QtCore.QMetaObject.connectSlotsByName(Para_Schemes_Add_Dlg)

    def retranslateUi(self, Para_Schemes_Add_Dlg):
        Para_Schemes_Add_Dlg.setWindowTitle(_translate("Para_Schemes_Add_Dlg", "添加项目标示信息", None))
        self.btn_ok.setText(_translate("Para_Schemes_Add_Dlg", "确定", None))
        self.btn_cancel.setText(_translate("Para_Schemes_Add_Dlg", "取消", None))
        self.btn_help.setText(_translate("Para_Schemes_Add_Dlg", "帮助", None))
        self.label.setText(_translate("Para_Schemes_Add_Dlg", "方案编号：", None))
        self.pushButton.setText(_translate("Para_Schemes_Add_Dlg", "生成", None))
        self.label_2.setText(_translate("Para_Schemes_Add_Dlg", "子方案名称：", None))
        self.label_3.setText(_translate("Para_Schemes_Add_Dlg", "项目编号：", None))
        self.label_4.setText(_translate("Para_Schemes_Add_Dlg", "备注", None))

