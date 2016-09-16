from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from datetime import datetime, date, time, timedelta
import sys

def calcular_fecha(self):
	fecha_actual = datetime.now()
	mes_actual = fecha_actual.month
	año_actual = fecha_actual.year

	if mes_actual <= 9:
		mes_patrio = datetime(año_actual, 9, 15)
	else:
		mes_patrio = datetime(año_actual + 1, 9, 15)

	nueva_fecha = mes_patrio - fecha_actual

	text.setText("       Tiempo restante para el próximo\n" +
		"día de la Independencia: " + str(nueva_fecha))
	text.move(110, 20)

app = QApplication(sys.argv)
qhm = QtGui.QWidget()
text = QtGui.QLabel(qhm)
text.setText("Miguel Hidalgo y Costilla (1753 – 1811)\n"+
            "Ignacio Allende (1769 – 1811)\n"+
            "Josefa Ortiz de Domínguez (1768 – 1829)")
text.setOpenExternalLinks(True)
text.move(50,20)
btn = QtGui.QPushButton('Faltan', qhm)
btn.clicked.connect(calcular_fecha)
btn.resize(btn.sizeHint())
btn.move(150, 70)
qhm.setWindowIcon(QIcon('mex.png'))
qhm.resize(400,200)
qhm.setWindowTitle('¡¡Viva México Ca...!!')
qhm.show()
sys.exit(app.exec_())

"""
def fecha(self):
    hoy = datetime.now()
    if hoy.month <= 9:
        sep = datetime(hoy.year, 9, 15)
    else:
        sep = datetime(hoy.year + 1, 9, 15)
    text.setText("Faltan "+str(sep - hoy)+"\n"+"para el siguiente 15 de septiembre")
    text.move(110,20)

app = QApplication(sys.argv)
qhm = QtGui.QWidget()
text = QtGui.QLabel(qhm)
text.setText("Miguel Hidalgo y Costilla (1753 – 1811)\n"+
            "Ignacio Allende (1769 – 1811)\n"+
            "Josefa Ortiz de Domínguez (1768 – 1829)")
text.move(50,20)
btn = QtGui.QPushButton('Faltan', qhm)
btn.clicked.connect(fecha)
btn.resize(btn.sizeHint())
btn.move(150, 70)
qhm.setWindowIcon(QIcon('1.png'))
qhm.resize(400,200)
qhm.setWindowTitle('¡Viva México!')
qhm.show()
sys.exit(app.exec_())
"""