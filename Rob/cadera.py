import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow,  QLabel, QSlider, QPushButton, QLineEdit, QApplication, QDial
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPoint
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import serial
import time

from definirServos import DefinirServos
from arduino import Arduino
from servos import Servos

class Cadera(QMainWindow):
    def __init__(self):
        super(Cadera,self).__init__()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, "cadera.ui")
        loadUi(ui_file, self)         
         
        self.definirServos = DefinirServos()
        self.arduino = Arduino()
        self.servos = Servos()        
         
        # Inicialización de la conexión serial
        self.arduino_port_izquierda=self.arduino.arduinoPuertoIzq
        self.baud_rate_izq=self.arduino.arduinoBaudiosIzq
        self.arduino_izq = serial.Serial(self.arduino.arduino_port_izquierda, self.arduino.baud_rate_izq)
        time.sleep(2)  # Esperar a que se establezca la conexión            
            
        
        # Datos servos brazo
        self.caderaPin=self.definirServos.caderaPin
        self.caderaMinimo=self.definirServos.caderaMinimo
        self.caderaMaximo=self.definirServos.caderaMaximo
        self.caderaInicio=self.definirServos.caderaInicio
        self.caderaRetraso=self.definirServos.caderaRetraso
        
        #Iniciar cabera
        self.servos.iniciarServoIzq(self.caderaPin,self.caderaInicio,self.caderaRetraso)               
        
        self.caderaProgressBar.hide()
        
        self.setWindowTitle("Cadera")

        # Botones de la barra superior
        self.click_posicion = QPoint()
        self.bt_close_cadera.clicked.connect(lambda: self.close())
        self.bt_minimize_cadera.clicked.connect(lambda: self.showMinimized())

        # Eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.etiquetaCaderaPin.setText(self.caderaPin)
        self.lcdNumber.display(self.caderaInicio)
        self.dial.setValue(self.caderaInicio)
        self.dial.valueChanged.connect(self.caderaDialPwm)
        self.caderaOnOff.clicked.connect(self.caderaOnOffPwm)
        self.caderaBucle.clicked.connect(self.caderaBuclePwm)
        self.caderaBotonInicio.clicked.connect(self.caderaInicioPwm)

        
    def caderaDialPwm(self, value):        
        self.lcdNumber.display(value) 
        self.enviar_comando(f"1,{self.caderaPin},{value},0,0,0,30\n")
        
    def caderaOnOffPwm(self):        
        if self.caderaOnOff.isChecked()==True:
            self.etiquetaCaderaOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaCaderaOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.caderaPin},0,0,0,0,0\n")
        else:
            self.etiquetaCaderaOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaCaderaOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.caderaPin},0,0,0,0,0\n")        
        
    def caderaBuclePwm(self):        
        if self.caderaBucle.isChecked()==True:
            self.etiquetaCaderaBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaCaderaBucle.setText(str('ON'))
            self.dial.setEnabled(False)            
            self.caderaOnOff.setChecked(True)
            self.etiquetaCaderaOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaCaderaOnOff.setText(str('ON'))          
            self.caderaOnOff.setEnabled(False)            
            self.enviar_comando(f"4,{self.caderaPin},0,0,0,0,0\n")
            time.sleep(0.3)            
            self.enviar_comando(f"6,{self.caderaPin},{self.caderaMinimo},{self.caderaMaximo},{self.caderaInicio},{self.caderaRetraso},75\n")
        else:
            self.etiquetaCaderaBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaCaderaBucle.setText(str('OFF'))
            self.dial.setEnabled(True)  
            self.caderaOnOff.setChecked(False)
            self.etiquetaCaderaOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaCaderaOnOff.setText(str('OFF'))
            self.caderaOnOff.setEnabled(True)
            self.enviar_comando(f"S")
         
    def caderaInicioPwm(self):        
        if self.caderaBotonInicio.isChecked()==True:
            self.caderaProgressBar.show()
            self.etiquetaCaderaInicio.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaCaderaInicio.setText(str('ON'))
            self.caderaOnOff.setChecked(True)
            self.etiquetaCaderaOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaCaderaOnOff.setText(str('ON'))
            QApplication.processEvents()
            self.enviar_comando(f"2,{self.caderaPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.enviar_comando(f"1,{self.caderaPin},{self.caderaInicio},0,0,0,75\n")
            time.sleep(1)
            self.enviar_comando(f"3,{self.caderaPin},0,0,0,0,0\n")
            self.caderaBotonInicio.setChecked(False)
            self.etiquetaCaderaInicio.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaCaderaInicio.setText(str('OFF'))
            self.caderaOnOff.setChecked(False)
            self.etiquetaCaderaOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaCaderaOnOff.setText(str('OFF'))
            self.lcdNumber.display(self.caderaInicio)
            self.dial.setValue(self.caderaInicio)
            self.caderaProgressBar.hide()
        
    def enviar_comando(self, comando):
        self.arduino_izq.write(comando.encode())
        print(f"Comando enviado: {comando}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = Cadera()
    my_app.show()
    sys.exit(app.exec_())
