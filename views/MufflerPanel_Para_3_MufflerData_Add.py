# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\freecad-8-26-all-success\Mod\Muffler\MufflerData\views\MufflerPanel_Para_3_MufflerData_Add.ui'
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

class Ui_Para_MufflerData_Add_Dlg(object):
    def setupUi(self, Para_MufflerData_Add_Dlg):
        Para_MufflerData_Add_Dlg.setObjectName(_fromUtf8("Para_MufflerData_Add_Dlg"))
        Para_MufflerData_Add_Dlg.resize(315, 528)
        Para_MufflerData_Add_Dlg.setMinimumSize(QtCore.QSize(0, 528))
        Para_MufflerData_Add_Dlg.setMaximumSize(QtCore.QSize(982, 528))
        Para_MufflerData_Add_Dlg.setModal(False)
        self.btn_ok = QtGui.QPushButton(Para_MufflerData_Add_Dlg)
        self.btn_ok.setGeometry(QtCore.QRect(10, 490, 75, 23))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_cancel = QtGui.QPushButton(Para_MufflerData_Add_Dlg)
        self.btn_cancel.setGeometry(QtCore.QRect(110, 490, 75, 23))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.btn_help = QtGui.QPushButton(Para_MufflerData_Add_Dlg)
        self.btn_help.setGeometry(QtCore.QRect(200, 490, 75, 23))
        self.btn_help.setObjectName(_fromUtf8("btn_help"))
        self.groupBox6 = QtGui.QGroupBox(Para_MufflerData_Add_Dlg)
        self.groupBox6.setGeometry(QtCore.QRect(10, 10, 291, 461))
        self.groupBox6.setObjectName(_fromUtf8("groupBox6"))
        self.box6_label1 = QtGui.QLabel(self.groupBox6)
        self.box6_label1.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.box6_label1.setStyleSheet(_fromUtf8(""))
        self.box6_label1.setObjectName(_fromUtf8("box6_label1"))
        self.box6_btn_import = QtGui.QPushButton(self.groupBox6)
        self.box6_btn_import.setGeometry(QtCore.QRect(220, 20, 61, 23))
        self.box6_btn_import.setObjectName(_fromUtf8("box6_btn_import"))
        self.box6_label2 = QtGui.QLabel(self.groupBox6)
        self.box6_label2.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.box6_label2.setStyleSheet(_fromUtf8(""))
        self.box6_label2.setObjectName(_fromUtf8("box6_label2"))
        self.box6_progressBar = QtGui.QProgressBar(self.groupBox6)
        self.box6_progressBar.setGeometry(QtCore.QRect(10, 50, 271, 20))
        self.box6_progressBar.setProperty("value", 0)
        self.box6_progressBar.setObjectName(_fromUtf8("box6_progressBar"))
        self.box6_tableWidget1 = QtGui.QTableWidget(self.groupBox6)
        self.box6_tableWidget1.setGeometry(QtCore.QRect(10, 100, 271, 161))
        self.box6_tableWidget1.setObjectName(_fromUtf8("box6_tableWidget1"))
        self.box6_tableWidget1.setColumnCount(2)
        self.box6_tableWidget1.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.box6_tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.box6_tableWidget1.setHorizontalHeaderItem(1, item)
        self.box6_tableWidget2 = QtGui.QTableWidget(self.groupBox6)
        self.box6_tableWidget2.setGeometry(QtCore.QRect(10, 290, 271, 161))
        self.box6_tableWidget2.setObjectName(_fromUtf8("box6_tableWidget2"))
        self.box6_tableWidget2.setColumnCount(2)
        self.box6_tableWidget2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.box6_tableWidget2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.box6_tableWidget2.setHorizontalHeaderItem(1, item)
        self.box6_label3 = QtGui.QLabel(self.groupBox6)
        self.box6_label3.setGeometry(QtCore.QRect(10, 270, 121, 16))
        self.box6_label3.setStyleSheet(_fromUtf8(""))
        self.box6_label3.setObjectName(_fromUtf8("box6_label3"))
        self.comboBox_4 = QtGui.QComboBox(self.groupBox6)
        self.comboBox_4.setGeometry(QtCore.QRect(80, 20, 111, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))

        self.retranslateUi(Para_MufflerData_Add_Dlg)
        QtCore.QMetaObject.connectSlotsByName(Para_MufflerData_Add_Dlg)
        Para_MufflerData_Add_Dlg.setTabOrder(self.btn_ok, self.btn_cancel)
        Para_MufflerData_Add_Dlg.setTabOrder(self.btn_cancel, self.btn_help)

    def retranslateUi(self, Para_MufflerData_Add_Dlg):
        Para_MufflerData_Add_Dlg.setWindowTitle(_translate("Para_MufflerData_Add_Dlg", "消声器信息录入", None))
        self.btn_ok.setText(_translate("Para_MufflerData_Add_Dlg", "确定", None))
        self.btn_cancel.setText(_translate("Para_MufflerData_Add_Dlg", "取消", None))
        self.btn_help.setText(_translate("Para_MufflerData_Add_Dlg", "帮助", None))
        self.groupBox6.setTitle(_translate("Para_MufflerData_Add_Dlg", "传递损失数据", None))
        self.box6_label1.setText(_translate("Para_MufflerData_Add_Dlg", "频率范围：", None))
        self.box6_btn_import.setText(_translate("Para_MufflerData_Add_Dlg", "导入", None))
        self.box6_label2.setText(_translate("Para_MufflerData_Add_Dlg", "导入数据显示(1000)：", None))
        item = self.box6_tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("Para_MufflerData_Add_Dlg", "New Column", None))
        item = self.box6_tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("Para_MufflerData_Add_Dlg", "New Column", None))
        item = self.box6_tableWidget2.horizontalHeaderItem(0)
        item.setText(_translate("Para_MufflerData_Add_Dlg", "New Column", None))
        item = self.box6_tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("Para_MufflerData_Add_Dlg", "New Column", None))
        self.box6_label3.setText(_translate("Para_MufflerData_Add_Dlg", "导入数据显示(3000)：", None))
        self.comboBox_4.setToolTip(_translate("Para_MufflerData_Add_Dlg", "notfield", None))
        self.comboBox_4.setItemText(0, _translate("Para_MufflerData_Add_Dlg", "1000", None))
        self.comboBox_4.setItemText(1, _translate("Para_MufflerData_Add_Dlg", "3000", None))

