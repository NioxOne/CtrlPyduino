# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIPyduino.ui'
#
# Created: Tue Dec  9 16:58:10 2014
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_CtrlPyduino(object):
    def setupUi(self, CtrlPyduino):
        CtrlPyduino.setObjectName(_fromUtf8("CtrlPyduino"))
        CtrlPyduino.resize(617, 413)
        self.centralwidget = QtGui.QWidget(CtrlPyduino)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 70, 269, 181))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.gridLNumeros = QtGui.QGridLayout(self.formLayoutWidget)
        self.gridLNumeros.setMargin(0)
        self.gridLNumeros.setObjectName(_fromUtf8("gridLNumeros"))
        self.siete = QtGui.QPushButton(self.formLayoutWidget)
        self.siete.setObjectName(_fromUtf8("siete"))
        self.gridLNumeros.addWidget(self.siete, 4, 0, 1, 1)
        self.cero = QtGui.QPushButton(self.formLayoutWidget)
        self.cero.setObjectName(_fromUtf8("cero"))
        self.gridLNumeros.addWidget(self.cero, 5, 1, 1, 1)
        self.tres = QtGui.QPushButton(self.formLayoutWidget)
        self.tres.setObjectName(_fromUtf8("tres"))
        self.gridLNumeros.addWidget(self.tres, 2, 2, 1, 1)
        self.seis = QtGui.QPushButton(self.formLayoutWidget)
        self.seis.setObjectName(_fromUtf8("seis"))
        self.gridLNumeros.addWidget(self.seis, 3, 2, 1, 1)
        self.power = QtGui.QPushButton(self.formLayoutWidget)
        self.power.setObjectName(_fromUtf8("power"))
        self.gridLNumeros.addWidget(self.power, 1, 0, 1, 1)
        self.uno = QtGui.QPushButton(self.formLayoutWidget)
        self.uno.setObjectName(_fromUtf8("uno"))
        self.gridLNumeros.addWidget(self.uno, 2, 0, 1, 1)
        self.cuatro = QtGui.QPushButton(self.formLayoutWidget)
        self.cuatro.setObjectName(_fromUtf8("cuatro"))
        self.gridLNumeros.addWidget(self.cuatro, 3, 0, 1, 1)
        self.cinco = QtGui.QPushButton(self.formLayoutWidget)
        self.cinco.setObjectName(_fromUtf8("cinco"))
        self.gridLNumeros.addWidget(self.cinco, 3, 1, 1, 1)
        self.nueve = QtGui.QPushButton(self.formLayoutWidget)
        self.nueve.setObjectName(_fromUtf8("nueve"))
        self.gridLNumeros.addWidget(self.nueve, 4, 2, 1, 1)
        self.cancelar = QtGui.QPushButton(self.formLayoutWidget)
        self.cancelar.setObjectName(_fromUtf8("cancelar"))
        self.gridLNumeros.addWidget(self.cancelar, 5, 2, 1, 1)
        self.ocho = QtGui.QPushButton(self.formLayoutWidget)
        self.ocho.setObjectName(_fromUtf8("ocho"))
        self.gridLNumeros.addWidget(self.ocho, 4, 1, 1, 1)
        self.dos = QtGui.QPushButton(self.formLayoutWidget)
        self.dos.setObjectName(_fromUtf8("dos"))
        self.gridLNumeros.addWidget(self.dos, 2, 1, 1, 1)
        self.formLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(300, 50, 191, 91))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.gridLCambios = QtGui.QGridLayout(self.formLayoutWidget_2)
        self.gridLCambios.setMargin(0)
        self.gridLCambios.setObjectName(_fromUtf8("gridLCambios"))
        self.volUp = QtGui.QPushButton(self.formLayoutWidget_2)
        self.volUp.setObjectName(_fromUtf8("volUp"))
        self.gridLCambios.addWidget(self.volUp, 0, 0, 1, 1)
        self.volDown = QtGui.QPushButton(self.formLayoutWidget_2)
        self.volDown.setObjectName(_fromUtf8("volDown"))
        self.gridLCambios.addWidget(self.volDown, 1, 0, 1, 1)
        self.chDown = QtGui.QPushButton(self.formLayoutWidget_2)
        self.chDown.setObjectName(_fromUtf8("chDown"))
        self.gridLCambios.addWidget(self.chDown, 1, 1, 1, 1)
        self.chUp = QtGui.QPushButton(self.formLayoutWidget_2)
        self.chUp.setObjectName(_fromUtf8("chUp"))
        self.gridLCambios.addWidget(self.chUp, 0, 1, 1, 1)
        self.formLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(300, 150, 271, 131))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.gridLControl = QtGui.QGridLayout(self.formLayoutWidget_3)
        self.gridLControl.setMargin(0)
        self.gridLControl.setObjectName(_fromUtf8("gridLControl"))
        self.input = QtGui.QPushButton(self.formLayoutWidget_3)
        self.input.setObjectName(_fromUtf8("input"))
        self.gridLControl.addWidget(self.input, 1, 0, 1, 1)
        self.right = QtGui.QPushButton(self.formLayoutWidget_3)
        self.right.setObjectName(_fromUtf8("right"))
        self.gridLControl.addWidget(self.right, 3, 2, 1, 1)
        self.down = QtGui.QPushButton(self.formLayoutWidget_3)
        self.down.setObjectName(_fromUtf8("down"))
        self.gridLControl.addWidget(self.down, 3, 0, 1, 1)
        self.up = QtGui.QPushButton(self.formLayoutWidget_3)
        self.up.setObjectName(_fromUtf8("up"))
        self.gridLControl.addWidget(self.up, 0, 0, 1, 1)
        self.left = QtGui.QPushButton(self.formLayoutWidget_3)
        self.left.setObjectName(_fromUtf8("left"))
        self.gridLControl.addWidget(self.left, 3, 1, 1, 1)
        self.ok = QtGui.QPushButton(self.formLayoutWidget_3)
        self.ok.setObjectName(_fromUtf8("ok"))
        self.gridLControl.addWidget(self.ok, 1, 1, 1, 1)
        self.menu = QtGui.QPushButton(self.formLayoutWidget_3)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.gridLControl.addWidget(self.menu, 1, 2, 1, 1)
        self.labelVideo = QtGui.QLabel(self.centralwidget)
        self.labelVideo.setGeometry(QtCore.QRect(520, 90, 81, 21))
        self.labelVideo.setStyleSheet(_fromUtf8("font: 12pt \"Cantarell\";"))
        self.labelVideo.setObjectName(_fromUtf8("labelVideo"))
        self.video = QtGui.QPushButton(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(510, 50, 91, 31))
        self.video.setObjectName(_fromUtf8("video"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 300, 271, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horLRutina = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horLRutina.setMargin(0)
        self.horLRutina.setObjectName(_fromUtf8("horLRutina"))
        self.siguiente = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.siguiente.setObjectName(_fromUtf8("siguiente"))
        self.horLRutina.addWidget(self.siguiente)
        self.anterior = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.anterior.setObjectName(_fromUtf8("anterior"))
        self.horLRutina.addWidget(self.anterior)
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 300, 160, 91))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushHDMI = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushHDMI.setObjectName(_fromUtf8("pushHDMI"))
        self.gridLayout.addWidget(self.pushHDMI, 3, 0, 1, 1)
        self.lineHDMI = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineHDMI.setObjectName(_fromUtf8("lineHDMI"))
        self.gridLayout.addWidget(self.lineHDMI, 0, 0, 1, 1)
        self.labelHDMI = QtGui.QLabel(self.gridLayoutWidget)
        self.labelHDMI.setObjectName(_fromUtf8("labelHDMI"))
        self.gridLayout.addWidget(self.labelHDMI, 2, 0, 1, 1)
        self.labelHDMI2 = QtGui.QLabel(self.gridLayoutWidget)
        self.labelHDMI2.setObjectName(_fromUtf8("labelHDMI2"))
        self.gridLayout.addWidget(self.labelHDMI2, 4, 0, 1, 1)
        #CtrlPyduino.setCentralWidget(self.centralwidget)

        self.retranslateUi(CtrlPyduino)
        QtCore.QMetaObject.connectSlotsByName(CtrlPyduino)

    def retranslateUi(self, CtrlPyduino):
        CtrlPyduino.setWindowTitle(_translate("CtrlPyduino", "MainWindow", None))
        self.comboBox.setItemText(0, _translate("CtrlPyduino", "Haier", None))
        self.comboBox.setItemText(1, _translate("CtrlPyduino", "LG", None))
        self.comboBox.setItemText(2, _translate("CtrlPyduino", "TotalPlay", None))
        self.siete.setText(_translate("CtrlPyduino", "7", None))
        self.cero.setText(_translate("CtrlPyduino", "0", None))
        self.tres.setText(_translate("CtrlPyduino", "3", None))
        self.seis.setText(_translate("CtrlPyduino", "6", None))
        self.power.setText(_translate("CtrlPyduino", "Power", None))
        self.uno.setText(_translate("CtrlPyduino", "1", None))
        self.cuatro.setText(_translate("CtrlPyduino", "4", None))
        self.cinco.setText(_translate("CtrlPyduino", "5", None))
        self.nueve.setText(_translate("CtrlPyduino", "9", None))
        self.cancelar.setText(_translate("CtrlPyduino", "X", None))
        self.ocho.setText(_translate("CtrlPyduino", "8", None))
        self.dos.setText(_translate("CtrlPyduino", "2", None))
        self.volUp.setText(_translate("CtrlPyduino", "VOL+", None))
        self.volDown.setText(_translate("CtrlPyduino", "VOL-", None))
        self.chDown.setText(_translate("CtrlPyduino", "CH-", None))
        self.chUp.setText(_translate("CtrlPyduino", "CH+", None))
        self.input.setText(_translate("CtrlPyduino", "INPUT", None))
        self.right.setText(_translate("CtrlPyduino", "Right ->", None))
        self.down.setText(_translate("CtrlPyduino", "Down", None))
        self.up.setText(_translate("CtrlPyduino", "Up", None))
        self.left.setText(_translate("CtrlPyduino", "<- Left ", None))
        self.ok.setText(_translate("CtrlPyduino", "OK", None))
        self.menu.setText(_translate("CtrlPyduino", "Menu", None))
        self.labelVideo.setText(_translate("CtrlPyduino", "Serie", None))
        self.video.setText(_translate("CtrlPyduino", "Video", None))
        self.siguiente.setText(_translate("CtrlPyduino", "Siguiente", None))
        self.anterior.setText(_translate("CtrlPyduino", "Anterior", None))
        self.pushHDMI.setText(_translate("CtrlPyduino", "Iniciar Prueba", None))
        self.labelHDMI.setText(_translate("CtrlPyduino", "<html><head/><body><p align=\"center\">Puertos HDMI</p></body></html>", None))
        self.labelHDMI2.setText(_translate("CtrlPyduino", "<html><head/><body><p align=\"center\"> </p></body></html>", None))

