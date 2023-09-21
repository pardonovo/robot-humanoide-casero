import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem, QLabel, QSlider, QPushButton, QVBoxLayout, QLineEdit, QApplication, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPoint
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import serial
import time


from PyQt5.QtGui import QBrush, QColor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



from definirServos import DefinirServos
from arduino import Arduino
from servos import Servos

class AnilloLeds(QMainWindow):
    def __init__(self):
        super(AnilloLeds,self).__init__()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, "anilloLeds.ui")
        loadUi(ui_file, self)
         
        self.definirServos = DefinirServos()
        self.arduino = Arduino()
        self.servos = Servos()        
         
        # Inicialización de la conexión serial
        self.arduino_port_derecha=self.arduino.arduinoPuertoDer
        self.baud_rate_der=self.arduino.arduinoBaudiosDer
        self.arduino_der = serial.Serial(self.arduino.arduino_port_derecha, self.arduino.baud_rate_der)
        time.sleep(2)  # Esperar a que se establezca la conexión            
                    
        # Datos servos brazo
        self.anilloPin=self.definirServos.anilloPin        
        self.anilloInicio=self.definirServos.anilloInicio
        self.anilloRetraso=self.definirServos.anilloRetraso
        
        self.setWindowTitle("Anillo Leds")

        # Botones de la barra superior
        self.click_posicion = QPoint()
        self.bt_close_anillo.clicked.connect(lambda: self.close())
        self.bt_minimize_anillo.clicked.connect(lambda: self.showMinimized())

        # Eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.etiquetaAnilloPin.setText(self.anilloPin)
        self.anilloOnOff.clicked.connect(self.anilloOnOffPwm)
        self.anilloBucle.clicked.connect(self.anilloBuclePwm)
        self.anilloColores='true';        
      
        self.colors = [
            QColor(255, 0, 0),
            QColor(255, 165, 0),
            QColor(255, 0, 255),
            QColor(255, 192, 203),
            QColor(128, 0, 128),                
            QColor(0, 0, 128), 
            QColor(0, 0, 255),           
            QColor(133, 193, 233),
            QColor(0, 255, 255),            
            QColor(0, 128, 0),
            QColor(0, 255, 0),
            QColor(130, 224, 170),                                
            QColor(255, 255, 255),                                
            QColor(128, 128, 0),
            QColor(183, 149, 11),                                                
            QColor(255, 255, 0)             
        ]

        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)

        center_x = 350
        center_y = 350
        radius = 300

        angle_step = 360 / len(self.colors)
        for i, color in enumerate(self.colors):
            angle = i * angle_step
            x = center_x + radius * 0.9 * (-1 if angle <= 180 else 1) * abs(0.5 - abs((angle % 180) / 180 - 0.5))
            y = center_y + radius * 0.9 * (-1 if angle <= 90 or (angle > 180 and angle <= 270) else 1) * abs(0.5 - abs(((angle - 90) % 180) / 180 - 0.5))

            ellipse = QGraphicsEllipseItem(x - 20, y - 20, 40, 40)
            ellipse.setBrush(color)
            ellipse.setFlag(QGraphicsEllipseItem.ItemIsSelectable, True)
            self.scene.addItem(ellipse)

        self.scene.setSceneRect(self.scene.itemsBoundingRect())
        self.graphicsView.mousePressEvent = self.enviar_color

    def enviar_color(self, event):
        if self.anilloColores=='true':
            item = self.graphicsView.itemAt(event.pos())
            if isinstance(item, QGraphicsEllipseItem):
                color = item.brush().color()
                rgb_color = color.getRgb()
                self.enviar_comando(f"9,{self.anilloPin},{rgb_color[0]},{rgb_color[1]},{rgb_color[2]},0,0\n")           

    def anilloOnOffPwm(self):        
        if self.anilloOnOff.isChecked()==True:
            self.etiquetaAnilloOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaAnilloOnOff.setText(str('ON'))
            self.enviar_comando(f"7,{self.anilloPin},0,0,0,0,0\n")            
        else:
            self.etiquetaAnilloOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaAnilloOnOff.setText(str('OFF')) 
            self.enviar_comando(f"8,{self.anilloPin},0,0,0,0,0\n")        
        
    def anilloBuclePwm(self):        
        if self.anilloBucle.isChecked()==True:
            self.anilloColores='false'
            self.etiquetaAnilloBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaAnilloBucle.setText(str('ON'))            
            self.anilloOnOff.setChecked(True)
            self.etiquetaAnilloOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaAnilloOnOff.setText(str('ON'))          
            self.anilloOnOff.setEnabled(False)            
            self.enviar_comando(f"10,{self.anilloPin},0,0,0,0,0\n")
            time.sleep(0.3)            
            self.enviar_comando(f"11,{self.anilloPin},0,0,0,0,0\n")
        else:
            self.anilloColores='true'
            self.etiquetaAnilloBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaAnilloBucle.setText(str('OFF'))            
            self.anilloOnOff.setChecked(False)
            self.etiquetaAnilloOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaAnilloOnOff.setText(str('OFF'))
            self.anilloOnOff.setEnabled(True)
            self.enviar_comando(f"R")
         
    def enviar_comando(self, comando):
        self.arduino_der.write(comando.encode())
        print(f"Comando enviado: {comando}")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = AnilloLeds()
    my_app.show()
    sys.exit(app.exec_())
