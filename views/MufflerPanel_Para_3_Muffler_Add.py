# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\freecad-8-26-all-success\Mod\Database\MufflerData\views\MufflerPanel_Para_3_Muffler_Add.ui'
#
# Created: Wed Feb 25 11:23:34 2015
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

class Ui_Para_Muffler_Add_Dlg(object):
    def setupUi(self, Para_Muffler_Add_Dlg):
        Para_Muffler_Add_Dlg.setObjectName(_fromUtf8("Para_Muffler_Add_Dlg"))
        Para_Muffler_Add_Dlg.resize(982, 528)
        Para_Muffler_Add_Dlg.setMinimumSize(QtCore.QSize(982, 528))
        Para_Muffler_Add_Dlg.setMaximumSize(QtCore.QSize(982, 528))
        Para_Muffler_Add_Dlg.setModal(False)
        self.btn_ok = QtGui.QPushButton(Para_Muffler_Add_Dlg)
        self.btn_ok.setGeometry(QtCore.QRect(710, 490, 75, 23))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.btn_cancel = QtGui.QPushButton(Para_Muffler_Add_Dlg)
        self.btn_cancel.setGeometry(QtCore.QRect(800, 490, 75, 23))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.groupBox1 = QtGui.QGroupBox(Para_Muffler_Add_Dlg)
        self.groupBox1.setGeometry(QtCore.QRect(10, 10, 241, 201))
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.box1_label1 = QtGui.QLabel(self.groupBox1)
        self.box1_label1.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.box1_label1.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0)"))
        self.box1_label1.setObjectName(_fromUtf8("box1_label1"))
        self.box1_lineEdit1 = QtGui.QLineEdit(self.groupBox1)
        self.box1_lineEdit1.setEnabled(False)
        self.box1_lineEdit1.setGeometry(QtCore.QRect(100, 20, 131, 20))
        self.box1_lineEdit1.setText(_fromUtf8(""))
        self.box1_lineEdit1.setObjectName(_fromUtf8("box1_lineEdit1"))
        self.box1_label2 = QtGui.QLabel(self.groupBox1)
        self.box1_label2.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.box1_label2.setStyleSheet(_fromUtf8(""))
        self.box1_label2.setObjectName(_fromUtf8("box1_label2"))
        self.box1_label3 = QtGui.QLabel(self.groupBox1)
        self.box1_label3.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.box1_label3.setStyleSheet(_fromUtf8(""))
        self.box1_label3.setObjectName(_fromUtf8("box1_label3"))
        self.box1_label4 = QtGui.QLabel(self.groupBox1)
        self.box1_label4.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.box1_label4.setStyleSheet(_fromUtf8(""))
        self.box1_label4.setObjectName(_fromUtf8("box1_label4"))
        self.box1_label5 = QtGui.QLabel(self.groupBox1)
        self.box1_label5.setGeometry(QtCore.QRect(10, 140, 81, 16))
        self.box1_label5.setStyleSheet(_fromUtf8(""))
        self.box1_label5.setObjectName(_fromUtf8("box1_label5"))
        self.box1_label6 = QtGui.QLabel(self.groupBox1)
        self.box1_label6.setGeometry(QtCore.QRect(10, 170, 81, 16))
        self.box1_label6.setStyleSheet(_fromUtf8(""))
        self.box1_label6.setObjectName(_fromUtf8("box1_label6"))
        self.box1_lineEdit2 = QtGui.QLineEdit(self.groupBox1)
        self.box1_lineEdit2.setGeometry(QtCore.QRect(100, 110, 131, 20))
        self.box1_lineEdit2.setText(_fromUtf8(""))
        self.box1_lineEdit2.setObjectName(_fromUtf8("box1_lineEdit2"))
        self.box1_lineEdit3 = QtGui.QLineEdit(self.groupBox1)
        self.box1_lineEdit3.setGeometry(QtCore.QRect(100, 140, 131, 20))
        self.box1_lineEdit3.setText(_fromUtf8(""))
        self.box1_lineEdit3.setObjectName(_fromUtf8("box1_lineEdit3"))
        self.box1_combo3 = QtGui.QComboBox(self.groupBox1)
        self.box1_combo3.setGeometry(QtCore.QRect(100, 170, 131, 22))
        self.box1_combo3.setEditable(True)
        self.box1_combo3.setObjectName(_fromUtf8("box1_combo3"))
        self.box1_combo3.addItem(_fromUtf8(""))
        self.box1_combo3.addItem(_fromUtf8(""))
        self.box1_combo3.addItem(_fromUtf8(""))
        self.box1_combo3.addItem(_fromUtf8(""))
        self.box1_combo3.addItem(_fromUtf8(""))
        self.box1_combo3.addItem(_fromUtf8(""))
        self.box1_combo3.addItem(_fromUtf8(""))
        self.box1_combo2 = QtGui.QComboBox(self.groupBox1)
        self.box1_combo2.setGeometry(QtCore.QRect(100, 80, 131, 22))
        self.box1_combo2.setEditable(True)
        self.box1_combo2.setObjectName(_fromUtf8("box1_combo2"))
        self.box1_combo2.addItem(_fromUtf8(""))
        self.box1_combo2.addItem(_fromUtf8(""))
        self.box1_combo2.addItem(_fromUtf8(""))
        self.box1_combo1 = QtGui.QComboBox(self.groupBox1)
        self.box1_combo1.setGeometry(QtCore.QRect(100, 50, 131, 22))
        self.box1_combo1.setEditable(True)
        self.box1_combo1.setObjectName(_fromUtf8("box1_combo1"))
        self.box1_combo1.addItem(_fromUtf8(""))
        self.box1_combo1.addItem(_fromUtf8(""))
        self.box1_combo1.addItem(_fromUtf8(""))
        self.box1_combo1.addItem(_fromUtf8(""))
        self.box1_combo1.addItem(_fromUtf8(""))
        self.box1_combo1.addItem(_fromUtf8(""))
        self.groupBox2 = QtGui.QGroupBox(Para_Muffler_Add_Dlg)
        self.groupBox2.setGeometry(QtCore.QRect(10, 220, 241, 171))
        self.groupBox2.setObjectName(_fromUtf8("groupBox2"))
        self.box2_lineEdit_left1 = QtGui.QLineEdit(self.groupBox2)
        self.box2_lineEdit_left1.setGeometry(QtCore.QRect(10, 20, 101, 20))
        self.box2_lineEdit_left1.setText(_fromUtf8(""))
        self.box2_lineEdit_left1.setObjectName(_fromUtf8("box2_lineEdit_left1"))
        self.box2_lineEdit_right1 = QtGui.QLineEdit(self.groupBox2)
        self.box2_lineEdit_right1.setGeometry(QtCore.QRect(120, 20, 111, 20))
        self.box2_lineEdit_right1.setText(_fromUtf8(""))
        self.box2_lineEdit_right1.setObjectName(_fromUtf8("box2_lineEdit_right1"))
        self.box2_lineEdit_right2 = QtGui.QLineEdit(self.groupBox2)
        self.box2_lineEdit_right2.setGeometry(QtCore.QRect(120, 50, 111, 21))
        self.box2_lineEdit_right2.setText(_fromUtf8(""))
        self.box2_lineEdit_right2.setObjectName(_fromUtf8("box2_lineEdit_right2"))
        self.box2_lineEdit_left2 = QtGui.QLineEdit(self.groupBox2)
        self.box2_lineEdit_left2.setGeometry(QtCore.QRect(10, 50, 101, 20))
        self.box2_lineEdit_left2.setText(_fromUtf8(""))
        self.box2_lineEdit_left2.setObjectName(_fromUtf8("box2_lineEdit_left2"))
        self.box2_lineEdit_left4 = QtGui.QLineEdit(self.groupBox2)
        self.box2_lineEdit_left4.setGeometry(QtCore.QRect(10, 110, 101, 20))
        self.box2_lineEdit_left4.setText(_fromUtf8(""))
        self.box2_lineEdit_left4.setObjectName(_fromUtf8("box2_lineEdit_left4"))
        self.box2_lineEdit_left3 = QtGui.QLineEdit(self.groupBox2)
        self.box2_lineEdit_left3.setGeometry(QtCore.QRect(10, 80, 101, 20))
        self.box2_lineEdit_left3.setText(_fromUtf8(""))
        self.box2_lineEdit_left3.setObjectName(_fromUtf8("box2_lineEdit_left3"))
        self.box2_lineEdit_left5 = QtGui.QLineEdit(self.groupBox2)
        self.box2_lineEdit_left5.setGeometry(QtCore.QRect(10, 140, 101, 20))
        self.box2_lineEdit_left5.setText(_fromUtf8(""))
        self.box2_lineEdit_left5.setObjectName(_fromUtf8("box2_lineEdit_left5"))
        self.box2_lineEdit_right4 = QtGui.QLineEdit(self.groupBox2)
        self.box2_lineEdit_right4.setGeometry(QtCore.QRect(120, 110, 111, 20))
        self.box2_lineEdit_right4.setText(_fromUtf8(""))
        self.box2_lineEdit_right4.setObjectName(_fromUtf8("box2_lineEdit_right4"))
        self.box2_lineEdit_right5 = QtGui.QLineEdit(self.groupBox2)
        self.box2_lineEdit_right5.setGeometry(QtCore.QRect(120, 140, 111, 20))
        self.box2_lineEdit_right5.setText(_fromUtf8(""))
        self.box2_lineEdit_right5.setObjectName(_fromUtf8("box2_lineEdit_right5"))
        self.box2_lineEdit_right3 = QtGui.QLineEdit(self.groupBox2)
        self.box2_lineEdit_right3.setGeometry(QtCore.QRect(120, 80, 111, 20))
        self.box2_lineEdit_right3.setText(_fromUtf8(""))
        self.box2_lineEdit_right3.setObjectName(_fromUtf8("box2_lineEdit_right3"))
        self.groupBox4 = QtGui.QGroupBox(Para_Muffler_Add_Dlg)
        self.groupBox4.setGeometry(QtCore.QRect(260, 10, 421, 381))
        self.groupBox4.setObjectName(_fromUtf8("groupBox4"))
        self.box4_label1 = QtGui.QLabel(self.groupBox4)
        self.box4_label1.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.box4_label1.setStyleSheet(_fromUtf8(""))
        self.box4_label1.setObjectName(_fromUtf8("box4_label1"))
        self.box4_label2 = QtGui.QLabel(self.groupBox4)
        self.box4_label2.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.box4_label2.setStyleSheet(_fromUtf8(""))
        self.box4_label2.setObjectName(_fromUtf8("box4_label2"))
        self.box4_label3 = QtGui.QLabel(self.groupBox4)
        self.box4_label3.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.box4_label3.setStyleSheet(_fromUtf8(""))
        self.box4_label3.setObjectName(_fromUtf8("box4_label3"))
        self.box4_label4 = QtGui.QLabel(self.groupBox4)
        self.box4_label4.setGeometry(QtCore.QRect(10, 180, 81, 16))
        self.box4_label4.setStyleSheet(_fromUtf8(""))
        self.box4_label4.setObjectName(_fromUtf8("box4_label4"))
        self.box4_label5 = QtGui.QLabel(self.groupBox4)
        self.box4_label5.setGeometry(QtCore.QRect(10, 230, 81, 16))
        self.box4_label5.setStyleSheet(_fromUtf8(""))
        self.box4_label5.setObjectName(_fromUtf8("box4_label5"))
        self.box4_label6 = QtGui.QLabel(self.groupBox4)
        self.box4_label6.setGeometry(QtCore.QRect(10, 280, 131, 16))
        self.box4_label6.setStyleSheet(_fromUtf8(""))
        self.box4_label6.setObjectName(_fromUtf8("box4_label6"))
        self.box4_label7 = QtGui.QLabel(self.groupBox4)
        self.box4_label7.setGeometry(QtCore.QRect(10, 340, 131, 16))
        self.box4_label7.setStyleSheet(_fromUtf8(""))
        self.box4_label7.setObjectName(_fromUtf8("box4_label7"))
        self.box4_btn1 = QtGui.QPushButton(self.groupBox4)
        self.box4_btn1.setGeometry(QtCore.QRect(350, 30, 61, 23))
        self.box4_btn1.setObjectName(_fromUtf8("box4_btn1"))
        self.box4_btn2 = QtGui.QPushButton(self.groupBox4)
        self.box4_btn2.setGeometry(QtCore.QRect(350, 80, 61, 23))
        self.box4_btn2.setObjectName(_fromUtf8("box4_btn2"))
        self.box4_btn3 = QtGui.QPushButton(self.groupBox4)
        self.box4_btn3.setGeometry(QtCore.QRect(350, 130, 61, 23))
        self.box4_btn3.setObjectName(_fromUtf8("box4_btn3"))
        self.box4_btn4 = QtGui.QPushButton(self.groupBox4)
        self.box4_btn4.setGeometry(QtCore.QRect(350, 180, 61, 23))
        self.box4_btn4.setObjectName(_fromUtf8("box4_btn4"))
        self.box4_btn5 = QtGui.QPushButton(self.groupBox4)
        self.box4_btn5.setGeometry(QtCore.QRect(350, 230, 61, 23))
        self.box4_btn5.setObjectName(_fromUtf8("box4_btn5"))
        self.box4_btn6 = QtGui.QPushButton(self.groupBox4)
        self.box4_btn6.setGeometry(QtCore.QRect(350, 280, 61, 23))
        self.box4_btn6.setObjectName(_fromUtf8("box4_btn6"))
        self.box4_btn7 = QtGui.QPushButton(self.groupBox4)
        self.box4_btn7.setGeometry(QtCore.QRect(350, 340, 61, 23))
        self.box4_btn7.setObjectName(_fromUtf8("box4_btn7"))
        self.label1 = QtGui.QLabel(self.groupBox4)
        self.label1.setGeometry(QtCore.QRect(150, 20, 191, 31))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.label2 = QtGui.QLabel(self.groupBox4)
        self.label2.setGeometry(QtCore.QRect(150, 70, 191, 31))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.label3 = QtGui.QLabel(self.groupBox4)
        self.label3.setGeometry(QtCore.QRect(150, 120, 191, 31))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.label4 = QtGui.QLabel(self.groupBox4)
        self.label4.setGeometry(QtCore.QRect(150, 170, 191, 31))
        self.label4.setObjectName(_fromUtf8("label4"))
        self.label5 = QtGui.QLabel(self.groupBox4)
        self.label5.setGeometry(QtCore.QRect(150, 220, 191, 31))
        self.label5.setObjectName(_fromUtf8("label5"))
        self.label6 = QtGui.QLabel(self.groupBox4)
        self.label6.setGeometry(QtCore.QRect(150, 270, 191, 31))
        self.label6.setObjectName(_fromUtf8("label6"))
        self.label7 = QtGui.QLabel(self.groupBox4)
        self.label7.setGeometry(QtCore.QRect(150, 330, 191, 31))
        self.label7.setObjectName(_fromUtf8("label7"))
        self.groupBox3 = QtGui.QGroupBox(Para_Muffler_Add_Dlg)
        self.groupBox3.setGeometry(QtCore.QRect(10, 400, 241, 121))
        self.groupBox3.setObjectName(_fromUtf8("groupBox3"))
        self.box3_plainTextEdit = QtGui.QPlainTextEdit(self.groupBox3)
        self.box3_plainTextEdit.setGeometry(QtCore.QRect(10, 20, 221, 91))
        self.box3_plainTextEdit.setObjectName(_fromUtf8("box3_plainTextEdit"))
        self.groupBox6 = QtGui.QGroupBox(Para_Muffler_Add_Dlg)
        self.groupBox6.setGeometry(QtCore.QRect(690, 10, 291, 461))
        self.groupBox6.setObjectName(_fromUtf8("groupBox6"))
        self.box6_label1 = QtGui.QLabel(self.groupBox6)
        self.box6_label1.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.box6_label1.setStyleSheet(_fromUtf8(""))
        self.box6_label1.setObjectName(_fromUtf8("box6_label1"))
        self.box6_comboBox = QtGui.QComboBox(self.groupBox6)
        self.box6_comboBox.setGeometry(QtCore.QRect(90, 20, 111, 22))
        self.box6_comboBox.setEditable(True)
        self.box6_comboBox.setObjectName(_fromUtf8("box6_comboBox"))
        self.box6_comboBox.addItem(_fromUtf8(""))
        self.box6_comboBox.addItem(_fromUtf8(""))
        self.box6_btn_import = QtGui.QPushButton(self.groupBox6)
        self.box6_btn_import.setGeometry(QtCore.QRect(220, 20, 61, 23))
        self.box6_btn_import.setObjectName(_fromUtf8("box6_btn_import"))
        self.box6_label2 = QtGui.QLabel(self.groupBox6)
        self.box6_label2.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.box6_label2.setStyleSheet(_fromUtf8(""))
        self.box6_label2.setObjectName(_fromUtf8("box6_label2"))
        self.box6_progressBar = QtGui.QProgressBar(self.groupBox6)
        self.box6_progressBar.setGeometry(QtCore.QRect(10, 50, 271, 20))
        self.box6_progressBar.setProperty("value", 24)
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
        self.groupBox5 = QtGui.QGroupBox(Para_Muffler_Add_Dlg)
        self.groupBox5.setGeometry(QtCore.QRect(260, 400, 421, 121))
        self.groupBox5.setObjectName(_fromUtf8("groupBox5"))
        self.box5_label1 = QtGui.QLabel(self.groupBox5)
        self.box5_label1.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.box5_label1.setStyleSheet(_fromUtf8(""))
        self.box5_label1.setObjectName(_fromUtf8("box5_label1"))
        self.box5_lineEdit1 = QtGui.QLineEdit(self.groupBox5)
        self.box5_lineEdit1.setGeometry(QtCore.QRect(100, 30, 241, 20))
        self.box5_lineEdit1.setText(_fromUtf8(""))
        self.box5_lineEdit1.setObjectName(_fromUtf8("box5_lineEdit1"))
        self.box5_btn1 = QtGui.QPushButton(self.groupBox5)
        self.box5_btn1.setGeometry(QtCore.QRect(350, 30, 61, 23))
        self.box5_btn1.setObjectName(_fromUtf8("box5_btn1"))
        self.box5_btn2 = QtGui.QPushButton(self.groupBox5)
        self.box5_btn2.setGeometry(QtCore.QRect(350, 60, 61, 23))
        self.box5_btn2.setObjectName(_fromUtf8("box5_btn2"))
        self.box5_label2 = QtGui.QLabel(self.groupBox5)
        self.box5_label2.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.box5_label2.setStyleSheet(_fromUtf8(""))
        self.box5_label2.setObjectName(_fromUtf8("box5_label2"))
        self.box5_lineEdit2 = QtGui.QLineEdit(self.groupBox5)
        self.box5_lineEdit2.setGeometry(QtCore.QRect(100, 60, 241, 20))
        self.box5_lineEdit2.setText(_fromUtf8(""))
        self.box5_lineEdit2.setObjectName(_fromUtf8("box5_lineEdit2"))
        self.box5_btn3 = QtGui.QPushButton(self.groupBox5)
        self.box5_btn3.setGeometry(QtCore.QRect(350, 90, 61, 23))
        self.box5_btn3.setObjectName(_fromUtf8("box5_btn3"))
        self.box5_label3 = QtGui.QLabel(self.groupBox5)
        self.box5_label3.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.box5_label3.setStyleSheet(_fromUtf8(""))
        self.box5_label3.setObjectName(_fromUtf8("box5_label3"))
        self.box5_lineEdit3 = QtGui.QLineEdit(self.groupBox5)
        self.box5_lineEdit3.setGeometry(QtCore.QRect(100, 90, 241, 20))
        self.box5_lineEdit3.setText(_fromUtf8(""))
        self.box5_lineEdit3.setObjectName(_fromUtf8("box5_lineEdit3"))
        self.btn_help = QtGui.QPushButton(Para_Muffler_Add_Dlg)
        self.btn_help.setGeometry(QtCore.QRect(890, 490, 75, 23))
        self.btn_help.setObjectName(_fromUtf8("btn_help"))

        self.retranslateUi(Para_Muffler_Add_Dlg)
        self.box1_combo3.setCurrentIndex(-1)
        self.box1_combo2.setCurrentIndex(-1)
        self.box1_combo1.setCurrentIndex(-1)
        self.box6_comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Para_Muffler_Add_Dlg)

    def retranslateUi(self, Para_Muffler_Add_Dlg):
        Para_Muffler_Add_Dlg.setWindowTitle(_translate("Para_Muffler_Add_Dlg", "消声器信息录入", None))
        self.btn_ok.setText(_translate("Para_Muffler_Add_Dlg", "确定", None))
        self.btn_cancel.setText(_translate("Para_Muffler_Add_Dlg", "取消", None))
        self.groupBox1.setTitle(_translate("Para_Muffler_Add_Dlg", "结构信息", None))
        self.box1_label1.setText(_translate("Para_Muffler_Add_Dlg", "消声器编号*", None))
        self.box1_label2.setText(_translate("Para_Muffler_Add_Dlg", "腔的数量(个)", None))
        self.box1_label3.setText(_translate("Para_Muffler_Add_Dlg", "消声器类型", None))
        self.box1_label4.setText(_translate("Para_Muffler_Add_Dlg", "消声器溶剂/L", None))
        self.box1_label5.setText(_translate("Para_Muffler_Add_Dlg", "截面面积/mm2", None))
        self.box1_label6.setText(_translate("Para_Muffler_Add_Dlg", "截面形状", None))
        self.box1_combo3.setItemText(0, _translate("Para_Muffler_Add_Dlg", "圆形", None))
        self.box1_combo3.setItemText(1, _translate("Para_Muffler_Add_Dlg", "椭圆形", None))
        self.box1_combo3.setItemText(2, _translate("Para_Muffler_Add_Dlg", "类跑道形", None))
        self.box1_combo3.setItemText(3, _translate("Para_Muffler_Add_Dlg", "圆角矩形", None))
        self.box1_combo3.setItemText(4, _translate("Para_Muffler_Add_Dlg", "圆角三角形", None))
        self.box1_combo3.setItemText(5, _translate("Para_Muffler_Add_Dlg", "圆角梯形", None))
        self.box1_combo3.setItemText(6, _translate("Para_Muffler_Add_Dlg", "其他形状", None))
        self.box1_combo2.setItemText(0, _translate("Para_Muffler_Add_Dlg", "混合消声器", None))
        self.box1_combo2.setItemText(1, _translate("Para_Muffler_Add_Dlg", "阻性消声器", None))
        self.box1_combo2.setItemText(2, _translate("Para_Muffler_Add_Dlg", "抗性消声器", None))
        self.box1_combo1.setItemText(0, _translate("Para_Muffler_Add_Dlg", "1", None))
        self.box1_combo1.setItemText(1, _translate("Para_Muffler_Add_Dlg", "2", None))
        self.box1_combo1.setItemText(2, _translate("Para_Muffler_Add_Dlg", "3", None))
        self.box1_combo1.setItemText(3, _translate("Para_Muffler_Add_Dlg", "4", None))
        self.box1_combo1.setItemText(4, _translate("Para_Muffler_Add_Dlg", "5", None))
        self.box1_combo1.setItemText(5, _translate("Para_Muffler_Add_Dlg", "6", None))
        self.groupBox2.setTitle(_translate("Para_Muffler_Add_Dlg", "尺寸信息", None))
        self.groupBox4.setTitle(_translate("Para_Muffler_Add_Dlg", "图片信息", None))
        self.box4_label1.setText(_translate("Para_Muffler_Add_Dlg", "尺寸标注图", None))
        self.box4_label2.setText(_translate("Para_Muffler_Add_Dlg", "实体图1", None))
        self.box4_label3.setText(_translate("Para_Muffler_Add_Dlg", "实体图2", None))
        self.box4_label4.setText(_translate("Para_Muffler_Add_Dlg", "GT图1", None))
        self.box4_label5.setText(_translate("Para_Muffler_Add_Dlg", "GT图2", None))
        self.box4_label6.setText(_translate("Para_Muffler_Add_Dlg", "传递损失实验测试图片1", None))
        self.box4_label7.setText(_translate("Para_Muffler_Add_Dlg", "传递损失实验测试图片2", None))
        self.box4_btn1.setText(_translate("Para_Muffler_Add_Dlg", "浏览", None))
        self.box4_btn2.setText(_translate("Para_Muffler_Add_Dlg", "浏览", None))
        self.box4_btn3.setText(_translate("Para_Muffler_Add_Dlg", "浏览", None))
        self.box4_btn4.setText(_translate("Para_Muffler_Add_Dlg", "浏览", None))
        self.box4_btn5.setText(_translate("Para_Muffler_Add_Dlg", "浏览", None))
        self.box4_btn6.setText(_translate("Para_Muffler_Add_Dlg", "浏览", None))
        self.box4_btn7.setText(_translate("Para_Muffler_Add_Dlg", "浏览", None))
        self.label1.setText(_translate("Para_Muffler_Add_Dlg", "TextLabel", None))
        self.label2.setText(_translate("Para_Muffler_Add_Dlg", "TextLabel", None))
        self.label3.setText(_translate("Para_Muffler_Add_Dlg", "TextLabel", None))
        self.label4.setText(_translate("Para_Muffler_Add_Dlg", "TextLabel", None))
        self.label5.setText(_translate("Para_Muffler_Add_Dlg", "TextLabel", None))
        self.label6.setText(_translate("Para_Muffler_Add_Dlg", "TextLabel", None))
        self.label7.setText(_translate("Para_Muffler_Add_Dlg", "TextLabel", None))
        self.groupBox3.setTitle(_translate("Para_Muffler_Add_Dlg", "备注", None))
        self.groupBox6.setTitle(_translate("Para_Muffler_Add_Dlg", "传递损失数据", None))
        self.box6_label1.setText(_translate("Para_Muffler_Add_Dlg", "频率范围：", None))
        self.box6_comboBox.setItemText(0, _translate("Para_Muffler_Add_Dlg", "1000", None))
        self.box6_comboBox.setItemText(1, _translate("Para_Muffler_Add_Dlg", "3000", None))
        self.box6_btn_import.setText(_translate("Para_Muffler_Add_Dlg", "导入", None))
        self.box6_label2.setText(_translate("Para_Muffler_Add_Dlg", "导入数据显示(1000)：", None))
        item = self.box6_tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("Para_Muffler_Add_Dlg", "New Column", None))
        item = self.box6_tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("Para_Muffler_Add_Dlg", "New Column", None))
        item = self.box6_tableWidget2.horizontalHeaderItem(0)
        item.setText(_translate("Para_Muffler_Add_Dlg", "New Column", None))
        item = self.box6_tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("Para_Muffler_Add_Dlg", "New Column", None))
        self.box6_label3.setText(_translate("Para_Muffler_Add_Dlg", "导入数据显示(1000)：", None))
        self.groupBox5.setTitle(_translate("Para_Muffler_Add_Dlg", "几何模型", None))
        self.box5_label1.setText(_translate("Para_Muffler_Add_Dlg", "CAD图", None))
        self.box5_btn1.setText(_translate("Para_Muffler_Add_Dlg", "浏览", None))
        self.box5_btn2.setText(_translate("Para_Muffler_Add_Dlg", "浏览", None))
        self.box5_label2.setText(_translate("Para_Muffler_Add_Dlg", "三维GT数模", None))
        self.box5_btn3.setText(_translate("Para_Muffler_Add_Dlg", "浏览", None))
        self.box5_label3.setText(_translate("Para_Muffler_Add_Dlg", "三维UG数模", None))
        self.btn_help.setText(_translate("Para_Muffler_Add_Dlg", "帮助", None))
