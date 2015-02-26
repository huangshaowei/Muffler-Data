# -*- coding: utf-8 -*-

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


class Ui_BaseView(object):
    def setupUi(self,Ui_View):
        Ui_view.setObjectName(_fromUtf8(Ui_View.__name__))
        Ui_view.resize(Ui_view.width,Ui_view.height)
        Ui_view.setMinimumSize(QtCore.QSize(Ui_view.width, Ui_view.height))
        Ui_view.setMaximumSize(QtCore.QSize(Ui_view.width, Ui_view.height))
        Ui_view.setModal(False)



import resources_rc