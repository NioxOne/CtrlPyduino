#!/usr/bin/python 
#-*-coding: utf-8 -*-
import sys
#import serial
from PyQt4 import QtGui, QtCore
from GUIPyduino import Ui_CtrlPyduino
from control1 import Control

class CtrlPyduino(QtGui.QWidget):

	def __init__(self):
		super(CtrlPyduino, self).__init__()
		self.initUI()
		
	def initUI(self):
		#GUI
		self.gui = Ui_CtrlPyduino()
		self.gui.setupUi(self)
		#Control
		self.control = Control()
		#Ajustes
		self.move(350,200)
		self.setWindowTitle("CtrlPyduino-1.1")
		#Icono
		icono = QtGui.QIcon("iconos/domHome.png")
		self.setWindowIcon(icono)

		#Eventos --> Signlas y Slots
		self.gui.siguiente.clicked.connect(self.control.siguiente)
		self.gui.anterior.clicked.connect(self.control.anterior)
		self.gui.input.clicked.connect(self.control.input)

		self.gui.video.clicked.connect(self.control.ruta)
		self.gui.volUp.clicked.connect(self.control.volUp)
		self.gui.volDown.clicked.connect(self.control.volDown)
		self.gui.chUp.clicked.connect(self.control.chUp)
		self.gui.down.clicked.connect(self.control.down)
		self.gui.up.clicked.connect(self.control.up)
		self.gui.ok.clicked.connect(self.control.ok)
		self.gui.menu.clicked.connect(self.control.menu)
		self.gui.chDown.clicked.connect(self.control.chDown)
		self.gui.power.clicked.connect(self.control.power)
		#Teclas Rápidas
		self.gui.siguiente.setShortcut('S')
		self.gui.anterior.setShortcut('A')
		self.gui.input.setShortcut('I')
		self.gui.volUp.setShortcut('+')
		self.gui.volDown.setShortcut('-')
		self.gui.chUp.setShortcut("Ctrl++")
		self.gui.chDown.setShortcut("Ctrl+-")
		self.gui.up.setShortcut("Up")
		self.gui.down.setShortcut("Down")
		self.gui.ok.setShortcut("k")
		self.gui.menu.setShortcut("m")
		self.gui.power.setShortcut("p")

		#Números
		self.gui.uno.clicked.connect(self.control.uno)
		self.gui.dos.clicked.connect(self.control.dos)
		self.gui.tres.clicked.connect(self.control.tres)
		self.gui.cuatro.clicked.connect(self.control.cuatro)
		self.gui.cinco.clicked.connect(self.control.cinco)
		self.gui.seis.clicked.connect(self.control.seis)
		self.gui.siete.clicked.connect(self.control.siete)
		self.gui.ocho.clicked.connect(self.control.ocho)
		self.gui.nueve.clicked.connect(self.control.nueve)
		self.gui.cero.clicked.connect(self.control.cero)
		self.showMaximized()
		self.show()

		#Teclas Rápidas
		#Teclas Rápidas
		self.gui.uno.setShortcut('1')
		self.gui.dos.setShortcut('2')
		self.gui.tres.setShortcut('3')
		self.gui.cuatro.setShortcut('4')
		self.gui.cinco.setShortcut('5')
		self.gui.seis.setShortcut("6")
		self.gui.siete.setShortcut("7")
		self.gui.ocho.setShortcut("8")
		self.gui.nueve.setShortcut("9")
		self.gui.cero.setShortcut("0")
	
def main():
	app = QtGui.QApplication(sys.argv);
	control = CtrlPyduino()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
