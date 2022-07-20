import sys
from Calculadora_Timp import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime
from PyQt5.QtGui import QIcon
from datetime import datetime, timedelta
# Desenvolvido por Esdras Ribas


class Calculadora(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calculadora, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCalcular.clicked.connect(self.calcular)
    def calcular(self):
        dt_inicio = self.ui.dtInicio.dateTime()
        dtInicio = dt_inicio.toPyDateTime() # Convertendo para datetime.datetime
        dt_fim = self.ui.dtFim.dateTime()
        dtFim = dt_fim.toPyDateTime() # Convertendo para datetime.datetime       

        diff = dtFim - dtInicio
        days = diff.days
        years, days = days // 365, days % 365
        months, days = days // 30, days % 30

        seconds = diff.seconds
        hours, seconds = seconds // 3600, seconds % 3600
        minutes, seconds = seconds // 60, seconds % 60

        if dtInicio < dtFim:
            if years > 0:
                self.ui.resultado.setText(f"Timp: {(years * 8760) + hours}:{minutes.__str__().zfill(2)} ")
            elif months > 0:
                self.ui.resultado.setText(f"Timp: {(months * 730) + hours}:{minutes.__str__().zfill(2)} ")
            else:
                self.ui.resultado.setText(f"Timp: {(days * 24) + hours}:{minutes.__str__().zfill(2)} ")
        else:
            self.ui.resultado.setText(f"Data Inicio >= a Data Fim.")

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Calculadora()
    win.setWindowTitle("Calculadora TIMP")
    win.setWindowIcon(QIcon("timp.jpeg"))
    win.show()
    sys.exit(app.exec_())
