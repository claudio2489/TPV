

#VENTANA PRINCIPAL#



#=============
#IMPORTACIONES
#=============

# Importamos el módulo sys que provee el acceso a funciones y objetos mantenidos por el intérprete.
import sys
# Importamos las herramientas de PyQT que vamos a utilizar
from PyQt5 import QtWidgets, uic, QtGui
# Importamos los elementos que se encuentran dentro del diseñador
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QStackedWidget, QDialog
# Importamos el modulo uic necesario para levantar un archivo .ui
from vistas import menu, comprarproducto


#====================
#DEFINICION DE CLASES
#====================

#Creacion de la clase menuPrincipal. Objeto tipo QMainWindow
class VistaPrincipal(QMainWindow):
	#Inicializacion del Objeto MainWindow
	def __init__(self):
		QMainWindow.__init__(self)

		#Importamos la vista "menuPrincipal" y la alojamos dentro de la variable "vistaprincipal"
		self.vista_principal = uic.loadUi("gui/principal.ui", self)
		
		#cambiamos el titulo de la ventana
		self.setWindowTitle("Resto")
		
		self.vista_principal.btn_iniciar.clicked.connect(self.AbrirMenu)
		self.vista_principal.btn_comprar.clicked.connect(self.AbrirComprarProducto)

	#===========================
	#DEFINICION DE LAS FUNCIONES
	#===========================
	def AbrirMenu(QWidget):
		#variables que alojan las clases que se encuentran dentro del archivo .py. (nombredelArchivo.nombredelaClase)
		widget_menu = menu.VistaMenu()
		#hacemos correr la ventana
		widget_menu.show()

	def AbrirComprarProducto(QWidget):
		#variables que alojan las clases que se encuentran dentro del archivo .py. (nombredelArchivo.nombredelaClase)
		widget_comprarproducto = comprarproducto.VistaComprarProducto()
		#hacemos correr la ventana
		widget_comprarproducto.show()

#======================
#EJECUTAR LA APLICACION
#======================

#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = VistaPrincipal()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()
