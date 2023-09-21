import sys
from random import randint
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QSlider, QLabel, QMainWindow, QPushButton
from PyQt5.QtCore import Qt

from dedosManoDerecha import DedosDerecha
from dedosManoIzquierda import DedosIzquierda
from brazoDerecho import BrazoDerecho
from brazoIzquierdo import BrazoIzquierdo
from cabeza import Cabeza
from cadera import Cadera
from boca import Boca
from anilloLeds import AnilloLeds

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(790, 445)
        self.setWindowTitle('Robot Rob')
        self.ventanaDedosDerecha = DedosDerecha()
        self.ventanaDedosIzquierda = DedosIzquierda()
        self.ventanaBrazoDerecho = BrazoDerecho()
        self.ventanaBrazoIzquierdo = BrazoIzquierdo()
        self.ventanaCabeza = Cabeza()
        self.ventanaCadera = Cadera()
        self.ventanaBoca = Boca()
        self.ventanaAnilloLeds = AnilloLeds()

        l = QHBoxLayout()
        
        buttonDedosDerecha = QPushButton("Dedos mano derecha")
        buttonDedosDerecha.clicked.connect(self.toggle_ventanaDedosDerecha)
        l.addWidget(buttonDedosDerecha)

        buttonDedosIzquierda = QPushButton("Dedos mano izquierda")
        buttonDedosIzquierda.clicked.connect(self.toggle_ventanaDedosIzquierda)
        l.addWidget(buttonDedosIzquierda)
     
        buttonBrazoDerecho = QPushButton("Brazo Derecho")
        buttonBrazoDerecho.clicked.connect(self.toggle_ventanaBrazoDerecho)
        l.addWidget(buttonBrazoDerecho)
 
        buttonBrazoIzquierdo = QPushButton("Brazo Izquierdo")
        buttonBrazoIzquierdo.clicked.connect(self.toggle_ventanaBrazoIzquierdo)
        l.addWidget(buttonBrazoIzquierdo)
        
        buttonCabeza = QPushButton("Cabeza")
        buttonCabeza.clicked.connect(self.toggle_ventanaCabeza)
        l.addWidget(buttonCabeza)

        buttonCadera = QPushButton("Cadera")
        buttonCadera.clicked.connect(self.toggle_ventanaCadera)
        l.addWidget(buttonCadera)
        
        buttonBoca = QPushButton("Boca")
        buttonBoca.clicked.connect(self.toggle_ventanaBoca)
        l.addWidget(buttonBoca)
        
        buttonAnilloLeds = QPushButton("Anillo Leds")
        buttonAnilloLeds.clicked.connect(self.toggle_ventanaAnilloLeds)
        l.addWidget(buttonAnilloLeds)
        
        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

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

    def toggle_ventanaCabeza(self, checked):       
        if self.ventanaCabeza.isVisible():
            self.ventanaCabeza.hide()
        else:
            self.ventanaCabeza.show()

    def toggle_ventanaCadera(self, checked):       
        if self.ventanaCadera.isVisible():
            self.ventanaCadera.hide()
        else:
            self.ventanaCadera.show()
            
    def toggle_ventanaBoca(self, checked):       
        if self.ventanaBoca.isVisible():
            self.ventanaBoca.hide()
        else:
            self.ventanaBoca.show()
            
    def toggle_ventanaAnilloLeds(self, checked):       
        if self.ventanaAnilloLeds.isVisible():
            self.ventanaAnilloLeds.hide()
        else:
            self.ventanaAnilloLeds.show()                        
            
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()