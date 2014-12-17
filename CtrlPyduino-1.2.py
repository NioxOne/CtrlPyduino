#!/usr/bin/python 
#-*-coding: utf-8 -*-
"""
	Copyright (C) <9/12/2014r> <Nicolas Lemus Plascencia>
				 			   <NioxDev@gmail.com>
	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
	GNU General Public License for more details.
	You should have received a copy of the GNU General Public License
	along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import sys
#import serial
from PyQt4 import QtGui, QtCore
from GUIPyduino import Ui_CtrlPyduino
from control import Control

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

		#Rutina Prueba HDMI
		self.gui.pushHDMI.clicked.connect(self.rutinaProbarHDMI)
		#Exit, Right, Left
		self.gui.cancelar.clicked.connect(self.control.exit)
		self.gui.left.clicked.connect(self.control.left)
		self.gui.right.clicked.connect(self.control.right)
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
	
	def rutinaProbarHDMI(self):
		puertos = int (self.gui.lineHDMI.text())
		for puerto in range(puertos):
			puerto = puerto + 1
			print puerto
			puerto = "<center>Probando HDMI %s </center>" % str (puerto)
			self.gui.labelHDMI2.setText(puerto)
			self.control.siguiente()
		self.gui.labelHDMI2.setText("")

def main():
	app = QtGui.QApplication(sys.argv);
	control = CtrlPyduino()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
