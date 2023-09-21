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

class BrazoIzquierdo(QMainWindow):
    def __init__(self):
        super(BrazoIzquierdo,self).__init__()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, "brazoIzquierdo.ui")
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
        self.munecaIzqPin=self.definirServos.munecaIzqPin
        self.munecaIzqMinimo=self.definirServos.munecaIzqMinimo
        self.munecaIzqMaximo=self.definirServos.munecaIzqMaximo
        self.munecaIzqInicio=self.definirServos.munecaIzqInicio
        self.munecaIzqRetraso=self.definirServos.munecaIzqRetraso
        self.antebrazoIzqPin=self.definirServos.antebrazoIzqPin
        self.antebrazoIzqMinimo=self.definirServos.antebrazoIzqMinimo
        self.antebrazoIzqMaximo=self.definirServos.antebrazoIzqMaximo
        self.antebrazoIzqInicio=self.definirServos.antebrazoIzqInicio
        self.antebrazoIzqRetraso=self.definirServos.antebrazoIzqRetraso
        self.brazoIzqPin=self.definirServos.brazoIzqPin
        self.brazoIzqMinimo=self.definirServos.brazoIzqMinimo
        self.brazoIzqMaximo=self.definirServos.brazoIzqMaximo
        self.brazoIzqInicio=self.definirServos.brazoIzqInicio
        self.brazoIzqRetraso=self.definirServos.brazoIzqRetraso
        self.rotacionIzqPin=self.definirServos.rotacionIzqPin
        self.rotacionIzqMinimo=self.definirServos.rotacionIzqMinimo
        self.rotacionIzqMaximo=self.definirServos.rotacionIzqMaximo
        self.rotacionIzqInicio=self.definirServos.rotacionIzqInicio
        self.rotacionIzqRetraso=self.definirServos.rotacionIzqRetraso
        self.omoplatoIzqPin=self.definirServos.omoplatoIzqPin
        self.omoplatoIzqMinimo=self.definirServos.omoplatoIzqMinimo
        self.omoplatoIzqMaximo=self.definirServos.omoplatoIzqMaximo
        self.omoplatoIzqInicio=self.definirServos.omoplatoIzqInicio
        self.omoplatoIzqRetraso=self.definirServos.omoplatoIzqRetraso            
        
        #Iniciar dedos
        self.servos.iniciarServoIzq(self.munecaIzqPin,self.munecaIzqInicio,self.munecaIzqRetraso)
        self.servos.iniciarServoIzq(self.antebrazoIzqPin,self.antebrazoIzqInicio,self.antebrazoIzqRetraso)
        self.servos.iniciarServoIzq(self.brazoIzqPin,self.brazoIzqInicio,self.brazoIzqRetraso)
        self.servos.iniciarServoIzq(self.rotacionIzqPin,self.rotacionIzqInicio,self.rotacionIzqRetraso)
        self.servos.iniciarServoIzq(self.omoplatoIzqPin,self.omoplatoIzqInicio,self.omoplatoIzqRetraso)
        
        self.brazoIzqProgressBar.hide()
        
        self.setWindowTitle("Brazo Izquierdo")

        # Botones de la barra superior
        self.click_posicion = QPoint()
        self.bt_close_brazo_izq.clicked.connect(lambda: self.close())
        self.bt_minimize_brazo_izq.clicked.connect(lambda: self.showMinimized())
    

        # Eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Sliders
        self.munecaSlider.setMinimum(self.munecaIzqMinimo)
        self.munecaSlider.setMaximum(self.munecaIzqMaximo)
        self.muneca_valor.setText(str(self.munecaIzqInicio))
        self.munecaSlider.setValue(self.munecaIzqInicio)
        self.etiquetaMunecaPin.setText(self.munecaIzqPin)
        self.etiquetaMunecaMinimo.setText(str(self.munecaIzqMinimo))
        self.etiquetaMunecaMedio.setText(str(int(self.munecaIzqMaximo/2)))
        self.etiquetaMunecaMaximo.setText(str(self.munecaIzqMaximo))
        self.munecaSlider.valueChanged.connect(self.munecaSliderPwm)
        self.valorVelocidadMuneca=self.munecaSpinBox.value()        
        self.munecaSpinBox.valueChanged.connect(self.munecaSpinBoxPwm)
        
        self.antebrazoSlider.setMinimum(self.antebrazoIzqMinimo)
        self.antebrazoSlider.setMaximum(self.antebrazoIzqMaximo)
        self.antebrazo_valor.setText(str(self.antebrazoIzqMinimo))
        self.etiquetaAntebrazoPin.setText(self.antebrazoIzqPin)
        self.etiquetaAntebrazoMinimo.setText(str(self.antebrazoIzqMinimo))
        self.etiquetaAntebrazoMedio.setText(str(int(self.antebrazoIzqMaximo/2)))
        self.etiquetaAntebrazoMaximo.setText(str(self.antebrazoIzqMaximo))
        self.antebrazoSlider.valueChanged.connect(self.antebrazoSliderPwm)
        self.valorVelocidadAntebrazo=self.antebrazoSpinBox.value()        
        self.antebrazoSpinBox.valueChanged.connect(self.antebrazoSpinBoxPwm)
        
        self.brazoSlider.setMinimum(self.brazoIzqMinimo)
        self.brazoSlider.setMaximum(self.brazoIzqMaximo)
        self.brazo_valor.setText(str(self.brazoIzqInicio))
        self.brazoSlider.setValue(self.brazoIzqInicio)
        self.etiquetaBrazoPin.setText(self.brazoIzqPin)
        self.etiquetaBrazoMinimo.setText(str(self.brazoIzqMinimo))
        self.etiquetaBrazoMedio.setText(str(int(self.brazoIzqMaximo/2)))
        self.etiquetaBrazoMaximo.setText(str(self.brazoIzqMaximo))
        self.brazoSlider.valueChanged.connect(self.brazoSliderPwm)
        self.valorVelocidadBrazo=self.brazoSpinBox.value()        
        self.brazoSpinBox.valueChanged.connect(self.brazoSpinBoxPwm)
        
        self.rotacionSlider.setMinimum(self.rotacionIzqMinimo)
        self.rotacionSlider.setMaximum(self.rotacionIzqMaximo)
        self.rotacion_valor.setText(str(self.rotacionIzqInicio))
        self.rotacionSlider.setValue(self.rotacionIzqInicio)
        self.etiquetaRotacionPin.setText(self.rotacionIzqPin)
        self.etiquetaRotacionMinimo.setText(str(self.rotacionIzqMinimo))
        self.etiquetaRotacionMedio.setText(str(int(self.rotacionIzqMaximo/2)))
        self.etiquetaRotacionMaximo.setText(str(self.rotacionIzqMaximo))
        self.rotacionSlider.valueChanged.connect(self.rotacionSliderPwm)
        self.valorVelocidadRotacion=self.rotacionSpinBox.value()        
        self.rotacionSpinBox.valueChanged.connect(self.rotacionSpinBoxPwm)
        
        self.omoplatoSlider.setMinimum(self.omoplatoIzqMinimo)
        self.omoplatoSlider.setMaximum(self.omoplatoIzqMaximo)
        self.omoplato_valor.setText(str(self.omoplatoIzqMinimo))
        self.etiquetaOmoplatoPin.setText(self.omoplatoIzqPin)
        self.etiquetaOmoplatoMinimo.setText(str(self.omoplatoIzqMinimo))
        self.etiquetaOmoplatoMedio.setText(str(int(self.omoplatoIzqMaximo/2)))
        self.etiquetaOmoplatoMaximo.setText(str(self.omoplatoIzqMaximo))
        self.omoplatoSlider.valueChanged.connect(self.omoplatoSliderPwm)
        self.valorVelocidadOmoplato=self.omoplatoSpinBox.value()        
        self.omoplatoSpinBox.valueChanged.connect(self.omoplatoSpinBoxPwm)            
        
        # Botones
        self.munecaOnOff.clicked.connect(self.munecaOnOffPwm)
        self.munecaBucle.clicked.connect(self.munecaBuclePwm)
        self.munecaPushButton.clicked.connect(self.munecaPushButtonPwm)   
        self.antebrazoOnOff.clicked.connect(self.antebrazoOnOffPwm)
        self.antebrazoBucle.clicked.connect(self.antebrazoBuclePwm)
        self.antebrazoPushButton.clicked.connect(self.antebrazoPushButtonPwm)
        self.brazoOnOff.clicked.connect(self.brazoOnOffPwm)
        self.brazoBucle.clicked.connect(self.brazoBuclePwm)
        self.brazoPushButton.clicked.connect(self.brazoPushButtonPwm)        
        self.rotacionOnOff.clicked.connect(self.rotacionOnOffPwm)
        self.rotacionBucle.clicked.connect(self.rotacionBuclePwm)
        self.rotacionPushButton.clicked.connect(self.rotacionPushButtonPwm)   
        self.omoplatoOnOff.clicked.connect(self.omoplatoOnOffPwm)
        self.omoplatoBucle.clicked.connect(self.omoplatoBuclePwm)        
        self.omoplatoPushButton.clicked.connect(self.omoplatoPushButtonPwm)            

    def munecaSpinBoxPwm(self, value):       
        self.valorVelocidadMuneca = value;
        
    def munecaSliderPwm(self, value):
        self.valorEsperaMuneca=self.definirServos.convertirVelocidadValor(self.valorVelocidadMuneca)                
        self.muneca_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.munecaIzqPin},{value},0,0,0,{self.valorEsperaMuneca}\n")
        
    def munecaPushButtonPwm(self):
        self.brazoIzqProgressBar.show()
        self.munecaOnOff.setChecked(True)            
        self.etiquetaMunecaOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaMunecaOnOff.setText(str('ON'))
        self.valorEsperaMuneca=self.definirServos.convertirVelocidadValor(self.valorVelocidadMuneca)
        self.muneca_valor.setText(str(self.munecaIzqInicio))
        self.munecaSlider.setValue(self.munecaIzqInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.munecaIzqPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.munecaIzqPin},{self.munecaIzqInicio},0,0,0,{self.valorEsperaMuneca}\n")               
        time.sleep(self.valorVelocidadMuneca)
        self.munecaOnOff.setChecked(False)            
        self.etiquetaMunecaOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaMunecaOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.munecaIzqPin},0,0,0,0,0\n")
        self.brazoIzqProgressBar.hide()
    
    def munecaOnOffPwm(self):        
        if self.munecaOnOff.isChecked()==True:
            self.etiquetaMunecaOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMunecaOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.munecaIzqPin},0,0,0,0,0\n")
        else:
            self.etiquetaMunecaOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMunecaOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.munecaIzqPin},0,0,0,0,0\n") 
       
    def munecaBuclePwm(self):        
        if self.munecaBucle.isChecked()==True:
            self.etiquetaMunecaBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMunecaBucle.setText(str('ON'))
            self.munecaSlider.setEnabled(False)
            self.munecaSpinBox.setEnabled(False)
            self.munecaPushButton.setEnabled(False)
            self.munecaOnOff.setChecked(True)
            self.etiquetaMunecaOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMunecaOnOff.setText(str('ON'))          
            self.munecaOnOff.setEnabled(False)            
            self.Deshabilitar_antebrazo()
            self.Deshabilitar_brazo()
            self.Deshabilitar_rotacion()
            self.Deshabilitar_omoplato()
            self.enviar_comando(f"4,{self.munecaIzqPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaMuneca=self.definirServos.convertirVelocidadValor(self.valorVelocidadMuneca)
            self.enviar_comando(f"6,{self.munecaIzqPin},{self.munecaIzqMinimo},{self.munecaIzqMaximo},0,{self.munecaIzqRetraso},{self.valorEsperaMuneca}\n")
        else:
            self.etiquetaMunecaBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMunecaBucle.setText(str('OFF'))
            self.munecaSlider.setEnabled(True)
            self.munecaSpinBox.setEnabled(True)
            self.munecaPushButton.setEnabled(True)
            self.munecaOnOff.setChecked(False)
            self.etiquetaMunecaOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMunecaOnOff.setText(str('OFF'))
            self.munecaOnOff.setEnabled(True)
            self.Habilitar_antebrazo()        
            self.Habilitar_brazo()
            self.Habilitar_rotacion()
            self.Habilitar_omoplato()
            self.enviar_comando(f"S")

    def antebrazoSpinBoxPwm(self, value):       
        self.valorVelocidadAntebrazo = value;        

    def antebrazoSliderPwm(self, value):
        self.valorEsperaAntebrazo=self.definirServos.convertirVelocidadValor(self.valorVelocidadAntebrazo)        
        self.antebrazo_valor.setText(str(value))
        self.enviar_comando(f"1,{self.antebrazoIzqPin},{value},0,0,0,{self.valorEsperaAntebrazo}\n")        
        
    def antebrazoPushButtonPwm(self):
        self.brazoIzqProgressBar.show()
        self.antebrazoOnOff.setChecked(True)            
        self.etiquetaAntebrazoOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaAntebrazoOnOff.setText(str('ON')) 
        self.valorEsperaAntebrazo=self.definirServos.convertirVelocidadValor(self.valorVelocidadAntebrazo)
        self.antebrazo_valor.setText(str(self.antebrazoIzqInicio))
        self.antebrazoSlider.setValue(self.antebrazoIzqInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.antebrazoIzqPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.antebrazoIzqPin},{self.antebrazoIzqInicio},0,0,0,{self.valorEsperaAntebrazo}\n")        
        if self.valorVelocidadAntebrazo==1:
            time.sleep(self.valorVelocidadAntebrazo/0.7)             
        elif self.valorVelocidadAntebrazo==2:
            time.sleep(self.valorVelocidadAntebrazo/0.8)
        elif self.valorVelocidadAntebrazo==3:
            time.sleep(self.valorVelocidadAntebrazo/1)            
        else:
            time.sleep(self.valorVelocidadAntebrazo)
        self.antebrazoOnOff.setChecked(False)            
        self.etiquetaAntebrazoOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaAntebrazoOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.antebrazoIzqPin},0,0,0,0,0\n")
        self.brazoIzqProgressBar.hide()
        
    def antebrazoOnOffPwm(self):        
        if self.antebrazoOnOff.isChecked()==True:
            self.etiquetaAntebrazoOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaAntebrazoOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.antebrazoIzqPin},0,0,0,0,0\n")
        else:
            self.etiquetaAntebrazoOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaAntebrazoOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.antebrazoIzqPin},0,0,0,0,0\n")         

    def antebrazoBuclePwm(self):        
        if self.antebrazoBucle.isChecked()==True:
            self.etiquetaAntebrazoBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaAntebrazoBucle.setText(str('ON'))
            self.antebrazoSlider.setEnabled(False)
            self.antebrazoSpinBox.setEnabled(False)
            self.antebrazoPushButton.setEnabled(False)
            self.antebrazoOnOff.setChecked(True)
            self.etiquetaAntebrazoOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaAntebrazoOnOff.setText(str('ON'))          
            self.antebrazoOnOff.setEnabled(False)
            self.Deshabilitar_muneca()   
            self.Deshabilitar_brazo()
            self.Deshabilitar_rotacion()
            self.Deshabilitar_omoplato()   
            self.enviar_comando(f"4,{self.antebrazoIzqPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaAntebrazo=self.definirServos.convertirVelocidadValor(self.valorVelocidadAntebrazo)
            self.enviar_comando(f"6,{self.antebrazoIzqPin},{self.antebrazoIzqMinimo},{self.antebrazoIzqMaximo},{self.munecaIzqInicio},{self.antebrazoIzqRetraso},{self.valorEsperaAntebrazo}\n")
        else:
            self.etiquetaAntebrazoBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaAntebrazoBucle.setText(str('OFF'))
            self.antebrazoSlider.setEnabled(True)
            self.antebrazoSpinBox.setEnabled(True)
            self.antebrazoPushButton.setEnabled(True)
            self.antebrazoOnOff.setChecked(False)
            self.etiquetaAntebrazoOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaAntebrazoOnOff.setText(str('OFF'))
            self.antebrazoOnOff.setEnabled(True)
            self.Habilitar_muneca()
            self.Habilitar_brazo()
            self.Habilitar_rotacion()
            self.Habilitar_omoplato()
            self.enviar_comando(f"S")   

    def brazoSpinBoxPwm(self, value):       
        self.valorVelocidadBrazo = value;        

    def brazoSliderPwm(self, value):
        self.valorEsperaBrazo=self.definirServos.convertirVelocidadValor(self.valorVelocidadBrazo)        
        self.brazo_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.brazoIzqPin},{value},0,0,0,{self.valorEsperaBrazo}\n")

    def brazoPushButtonPwm(self):
        self.brazoIzqProgressBar.show()
        self.brazoOnOff.setChecked(True)            
        self.etiquetaBrazoOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaBrazoOnOff.setText(str('ON'))
        self.valorEsperaBrazo=self.definirServos.convertirVelocidadValor(self.valorVelocidadBrazo)
        self.brazo_valor.setText(str(self.brazoIzqInicio))
        self.brazoSlider.setValue(self.brazoIzqInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.brazoIzqPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.brazoIzqPin},{self.brazoIzqInicio},0,0,0,{self.valorEsperaBrazo}\n")        
        if self.valorVelocidadBrazo==1:
            time.sleep(self.valorVelocidadBrazo/0.2)             
        elif self.valorVelocidadBrazo==2:
            time.sleep(self.valorVelocidadBrazo/0.4)
        elif self.valorVelocidadBrazo==3:
            time.sleep(self.valorVelocidadBrazo/0.6)
        elif self.valorVelocidadBrazo==4:
            time.sleep(self.valorVelocidadBrazo/0.8)
        elif self.valorVelocidadBrazo==5:
            time.sleep(self.valorVelocidadBrazo/0.8)             
        else:
            time.sleep(self.valorVelocidadBrazo)
        self.brazoOnOff.setChecked(False)            
        self.etiquetaBrazoOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaBrazoOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.brazoIzqPin},0,0,0,0,0\n")
        self.brazoIzqProgressBar.hide()

    def brazoOnOffPwm(self):        
        if self.brazoOnOff.isChecked()==True:
            self.etiquetaBrazoOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaBrazoOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.brazoIzqPin},0,0,0,0,0\n")
        else:
            self.etiquetaBrazoOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaBrazoOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.brazoIzqPin},0,0,0,0,0\n") 
       
    def brazoBuclePwm(self):        
        if self.brazoBucle.isChecked()==True:
            self.etiquetaBrazoBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaBrazoBucle.setText(str('ON'))
            self.brazoSlider.setEnabled(False)
            self.brazoSpinBox.setEnabled(False)
            self.brazoPushButton.setEnabled(False)
            self.brazoOnOff.setChecked(True)
            self.etiquetaBrazoOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaBrazoOnOff.setText(str('ON'))          
            self.brazoOnOff.setEnabled(False)
            self.Deshabilitar_muneca()
            self.Deshabilitar_antebrazo()
            self.Deshabilitar_rotacion()
            self.Deshabilitar_omoplato()
            self.enviar_comando(f"4,{self.brazoIzqPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaBrazo=self.definirServos.convertirVelocidadValor(self.valorVelocidadBrazo)
            self.enviar_comando(f"6,{self.brazoIzqPin},{self.brazoIzqMinimo},{self.brazoIzqMaximo},{self.brazoIzqInicio},{self.brazoIzqRetraso},{self.valorEsperaBrazo}\n")
        else:
            self.etiquetaBrazoBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaBrazoBucle.setText(str('OFF'))
            self.brazoSlider.setEnabled(True)
            self.brazoSpinBox.setEnabled(True)
            self.brazoPushButton.setEnabled(True)
            self.brazoOnOff.setChecked(False)
            self.etiquetaBrazoOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaBrazoOnOff.setText(str('OFF'))
            self.brazoOnOff.setEnabled(True)
            self.Habilitar_muneca()
            self.Habilitar_antebrazo()
            self.Habilitar_rotacion()
            self.Habilitar_omoplato()
            self.enviar_comando(f"S")

    def rotacionSpinBoxPwm(self, value):       
        self.valorVelocidadRotacion = value;
        
    def rotacionSliderPwm(self, value):
        self.valorEsperaRotacion=self.definirServos.convertirVelocidadValor(self.valorVelocidadRotacion)
        self.rotacion_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.rotacionIzqPin},{value},0,0,0,{self.valorEsperaRotacion}\n")

    def rotacionPushButtonPwm(self):
        self.brazoIzqProgressBar.show()
        self.rotacionOnOff.setChecked(True)            
        self.etiquetaRotacionOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaRotacionOnOff.setText(str('ON')) 
        self.valorEsperaRotacion=self.definirServos.convertirVelocidadValor(self.valorVelocidadRotacion)
        self.rotacion_valor.setText(str(self.rotacionIzqInicio))
        self.rotacionSlider.setValue(self.rotacionIzqInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.rotacionIzqPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.rotacionIzqPin},{self.rotacionIzqInicio},0,0,0,{self.valorEsperaRotacion}\n")        
        if self.valorVelocidadRotacion==1:
            time.sleep(self.valorVelocidadRotacion/0.5)             
        elif self.valorVelocidadRotacion==2:
            time.sleep(self.valorVelocidadRotacion/1)
        elif self.valorVelocidadRotacion==3:
            time.sleep(self.valorVelocidadRotacion/1.3)
        else:
            time.sleep(self.valorVelocidadRotacion)
        self.rotacionOnOff.setChecked(False)            
        self.etiquetaRotacionOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaRotacionOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.rotacionIzqPin},0,0,0,0,0\n")
        self.brazoIzqProgressBar.hide()

    def rotacionOnOffPwm(self):        
        if self.rotacionOnOff.isChecked()==True:
            self.etiquetaRotacionOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaRotacionOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.rotacionIzqPin},0,0,0,0,0\n")
        else:
            self.etiquetaRotacionOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaRotacionOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.rotacionIzqPin},0,0,0,0,0\n") 
       
    def rotacionBuclePwm(self):        
        if self.rotacionBucle.isChecked()==True:
            self.etiquetaRotacionBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaRotacionBucle.setText(str('ON'))
            self.rotacionSlider.setEnabled(False)
            self.rotacionSpinBox.setEnabled(False)
            self.rotacionPushButton.setEnabled(False)
            self.rotacionOnOff.setChecked(True)
            self.etiquetaRotacionOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaRotacionOnOff.setText(str('ON'))          
            self.rotacionOnOff.setEnabled(False)
            self.Deshabilitar_muneca()
            self.Deshabilitar_antebrazo()
            self.Deshabilitar_brazo()
            self.Deshabilitar_omoplato() 
            self.enviar_comando(f"4,{self.rotacionIzqPin},0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaRotacion=self.definirServos.convertirVelocidadValor(self.valorVelocidadRotacion)
            self.enviar_comando(f"6,{self.rotacionIzqPin},{self.rotacionIzqMinimo},{self.rotacionIzqMaximo},{self.rotacionIzqInicio},{self.rotacionIzqRetraso},{self.valorEsperaRotacion}\n")
        else:
            self.etiquetaRotacionBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaRotacionBucle.setText(str('OFF'))
            self.rotacionSlider.setEnabled(True)
            self.rotacionSpinBox.setEnabled(True)
            self.rotacionPushButton.setEnabled(True)
            self.rotacionOnOff.setChecked(False)
            self.etiquetaRotacionOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaRotacionOnOff.setText(str('OFF'))
            self.rotacionOnOff.setEnabled(True)
            self.Habilitar_muneca()
            self.Habilitar_antebrazo()
            self.Habilitar_brazo()
            self.Habilitar_omoplato()
            self.enviar_comando(f"S")

    def omoplatoSpinBoxPwm(self, value):       
        self.valorVelocidadOmoplato = value;

    def omoplatoSliderPwm(self, value):
        self.valorEsperaOmoplato=self.definirServos.convertirVelocidadValor(self.valorVelocidadOmoplato)
        self.omoplato_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.omoplatoIzqPin},{value},0,0,0,{self.valorEsperaOmoplato}\n")
        
    def omoplatoPushButtonPwm(self):
        self.brazoIzqProgressBar.show()
        self.omoplatoOnOff.setChecked(True)            
        self.etiquetaOmoplatoOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaOmoplatoOnOff.setText(str('ON')) 
        self.valorEsperaOmoplato=self.definirServos.convertirVelocidadValor(self.valorVelocidadOmoplato)
        self.omoplato_valor.setText(str(self.omoplatoIzqInicio))
        self.omoplatoSlider.setValue(self.omoplatoIzqInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.omoplatoIzqPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.omoplatoIzqPin},{self.omoplatoIzqInicio},0,0,0,{self.valorEsperaOmoplato}\n")        
        if self.valorVelocidadOmoplato==1:
            time.sleep(self.valorVelocidadOmoplato/0.5)             
        elif self.valorVelocidadOmoplato==2:
            time.sleep(self.valorVelocidadOmoplato/1)
        elif self.valorVelocidadOmoplato==3:
            time.sleep(self.valorVelocidadOmoplato/1.3)
        else:
            time.sleep(self.valorVelocidadOmoplato)
        self.omoplatoOnOff.setChecked(False)            
        self.etiquetaOmoplatoOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaOmoplatoOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.omoplatoIzqPin},0,0,0,0,0\n")
        self.brazoIzqProgressBar.hide()
    
    def omoplatoOnOffPwm(self):        
        if self.omoplatoOnOff.isChecked()==True:
            self.etiquetaOmoplatoOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaOmoplatoOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.omoplatoIzqPin},0,0,0,0,0\n")
        else:
            self.etiquetaOmoplatoOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaOmoplatoOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.omoplatoIzqPin},0,0,0,0,0\n") 
       
    def omoplatoBuclePwm(self):        
        if self.omoplatoBucle.isChecked()==True:
            self.etiquetaOmoplatoBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaOmoplatoBucle.setText(str('ON'))
            self.omoplatoSlider.setEnabled(False)
            self.omoplatoSpinBox.setEnabled(False)
            self.omoplatoPushButton.setEnabled(False)
            self.omoplatoOnOff.setChecked(True)
            self.etiquetaOmoplatoOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaOmoplatoOnOff.setText(str('ON'))          
            self.omoplatoOnOff.setEnabled(False)
            self.Deshabilitar_muneca()
            self.Deshabilitar_antebrazo()
            self.Deshabilitar_brazo()
            self.Deshabilitar_rotacion() 
            self.enviar_comando(f"4,{self.omoplatoIzqPin},0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaOmoplato=self.definirServos.convertirVelocidadValor(self.valorVelocidadOmoplato)
            self.enviar_comando(f"6,{self.omoplatoIzqPin},{self.omoplatoIzqMinimo},{self.omoplatoIzqMaximo},{self.omoplatoIzqInicio},{self.omoplatoIzqRetraso},{self.valorEsperaOmoplato}\n")
        else:
            self.etiquetaOmoplatoBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaOmoplatoBucle.setText(str('OFF'))
            self.omoplatoSlider.setEnabled(True)
            self.omoplatoSpinBox.setEnabled(True)
            self.omoplatoPushButton.setEnabled(True)
            self.omoplatoOnOff.setChecked(False)
            self.etiquetaOmoplatoOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaOmoplatoOnOff.setText(str('OFF'))
            self.omoplatoOnOff.setEnabled(True)
            self.Habilitar_muneca()
            self.Habilitar_antebrazo()
            self.Habilitar_brazo()
            self.Habilitar_rotacion()
            self.enviar_comando(f"S")


    def enviar_comando(self, comando):
        self.arduino_izq.write(comando.encode())
        print(f"Comando enviado: {comando}")           
        
    def Deshabilitar_muneca(self):
        self.munecaSlider.setEnabled(False)
        self.munecaOnOff.setEnabled(False)
        self.munecaBucle.setEnabled(False)
        self.munecaSpinBox.setEnabled(False)
        self.munecaPushButton.setEnabled(False)
          
    def Deshabilitar_antebrazo(self):
        self.antebrazoSlider.setEnabled(False)
        self.antebrazoOnOff.setEnabled(False)
        self.antebrazoBucle.setEnabled(False)
        self.antebrazoSpinBox.setEnabled(False)
        self.antebrazoPushButton.setEnabled(False)
          
    def Deshabilitar_brazo(self):
        self.brazoSlider.setEnabled(False)
        self.brazoOnOff.setEnabled(False)
        self.brazoBucle.setEnabled(False)
        self.brazoSpinBox.setEnabled(False)
        self.brazoPushButton.setEnabled(False)
        
    def Deshabilitar_rotacion(self):
        self.rotacionSlider.setEnabled(False)
        self.rotacionOnOff.setEnabled(False)
        self.rotacionBucle.setEnabled(False)
        self.rotacionSpinBox.setEnabled(False)
        self.rotacionPushButton.setEnabled(False)
        
    def Deshabilitar_omoplato(self):
        self.omoplatoSlider.setEnabled(False)
        self.omoplatoOnOff.setEnabled(False)
        self.omoplatoBucle.setEnabled(False)
        self.omoplatoSpinBox.setEnabled(False)
        self.omoplatoPushButton.setEnabled(False)
          
    def Habilitar_muneca(self):
        self.munecaSlider.setEnabled(True)
        self.munecaOnOff.setEnabled(True)
        self.munecaBucle.setEnabled(True)
        self.munecaSpinBox.setEnabled(True)
        self.munecaPushButton.setEnabled(True)
        
    def Habilitar_antebrazo(self):
        self.antebrazoSlider.setEnabled(True)
        self.antebrazoOnOff.setEnabled(True)
        self.antebrazoBucle.setEnabled(True)
        self.antebrazoSpinBox.setEnabled(True)
        self.antebrazoPushButton.setEnabled(True)
        
    def Habilitar_brazo(self):
        self.brazoSlider.setEnabled(True)
        self.brazoOnOff.setEnabled(True)
        self.brazoBucle.setEnabled(True)
        self.brazoSpinBox.setEnabled(True)
        self.brazoPushButton.setEnabled(True)
        
    def Habilitar_rotacion(self):
        self.rotacionSlider.setEnabled(True)
        self.rotacionOnOff.setEnabled(True)
        self.rotacionBucle.setEnabled(True)
        self.rotacionSpinBox.setEnabled(True)
        self.rotacionPushButton.setEnabled(True)

    def Habilitar_omoplato(self):
        self.omoplatoSlider.setEnabled(True)
        self.omoplatoOnOff.setEnabled(True)
        self.omoplatoBucle.setEnabled(True)
        self.omoplatoSpinBox.setEnabled(True)
        self.omoplatoPushButton.setEnabled(True)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = BrazoIzquierdo()
    my_app.show()
    sys.exit(app.exec_())
