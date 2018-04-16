#=============
#IMPORTACIONES
#=============

# Importamos el módulo sys que provee el acceso a funciones y objetos mantenidos por el intérprete.
import sys
# Importamos las herramientas de PyQT que vamos a utilizar
from PyQt5 import QtWidgets, uic, QtGui
# Importamos los elementos que se encuentran dentro del diseñador
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QStackedWidget
# Importamos el modulo uic necesario para levantar un archivo .ui
from PyQt5 import uic
from vistas import postresCarga


#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase vistaLista
class VistaPostres(QtWidgets.QWidget):
	#Inicializacion del Objeto QWidget
	def __init__(self):
		QWidget.__init__(self)

		#Importamos la vista "listaAfiliados" y la alojamos dentro de la variable "vistaLista"
		self.vista_postres = uic.loadUi("gui/postres/postres.ui", self)
		self.vista_postres.btn_agregarpostres.clicked.connect(self.AbrirPostresCarga)


	def AbrirPostresCarga(QWidget):
		#variables que alojan las clases que se encuentran dentro del archivo .py. (nombredelArchivo.nombredelaClase)
		widget_postres = postresCarga.VistaPostresCarga()
		#hacemos correr la ventana
		widget_postres.show()