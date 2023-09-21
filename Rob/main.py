import sys
import os
import subprocess
import smbus
import struct
from random import randint
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,  QLabel, QSlider, QPushButton, QLineEdit, QApplication, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPoint, QTimer
from PyQt5 import QtCore, QtWidgets

from dedosManoDerecha import DedosDerecha
from dedosManoIzquierda import DedosIzquierda
from brazoDerecho import BrazoDerecho
from brazoIzquierdo import BrazoIzquierdo
from cabeza import Cabeza
from cadera import Cadera
from boca import Boca
from anilloLeds import AnilloLeds
from testprueba import Testprueba

class Main(QMainWindow):
    def __init__(self):
       super(Main,self).__init__()
       
       script_dir = os.path.dirname(os.path.abspath(__file__))
       ui_file = os.path.join(script_dir, "main.ui")
       loadUi(ui_file, self)                   

       self.setWindowTitle("Robot")

       self.testprueba = Testprueba()

       # Botones de la barra superior
       self.click_posicion = QPoint()
       self.bt_close_main.clicked.connect(lambda: self.close())
       self.bt_minimize_main.clicked.connect(lambda: self.showMinimized())
    
       # Eliminar barra de titulo
       self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
       self.setWindowOpacity(1)
       self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
       self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
       
       self.ventanaCabeza = Cabeza()
       self.ventanaCadera = Cadera()
       self.ventanaBoca = Boca()
       self.ventanaDedosDerecha = DedosDerecha()
       self.ventanaDedosIzquierda = DedosIzquierda()
       self.ventanaBrazoDerecho = BrazoDerecho()
       self.ventanaBrazoIzquierdo = BrazoIzquierdo()       
       self.ventanaAnilloLeds = AnilloLeds()      
                
       self.cabezaPushButton.clicked.connect(self.toggle_ventanaCabeza)
       self.bocaPushButton.clicked.connect(self.toggle_ventanaBoca)
       self.manoDerechaPushButton.clicked.connect(self.toggle_ventanaDedosDerecha)
       self.manoIzquierdaPushButton.clicked.connect(self.toggle_ventanaDedosIzquierda)
       self.brazoDerechoPushButton.clicked.connect(self.toggle_ventanaBrazoDerecho)
       self.brazoIzquierdoPushButton.clicked.connect(self.toggle_ventanaBrazoIzquierdo)
       self.caderaPushButton.clicked.connect(self.toggle_ventanaCadera)
       self.anilloLedsPushButton.clicked.connect(self.toggle_ventanaAnilloLeds)
       
       self.apagado.clicked.connect(self.apagarSistema)       
       bus = smbus.SMBus(1)      
       self.timer = QTimer(self)
       self.timer.timeout.connect(lambda: self.readCapacity(bus))       
       self.timer.start(400)
       
       self.testPrueba.clicked.connect(self.testeoPrueba)


    def readCapacity(self,bus):
        try:
            address = 0x36
            read = bus.read_word_data(address, 4)
            swapped = struct.unpack("<H", struct.pack(">H", read))[0]
            capacity = swapped / 256           
            if capacity>0:                                
                self.bateriaRpi.setValue(int(capacity))
                
            return capacity
        except OSError as e:            
            return None
        
    def apagarSistema(self):
        respuesta = QMessageBox()
        respuesta.setIcon(QMessageBox.Question)
        respuesta.setWindowTitle('Apagar Robot')
        respuesta.setText('¿Desea apagar el robot?')
        respuesta.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
               
        respuesta.button(QMessageBox.Yes).setText('Si')

        buttonClicked = respuesta.exec_()
        
        if buttonClicked == QMessageBox.Yes:
            subprocess.run(['sudo /usr/local/bin/x750shutdown.sh'], shell=True)
        else:
            print("No se apagará el robot.")
            
    def testeoPrueba(self):
        self.testPrueba.setText(str('Ejecutando test'))
        QApplication.processEvents()
        self.testprueba.comenzarTest()
        self.testPrueba.setText(str('Test de prueba'))
        QApplication.processEvents()

    def toggle_ventanaCabeza(self, checked):       
        if self.ventanaCabeza.isVisible():
            self.ventanaCabeza.hide()
        else:
            self.ventanaCabeza.show()
            
    def toggle_ventanaBoca(self, checked):       
        if self.ventanaBoca.isVisible():
            self.ventanaBoca.hide()
        else:
            self.ventanaBoca.show()
            
    def toggle_ventanaDedosDerecha(self, checked):        
        if self.ventanaDedosDerecha.isVisible():
            self.ventanaDedosDerecha.hide()
        else:
            self.ventanaDedosDerecha.show()            

    def toggle_ventanaDedosIzquierda(self, checked):        
        if self.ventanaDedosIzquierda.isVisible():
            self.ventanaDedosIzquierda.hide()
        else:
            self.ventanaDedosIzquierda.show()

    def toggle_ventanaBrazoDerecho(self, checked):       
        if self.ventanaBrazoDerecho.isVisible():
            self.ventanaBrazoDerecho.hide()
        else:
            self.ventanaBrazoDerecho.show()

    def toggle_ventanaBrazoIzquierdo(self, checked):       
        if self.ventanaBrazoIzquierdo.isVisible():
            self.ventanaBrazoIzquierdo.hide()
        else:
            self.ventanaBrazoIzquierdo.show()
            
    def toggle_ventanaCadera(self, checked):       
        if self.ventanaCadera.isVisible():
            self.ventanaCadera.hide()
        else:
            self.ventanaCadera.show()
            
    def toggle_ventanaAnilloLeds(self, checked):       
        if self.ventanaAnilloLeds.isVisible():
            self.ventanaAnilloLeds.hide()
        else:
            self.ventanaAnilloLeds.show()
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = Main()
    my_app.show()
    sys.exit(app.exec_())
