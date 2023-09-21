import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow,  QLabel, QSlider, QPushButton, QLineEdit, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPoint
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import serial
import time

from definirServos import DefinirServos
from arduino import Arduino
from servos import Servos
from voz import Voz

class Boca(QMainWindow):
    def __init__(self):
        super(Boca,self).__init__()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, "boca.ui")
        loadUi(ui_file, self)        
         
        self.definirServos = DefinirServos()
        self.arduino = Arduino()
        self.servos = Servos()
        self.voz= Voz()
         
        # Inicialización de la conexión serial
        self.arduino_port_izquierda=self.arduino.arduinoPuertoIzq
        self.baud_rate_izq=self.arduino.arduinoBaudiosIzq
        self.arduino_izq = serial.Serial(self.arduino.arduino_port_izquierda, self.arduino.baud_rate_izq)
        time.sleep(2)  # Esperar a que se establezca la conexión            
                    
        self.texto_a_convertir = "Esto, es una prueba del sistema de voz, del robot en español."                    
                    
        # Datos servos boca
        self.bocaPin=self.definirServos.bocaPin
        self.bocaMinimo=self.definirServos.bocaMinimo
        self.bocaMaximo=self.definirServos.bocaMaximo
        self.bocaInicio=self.definirServos.bocaInicio
        self.bocaRetraso=self.definirServos.bocaRetraso
        
        #Iniciar cabeza
        self.servos.iniciarServoIzq(self.bocaPin,self.bocaInicio,self.bocaRetraso)       
        
        self.bocaProgressBar.hide()
        
        self.setWindowTitle("Boca")

        # Botones de la barra superior
        self.click_posicion = QPoint()
        self.bt_close_boca.clicked.connect(lambda: self.close())
        self.bt_minimize_boca.clicked.connect(lambda: self.showMinimized())
    
        # Eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Sliders
        self.bocaSlider.setMinimum(self.bocaMinimo)
        self.bocaSlider.setMaximum(self.bocaMaximo)
        self.boca_valor.setText(str(self.bocaInicio))
        self.bocaSlider.setValue(self.bocaInicio)
        self.etiquetaBocaPin.setText(self.bocaPin)
        self.etiquetaBocaMinimo.setText(str(self.bocaMinimo))
        self.etiquetaBocaMedio.setText(str(int(self.bocaMaximo/2)))
        self.etiquetaBocaMaximo.setText(str(self.bocaMaximo))
        self.bocaSlider.valueChanged.connect(self.bocaSliderPwm)
        self.valorVelocidadBoca=self.bocaSpinBox.value()        
        self.bocaSpinBox.valueChanged.connect(self.bocaSpinBoxPwm)
        
        # Botones
        self.bocaOnOff.clicked.connect(self.bocaOnOffPwm)
        self.bocaBucle.clicked.connect(self.bocaBuclePwm)
        self.bocaPushButton.clicked.connect(self.bocaPushButtonPwm)        
        self.pushButtonVoz.clicked.connect(self.textoDeVoz)
        

    def textoDeVoz(self):
        self.pushButtonVoz.setText('Procesando la Voz')
        QApplication.processEvents()
        texto = "Esto, es una prueba del sistema de voz, del robot en español."
        self.voz.procesarVoz(texto)
        self.pushButtonVoz.setText('Prueba de Voz')
        QApplication.processEvents()

    def bocaSpinBoxPwm(self, value):       
        self.valorVelocidadBoca = value;
        
    def bocaSliderPwm(self, value):
        self.valorEsperaBoca=self.definirServos.convertirVelocidadValor(self.valorVelocidadBoca)                
        self.boca_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.bocaPin},{value},0,0,0,{self.valorEsperaBoca}\n")
        
    def bocaPushButtonPwm(self):
        self.bocaProgressBar.show()
        self.bocaOnOff.setChecked(True)            
        self.etiquetaBocaOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaBocaOnOff.setText(str('ON'))
        self.valorEsperaBoca=self.definirServos.convertirVelocidadValor(self.valorVelocidadBoca)
        self.boca_valor.setText(str(self.bocaInicio))
        self.bocaSlider.setValue(self.bocaInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.bocaPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.bocaPin},{self.bocaInicio},0,0,0,{self.valorEsperaBoca}\n")               
        time.sleep(self.valorVelocidadBoca/3)
        self.bocaOnOff.setChecked(False)            
        self.etiquetaBocaOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaBocaOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.bocaPin},0,0,0,0,0\n")
        self.bocaProgressBar.hide()
    
    def bocaOnOffPwm(self):        
        if self.bocaOnOff.isChecked()==True:
            self.etiquetaBocaOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaBocaOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.bocaPin},0,0,0,0,0\n")
        else:
            self.etiquetaBocaOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaBocaOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.bocaPin},0,0,0,0,0\n") 
       
    def bocaBuclePwm(self):        
        if self.bocaBucle.isChecked()==True:
            self.etiquetaBocaBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaBocaBucle.setText(str('ON'))
            self.bocaSlider.setEnabled(False)
            self.bocaOnOff.setChecked(True)
            self.etiquetaBocaOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaBocaOnOff.setText(str('ON'))          
            self.bocaOnOff.setEnabled(False)            
            self.enviar_comando(f"4,{self.bocaPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaBoca=self.definirServos.convertirVelocidadValor(self.valorVelocidadBoca)
            self.enviar_comando(f"6,{self.bocaPin},{self.bocaMinimo},{self.bocaMaximo},{self.bocaInicio},{self.bocaRetraso},{self.valorEsperaBoca}\n")
        else:
            self.etiquetaBocaBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaBocaBucle.setText(str('OFF'))
            self.bocaSlider.setEnabled(True)
            self.bocaOnOff.setChecked(False)
            self.etiquetaBocaOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaBocaOnOff.setText(str('OFF'))
            self.bocaOnOff.setEnabled(True)
            self.enviar_comando(f"S")
            
    def enviar_comando(self, comando):
        self.arduino_izq.write(comando.encode())
        print(f"Comando enviado: {comando}")           
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = Boca()
    my_app.show()
    sys.exit(app.exec_())
