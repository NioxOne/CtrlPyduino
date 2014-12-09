#!/usr/bin/python 
#-*-coding:utf-8-*-
#control-0.1 optimizando código
import os
import subprocess
import serial
import sys
import time
from PyQt4 import QtGui
import autopy

class Control(object):

	def __init__(self):

		if sys.platform.startswith('linux'):
			puerto = "/dev/ttyACM0"
			self.rutaVideo = os.getcwd()+"/Videos"
			conexion = True
		elif sys.platform.startswith('win'):
			puerto = "COM3"		

		self.repSerie = True
		self.ser = ""
		while self.ser == "":
			try:
			    self.ser = serial.Serial(puerto,9600)	
			except:
				self.ser = ""
				self.noConexion()
			  
		    
	#Slots
	def siguiente(self):
		self.mensaje("s")
		print "Siguiente"
	
	def anterior(self):
		self.mensaje("r")
		print "Atras"

	#Método para saber que rutina ejecutar
	def mensaje(self,opcion):
		if opcion == "s" or opcion == "r":
	
			self.ser.write(opcion)
			#Tiempo de retardo de televisión HAIER al cambiar de HDMI
			time.sleep(4)
			#Saber si se ejecuta la lista de videos predeterminada o un video en especifico
			if self.repSerie:
				self.repMplayerCursor()
			else:
				self.repUnVideo()
				self.repSerie = True			
			
	
	#Metodos Para la funcionalidad de la Reproduccion de videos
	def repUnVideo(self):
		video = self.nombreArchivo(self.ruta,True)
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
	#Aun no es un metodo General que resuelva varios casos de uso.	
	def repMplayerCursor(self):
	  """
	  	Se mueve el cursor para hacer la pantalla de la tv activa
	  	Se utiliza konsole para abrir mplayer como proceso independiente
	  	Se utiliza totem para la reproducción del sonido y mplayer para los videos
	  	Al final se mata el proceso de konsole y totem 
	  	Se regresa el cursor a su posición inicial
	  """
	  pos_actual = autopy.mouse.get_pos()
	  autopy.mouse.move(1800,300)
	  autopy.mouse.click(autopy.mouse.LEFT_BUTTON)
	  m1 = os.getcwd() + "/Videos/m1.mp3"
	  subprocess.call(['konsole','--noclose','-e','totem',m1])
	  time.sleep(0.5) #Tiempo de retardo sincronización con la tv
	  for video in range(5):
 	  		video = os.getcwd() + "/Videos/" + str (video) + ".mp4"
	  		if sys.platform.startswith('linux'):
	  			subprocess.call(['konsole','--noclose','-e','mplayer','-fs',video])

			time.sleep(2)
			subprocess.call(['pkill',"mplayer"])

	  subprocess.call(['pkill',"konsole"])
	  subprocess.call(['pkill',"totem"])
	  autopy.mouse.move(*pos_actual)

	#Slot para seleccionar un video en específico y reproducirlo
	def ruta(self):
			os.chdir(dirActual)
			self.repSerie = False

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
			self.ser.write(direccion)
			print "Canal Arriba"
		elif direccion == "B":
			self.ser.write(direccion)
			print "Canal Abajo"
		elif direccion == "a":
			self.ser.write(direccion)
			print "Volumen Arriba"
		elif direccion == "b":
			self.ser.write(direccion)
			print "Volumen Abajo"
		elif direccion == "m":
			self.ser.write(direccion)
			print "Menu"
		elif direccion == "o":
			self.ser.write(direccion)
			print "OK"
		elif direccion == "u":
			self.ser.write(direccion)
			print "Arriba"
		elif direccion == "d":
			self.ser.write(direccion)
			print "Abajo"
		elif direccion == "p":
			self.ser.write(direccion)
			print "Encendido"
		elif direccion == "i":
			self.ser.write(direccion)
			print "Input"
		#Numeros
		elif direccion == "1":
			self.ser.write(direccion)
			print "Uno"
		elif direccion == "2":
			self.ser.write(direccion)
			print "dos"
		elif direccion == "3":
			self.ser.write(direccion)
			print "tres"
		elif direccion == "4":
			self.ser.write(direccion)
			print "cuatro"
		elif direccion == "5":
			self.ser.write(direccion)
			print "cinco"
		elif direccion == "6":
			self.ser.write(direccion)
			print "seis"
		elif direccion == "7":
			self.ser.write(direccion)
			print "siete"
		elif direccion == "8":
			self.ser.write(direccion)
			print "ocho"
		elif direccion == "9":
			self.ser.write(direccion)
			print "nueve"
		elif direccion == "0":
			self.ser.write(direccion)
			print "cero"
		
	#Slots
	def power(self):
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
	#NUmeros
	def uno(self):
		self.cambiar("1")
	def dos(self):
		self.cambiar("2")	
	def tres(self):
		self.cambiar("3")
	def cuatro(self):
		self.cambiar("4")
	def cinco(self):
		self.cambiar("5")
	def seis(self):
		self.cambiar("6")
	def siete(self):
		self.cambiar("7")
	def ocho(self):
		self.cambiar("8")
	def nueve(self):
		self.cambiar("9")
	def cero(self):
		self.cambiar("0")

	def noConexion(self):	
		print "Arduino no Conectado"
	  	msgBox = QtGui.QMessageBox()
	  	msgBox.setText("Dispositivo No Conectado")
	  	msgBox.setInformativeText("Conecte el dispositivo al puerto USB")
	  	icono = QtGui.QMessageBox.Critical
	  	msgBox.setIcon(icono)
	  	iconoVentana = QtGui.QIcon("iconos/domHome.png")
	  	msgBox.setWindowIcon(iconoVentana)
	  	msgBox.show()
	  	msgBox.exec_()
