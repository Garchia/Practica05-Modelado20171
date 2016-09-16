# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from datetime import date
import sys

class Independencia(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        titulo = "¡¡¡Viva México Ca...!!!"
        imagen = 'mex.png'

        self.resize(410, 260)
        self.setWindowIcon(QIcon(imagen))
        self.setWindowTitle(titulo)
        self.boton()
        self.texto()

    # Crea el botón que se usa para calcular el tiempo
    # que resta para el siguiente Grito de la Independencia
    def boton(self):
        self.button = QPushButton('Días Para el Siguiente Grito', self)
        self.button.setFixedWidth(260)
        self.button.move(72, 140)
        self.button.clicked.connect(self.click)

    def texto(self):

        # Vínculos a Wikipedia de cada uno de los héroes de Independencia
        a = '<a href="https://es.wikipedia.org/wiki/Miguel_Hidalgo_y_Costilla">Miguel Hidalgo y Costilla'
        b = '<a href="https://es.wikipedia.org/wiki/José_María_Morelos">José María Morelos'
        c = '<a href="https://es.wikipedia.org/wiki/Vicente_Guerrero">Vicente Guerrero'

        # Años que vivió cada uno
        sa = '(1765-1815)'
        sb = '(1753-1811)'
        sc = '(1782-1831)'

        # Establece los 3 hipervínculos
        self.label = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)

        # Fusiona los hipervínculos con el rango vivido
        self.label.setText(a + ' ' + sa)
        self.label2.setText(b + ' ' + sb)
        self.label3.setText(c + ' ' + sc)

        # Separa los 3 hipervínculos uno tras otro
        self.label.setOpenExternalLinks(True)
        self.label.move(20, 20)
        self.label2.setOpenExternalLinks(True)
        self.label2.move(20, 40)
        self.label3.setOpenExternalLinks(True)
        self.label3.move(20, 60)     

    # Define los cambios en el botón después de haber dado click
    def click(self):

        # Obtiene la fecha del sistema
        fecha = date.today()

        dia_indep = date(fecha.year, 9, 15)
        dias_restantes = (dia_indep - fecha).days

        # Almacena las cadenas que se mostrarán en el botón al dar click
        viva_mexico = 'Hoy es 15 de Septiembre: ¡¡VIVA MÉXICO!!'
        tiempo_restante = 'Faltan {} días para el próximo grito'.format(dias_restantes)

        # Determina el tiempo que falta para llegar al próximo grito
        if dias_restantes < 0:
            dia_indep = date(fecha.year + 1, 9, 15)
            dias_restantes = (dia_indep - fecha).days
        if dias_restantes == 0:
            display = viva_mexico
        else:
            display = tiempo_restante

        # Muestra el mensaje adecuado al dar click
        self.button.setText(display)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    indep = Independencia()
    indep.show()
    app.exec_()