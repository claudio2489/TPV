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
from vistas import accaja, acmesas, carta, bebidas, entradas, platos, postres


#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase vistaLista
class VistaMenu(QtWidgets.QWidget):
	#Inicializacion del Objeto QWidget
	def __init__(self):
		QWidget.__init__(self)

		#Importamos la vista "listaAfiliados" y la alojamos dentro de la variable "vistaLista"
		self.vista_menu = uic.loadUi("gui/menu.ui", self)
		self.vista_menu.showMaximized()
		self.vista_menu.btn_accaja.clicked.connect(self.AbrirAccaja)
		self.vista_menu.btn_acmesas.clicked.connect(self.AbrirAcmesas)
		self.vista_menu.btn_carta.clicked.connect(self.AbrirCarta)
		self.vista_menu.btn_entradas.clicked.connect(self.AbrirEntradas)
		self.vista_menu.btn_platos.clicked.connect(self.AbrirPlatos)
		self.vista_menu.btn_bebidas.clicked.connect(self.AbrirBebidas)
		self.vista_menu.btn_postres.clicked.connect(self.AbrirPostres)



	#===========================
	#DEFINICION DE LAS FUNCIONES
	#===========================
	def AbrirAccaja(QWidget):
		#variables que alojan las clases que se encuentran dentro del archivo .py. (nombredelArchivo.nombredelaClase)
		widget_accaja = accaja.VistaAccaja()
		#hacemos correr la ventana
		widget_accaja.show()

	def AbrirAcmesas(QWidget):
		#variables que alojan las clases que se encuentran dentro del archivo .py. (nombredelArchivo.nombredelaClase)
		widget_acmesas = acmesas.VistaAcmesas()
		#hacemos correr la ventana
		widget_acmesas.show()


	def AbrirCarta(QWidget):
		#variables que alojan las clases que se encuentran dentro del archivo .py. (nombredelArchivo.nombredelaClase)
		widget_carta = carta.VistaCarta()
		#hacemos correr la ventana
		widget_carta.show()

	def AbrirEntradas(QWidget):
		#variables que alojan las clases que se encuentran dentro del archivo .py. (nombredelArchivo.nombredelaClase)
		widget_entradas = entradas.VistaEntradas()
		#hacemos correr la ventana
		widget_entradas.show()

	def AbrirPlatos(QWidget):
		#variables que alojan las clases que se encuentran dentro del archivo .py. (nombredelArchivo.nombredelaClase)
		widget_platos = platos.VistaPlatos()
		#hacemos correr la ventana
		widget_platos.show()

	def AbrirBebidas(QWidget):
		#variables que alojan las clases que se encuentran dentro del archivo .py. (nombredelArchivo.nombredelaClase)
		widget_bebidas = bebidas.VistaBebidas()
		#hacemos correr la ventana
		widget_bebidas.show()

	def AbrirPostres(QWidget):
		#variables que alojan las clases que se encuentran dentro del archivo .py. (nombredelArchivo.nombredelaClase)
		widget_postres = postres.VistaPostres()
		#hacemos correr la ventana
		widget_postres.show()


