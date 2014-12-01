#!/usr/bin/python
#-*- coding: utf-8 -*-
#CtrlPyduino-1.0
"""
	Copyright (C) <28/11/2014r>  <Nicolas Lemus Plascencia>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import subprocess
import time
import serial
import sys 
from PyQt4 import QtGui


if sys.platform.startswith('linux'):
	puerto = "/dev/ttyACM0"
	ruta = "/home/NIOX/Documentos/HDMI_HAIER/Videos"
elif sys.platform.startswith('win'):
	puerto = "COM3"


ser = serial.Serial(puerto,9600)

class Verificador(QtGui.QWidget):

	def __init__(self):
		super(Verificador, self).__init__()
		self.initUI()
		self.rutaVideo = ""
		self.reproduccion = True

	def initUI(self):
		#Ventana 
		self.resize(400,300)
		self.setGeometry(300,300, 400,400)
		self.setWindowTitle("Verificador HDMI 1.0")
		#Botones
		btn1 = QtGui.QPushButton("Siguiente")
		btn2 = QtGui.QPushButton("Atras") 
		power = QtGui.QPushButton("Power")		
		btn3 = QtGui.QPushButton("Up")
		btn4 = QtGui.QPushButton("Down")
		btn5 = QtGui.QPushButton("Vol+")
		btn6 = QtGui.QPushButton("Vol-")

		btn7 = QtGui.QPushButton("OK")
		btn8 = QtGui.QPushButton("Menu")
		btn9 = QtGui.QPushButton("Up")
		btn10 = QtGui.QPushButton("Down")
		btn11 = QtGui.QPushButton("Input")
		#Boton para abrir archivos
		btn12 = QtGui.QPushButton("Video")

		#Tamaño de los botones		
		btn1.resize(btn1.sizeHint())
		btn2.resize(btn2.sizeHint())
		power.resize(power.sizeHint())
		btn3.resize(btn2.sizeHint())
		btn4.resize(btn4.sizeHint())
		btn5.resize(btn5.sizeHint())
		btn6.resize(btn6.sizeHint())
		btn7.resize(btn7.sizeHint())
		btn8.resize(btn8.sizeHint())
		btn9.resize(btn9.sizeHint())
		btn10.resize(btn10.sizeHint())
		btn11.resize(btn11.sizeHint())
		btn12.resize(btn12.sizeHint())
		
		#Eventos
		btn1.clicked.connect(self.siguiente)
		btn2.clicked.connect(self.atras)
		power.clicked.connect(self.encendido)
		btn3.clicked.connect(self.chUp)
		btn4.clicked.connect(self.chDown)
		btn5.clicked.connect(self.volUp)
		btn6.clicked.connect(self.volDown)
		btn7.clicked.connect(self.ok)
		btn8.clicked.connect(self.menu)
		btn9.clicked.connect(self.up)
		btn10.clicked.connect(self.down)
		btn11.clicked.connect(self.input)
		btn12.clicked.connect(self.rutaVideo)

		#Ventana de ayuda
		letra = QtGui.QFont('SansSerif',10)
		QtGui.QToolTip.setFont(letra)
		btn1.setToolTip("Verifica Entrada Siguiente")
		btn2.setToolTip("Verifica Entrada Anterior")
		power.setToolTip("Enciende y Apaga la TV")

		#Etiquetas
		self.estado = QtGui.QLabel("Verificando...")
		self.estado.hide()
		#Layout
		gridBox = QtGui.QGridLayout(self)
		gridBox.addWidget(power,0,0)
		#Canales		
		gridBox.addWidget(btn3,0,3)
		gridBox.addWidget(btn4,0,4)
		#Volumen
		gridBox.addWidget(btn5,1,3)
		gridBox.addWidget(btn6,1,4)		
		#Menu
		gridBox.addWidget(btn7,2,1)
		gridBox.addWidget(btn8,3,1)	
		gridBox.addWidget(btn9,2,0)
		gridBox.addWidget(btn11,1,1)
		gridBox.addWidget(btn10,2,2)
	
		#Atras y Siguiente
		gridBox.addWidget(btn1,4,0)
		gridBox.addWidget(btn2,4,1)		
		#Abrir Archivo
		gridBox.addWidget(btn12,0,2)

		gridBox.addWidget(self.estado,1,0)
		self.setLayout(gridBox)
		
		self.show()

	#Slots
	def siguiente(self):
		self.mensaje("1")
		print "Siguiente"
	
	def atras(self):
		self.estado.show()
		self.mensaje("2")
		self.estado.hide()
		print "Atras"

	#Método para saber que rutina ejecutar
	def mensaje(self,opcion):
		if opcion == "1" or opcion == "2":
			try:
				ser.write(opcion)
				#Tiempo de retardo de televisión HAIER al cambiar de HDMI
				time.sleep(4)

				#Saber si se ejecuta la lista de videos predeterminada o un video en especifico
				if self.reproduccion:
					self.repVideos()

				else:
					self.repUnVideo()
					self.reproduccion = True

			except:
				print "No se pudieron enviar Datos"
				print os.getcwd()
	
	def repUnVideo(self):
		video = self.nombreArchivo(self.rutaVideo,True)
		print "El nombre del video es",video
		#xdg-open abre el archivo con el programa determinado
		subprocess.call(["xdg-open",video])
		time.sleep(3)
		#Se utiliza el manejador de ventanas en modo consola wmctrl		
		subprocess.call(["wmctrl","-r",video,"-b","add,fullscreen"])
		subprocess.call(["wmctrl","-R",video])
		print "Reproduciendo..."
		time.sleep(2)
		subprocess.call(["pkill","totem"])

	#Método utilizado para reproducir una serie de videos en específico. 
	#Aun no es un metodo General que resuelve varios casos de uso.
	def repVideos(self):
		os.chdir(ruta)
		for video in range(5):
			video = str (video) + ".mp4"
			print video		
			
			if sys.platform.startswith('linux'):
				subprocess.call(["xdg-open",video])
				if video == "0.mp4":
					#Tiempo de retardo para maximizar totem
						time.sleep(3)
						subprocess.call(["wmctrl","-r",video,"-b","add,fullscreen"])
						subprocess.call(["wmctrl","-R",video])
			print "Reproduciendo..."
			#Espera dos 2s antes de cerrar totem
			time.sleep(2)
			if video == "4.mp4":
				subprocess.call(["pkill","totem"])

			elif sys.platform.startswith('win'):
				os.startfile(video)

	#Slot para seleccionar un video en específico y reproducirlo
	def rutaVideo(self):
		self.rutaVideo = QtGui.QFileDialog.getOpenFileName(self,"Abrir Archivo",ruta)
		#print self.rutaVideo
		dirActual = self.nombreArchivo(self.rutaVideo,False)
		if dirActual != '':
			os.chdir(dirActual)
			self.reproduccion = False

	def nombreArchivo(self,ruta,dic_o_archivo):
		i = 0 
		coincidencias = []
		for caracter in ruta:
			if caracter == '/':
				coincidencias.append(i)
			i+=1
		print coincidencias

		nom_archivo = ""
		#si hay elementos en la lista
		if len(coincidencias) > 0:
			ult_coincidencia = coincidencias[-1]
			
			if dic_o_archivo == True:
				#Se obtiene el nombre del archivo
				nom_archivo = ruta[ult_coincidencia+1:]

			else:
				#Se obtiene el nombre del directorio en el cual esta el archivo
				nom_archivo = ruta[:ult_coincidencia]

		return nom_archivo			

	#Método envía la opción correspondiente a Arduino
	def cambiar(self,direccion):
		if direccion == "A":
			ser.write(direccion)
			print "Canal Arriba"
		elif direccion == "B":
			ser.write(direccion)
			print "Canal Abajo"
		elif direccion == "a":
			ser.write(direccion)
			print "Volumen Arriba"
		elif direccion == "b":
			ser.write(direccion)
			print "Volumen Abajo"
		elif direccion == "m":
			ser.write(direccion)
			print "Menu"
		elif direccion == "o":
			ser.write(direccion)
			print "OK"
		elif direccion == "u":
			ser.write(direccion)
			print "Arriba"
		elif direccion == "d":
			ser.write(direccion)
			print "Abajo"
		elif direccion == "p":
			ser.write(direccion)
			print "Encendido"
		elif direccion == "i":
			ser.write(direccion)
			print "Input"

	#Slots
	def encendido(self):
		self.cambiar("p")
	def chUp(self):
		self.cambiar("A")	
	def chDown(self):
		self.cambiar("B")
	def volUp(self):
		self.cambiar("a")
	def volDown(self):
		self.cambiar("b")
	def menu(self):
		self.cambiar("m")
	def ok(self):
		self.cambiar("o")
	def up(self):
		self.cambiar("u")
	def down(self):
		self.cambiar("d")
	def input(self):
		self.cambiar("i")

def main():
	app = QtGui.QApplication(sys.argv)
	verificar = Verificador()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
