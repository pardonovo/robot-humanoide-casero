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

class BrazoDerecho(QMainWindow):
    def __init__(self):
        super(BrazoDerecho,self).__init__()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, "brazoDerecho.ui")
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
        self.munecaDerPin=self.definirServos.munecaDerPin
        self.munecaDerMinimo=self.definirServos.munecaDerMinimo
        self.munecaDerMaximo=self.definirServos.munecaDerMaximo
        self.munecaDerInicio=self.definirServos.munecaDerInicio
        self.munecaDerRetraso=self.definirServos.munecaDerRetraso
        self.antebrazoDerPin=self.definirServos.antebrazoDerPin
        self.antebrazoDerMinimo=self.definirServos.antebrazoDerMinimo
        self.antebrazoDerMaximo=self.definirServos.antebrazoDerMaximo
        self.antebrazoDerInicio=self.definirServos.antebrazoDerInicio
        self.antebrazoDerRetraso=self.definirServos.antebrazoDerRetraso
        self.brazoDerPin=self.definirServos.brazoDerPin
        self.brazoDerMinimo=self.definirServos.brazoDerMinimo
        self.brazoDerMaximo=self.definirServos.brazoDerMaximo
        self.brazoDerInicio=self.definirServos.brazoDerInicio
        self.brazoDerRetraso=self.definirServos.brazoDerRetraso
        self.rotacionDerPin=self.definirServos.rotacionDerPin
        self.rotacionDerMinimo=self.definirServos.rotacionDerMinimo
        self.rotacionDerMaximo=self.definirServos.rotacionDerMaximo
        self.rotacionDerInicio=self.definirServos.rotacionDerInicio
        self.rotacionDerRetraso=self.definirServos.rotacionDerRetraso
        self.omoplatoDerPin=self.definirServos.omoplatoDerPin
        self.omoplatoDerMinimo=self.definirServos.omoplatoDerMinimo
        self.omoplatoDerMaximo=self.definirServos.omoplatoDerMaximo
        self.omoplatoDerInicio=self.definirServos.omoplatoDerInicio
        self.omoplatoDerRetraso=self.definirServos.omoplatoDerRetraso            
        
        #Iniciar dedos
        self.servos.iniciarServoDer(self.munecaDerPin,self.munecaDerInicio,self.munecaDerRetraso)
        self.servos.iniciarServoDer(self.antebrazoDerPin,self.antebrazoDerInicio,self.antebrazoDerRetraso)
        self.servos.iniciarServoDer(self.brazoDerPin,self.brazoDerInicio,self.brazoDerRetraso)
        self.servos.iniciarServoDer(self.rotacionDerPin,self.rotacionDerInicio,self.rotacionDerRetraso)
        self.servos.iniciarServoDer(self.omoplatoDerPin,self.omoplatoDerInicio,self.omoplatoDerRetraso)
        
        self.brazoDerProgressBar.hide()
        
        self.setWindowTitle("Brazo Derecho")

        # Botones de la barra superior
        self.click_posicion = QPoint()
        self.bt_close_brazo_der.clicked.connect(lambda: self.close())
        self.bt_minimize_brazo_der.clicked.connect(lambda: self.showMinimized())
    

        # Eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Sliders
        self.munecaSlider.setMinimum(self.munecaDerMinimo)
        self.munecaSlider.setMaximum(self.munecaDerMaximo)
        self.muneca_valor.setText(str(self.munecaDerInicio))
        self.munecaSlider.setValue(self.munecaDerInicio)
        self.etiquetaMunecaPin.setText(self.munecaDerPin)
        self.etiquetaMunecaMinimo.setText(str(self.munecaDerMinimo))
        self.etiquetaMunecaMedio.setText(str(int(self.munecaDerMaximo/2)))
        self.etiquetaMunecaMaximo.setText(str(self.munecaDerMaximo))
        self.munecaSlider.valueChanged.connect(self.munecaSliderPwm)
        self.valorVelocidadMuneca=self.munecaSpinBox.value()        
        self.munecaSpinBox.valueChanged.connect(self.munecaSpinBoxPwm)
        
        self.antebrazoSlider.setMinimum(self.antebrazoDerMinimo)
        self.antebrazoSlider.setMaximum(self.antebrazoDerMaximo)
        self.antebrazo_valor.setText(str(self.antebrazoDerMinimo))
        self.etiquetaAntebrazoPin.setText(self.antebrazoDerPin)
        self.etiquetaAntebrazoMinimo.setText(str(self.antebrazoDerMinimo))
        self.etiquetaAntebrazoMedio.setText(str(int(self.antebrazoDerMaximo/2)))
        self.etiquetaAntebrazoMaximo.setText(str(self.antebrazoDerMaximo))
        self.antebrazoSlider.valueChanged.connect(self.antebrazoSliderPwm)
        self.valorVelocidadAntebrazo=self.antebrazoSpinBox.value()        
        self.antebrazoSpinBox.valueChanged.connect(self.antebrazoSpinBoxPwm)
        
        self.brazoSlider.setMinimum(self.brazoDerMinimo)
        self.brazoSlider.setMaximum(self.brazoDerMaximo)
        self.brazo_valor.setText(str(self.brazoDerInicio))
        self.brazoSlider.setValue(self.brazoDerInicio)
        self.etiquetaBrazoPin.setText(self.brazoDerPin)
        self.etiquetaBrazoMinimo.setText(str(self.brazoDerMinimo))
        self.etiquetaBrazoMedio.setText(str(int(self.brazoDerMaximo/2)))
        self.etiquetaBrazoMaximo.setText(str(self.brazoDerMaximo))
        self.brazoSlider.valueChanged.connect(self.brazoSliderPwm)
        self.valorVelocidadBrazo=self.brazoSpinBox.value()        
        self.brazoSpinBox.valueChanged.connect(self.brazoSpinBoxPwm)
        
        self.rotacionSlider.setMinimum(self.rotacionDerMinimo)
        self.rotacionSlider.setMaximum(self.rotacionDerMaximo)
        self.rotacion_valor.setText(str(self.rotacionDerInicio))
        self.rotacionSlider.setValue(self.rotacionDerInicio)
        self.etiquetaRotacionPin.setText(self.rotacionDerPin)
        self.etiquetaRotacionMinimo.setText(str(self.rotacionDerMinimo))
        self.etiquetaRotacionMedio.setText(str(int(self.rotacionDerMaximo/2)))
        self.etiquetaRotacionMaximo.setText(str(self.rotacionDerMaximo))
        self.rotacionSlider.valueChanged.connect(self.rotacionSliderPwm)
        self.valorVelocidadRotacion=self.rotacionSpinBox.value()        
        self.rotacionSpinBox.valueChanged.connect(self.rotacionSpinBoxPwm)
        
        self.omoplatoSlider.setMinimum(self.omoplatoDerMinimo)
        self.omoplatoSlider.setMaximum(self.omoplatoDerMaximo)
        self.omoplato_valor.setText(str(self.omoplatoDerMinimo))
        self.etiquetaOmoplatoPin.setText(self.omoplatoDerPin)
        self.etiquetaOmoplatoMinimo.setText(str(self.omoplatoDerMinimo))
        self.etiquetaOmoplatoMedio.setText(str(int(self.omoplatoDerMaximo/2)))
        self.etiquetaOmoplatoMaximo.setText(str(self.omoplatoDerMaximo))
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
        self.enviar_comando(f"1,{self.munecaDerPin},{value},0,0,0,{self.valorEsperaMuneca}\n")
        
    def munecaPushButtonPwm(self):
        self.brazoDerProgressBar.show()
        self.munecaOnOff.setChecked(True)            
        self.etiquetaMunecaOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaMunecaOnOff.setText(str('ON'))
        self.valorEsperaMuneca=self.definirServos.convertirVelocidadValor(self.valorVelocidadMuneca)
        self.muneca_valor.setText(str(self.munecaDerInicio))
        self.munecaSlider.setValue(self.munecaDerInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.munecaDerPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.munecaDerPin},{self.munecaDerInicio},0,0,0,{self.valorEsperaMuneca}\n")               
        time.sleep(self.valorVelocidadMuneca)
        self.munecaOnOff.setChecked(False)            
        self.etiquetaMunecaOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaMunecaOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.munecaDerPin},0,0,0,0,0\n")
        self.brazoDerProgressBar.hide()
    
    def munecaOnOffPwm(self):        
        if self.munecaOnOff.isChecked()==True:
            self.etiquetaMunecaOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMunecaOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.munecaDerPin},0,0,0,0,0\n")
        else:
            self.etiquetaMunecaOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMunecaOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.munecaDerPin},0,0,0,0,0\n") 
       
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
            self.enviar_comando(f"4,{self.munecaDerPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaMuneca=self.definirServos.convertirVelocidadValor(self.valorVelocidadMuneca)
            self.enviar_comando(f"6,{self.munecaDerPin},{self.munecaDerMinimo},{self.munecaDerMaximo},0,{self.munecaDerRetraso},{self.valorEsperaMuneca}\n")
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
        self.enviar_comando(f"1,{self.antebrazoDerPin},{value},0,0,0,{self.valorEsperaAntebrazo}\n")        
        
    def antebrazoPushButtonPwm(self):
        self.brazoDerProgressBar.show()
        self.antebrazoOnOff.setChecked(True)            
        self.etiquetaAntebrazoOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaAntebrazoOnOff.setText(str('ON')) 
        self.valorEsperaAntebrazo=self.definirServos.convertirVelocidadValor(self.valorVelocidadAntebrazo)
        self.antebrazo_valor.setText(str(self.antebrazoDerInicio))
        self.antebrazoSlider.setValue(self.antebrazoDerInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.antebrazoDerPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.antebrazoDerPin},{self.antebrazoDerInicio},0,0,0,{self.valorEsperaAntebrazo}\n")        
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
        self.enviar_comando(f"3,{self.antebrazoDerPin},0,0,0,0,0\n")
        self.brazoDerProgressBar.hide()
        
    def antebrazoOnOffPwm(self):        
        if self.antebrazoOnOff.isChecked()==True:
            self.etiquetaAntebrazoOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaAntebrazoOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.antebrazoDerPin},0,0,0,0,0\n")
        else:
            self.etiquetaAntebrazoOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaAntebrazoOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.antebrazoDerPin},0,0,0,0,0\n")         

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
            self.enviar_comando(f"4,{self.antebrazoDerPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaAntebrazo=self.definirServos.convertirVelocidadValor(self.valorVelocidadAntebrazo)
            self.enviar_comando(f"6,{self.antebrazoDerPin},{self.antebrazoDerMinimo},{self.antebrazoDerMaximo},{self.munecaDerInicio},{self.antebrazoDerRetraso},{self.valorEsperaAntebrazo}\n")
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
        self.enviar_comando(f"1,{self.brazoDerPin},{value},0,0,0,{self.valorEsperaBrazo}\n")

    def brazoPushButtonPwm(self):
        self.brazoDerProgressBar.show()
        self.brazoOnOff.setChecked(True)            
        self.etiquetaBrazoOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaBrazoOnOff.setText(str('ON'))
        self.valorEsperaBrazo=self.definirServos.convertirVelocidadValor(self.valorVelocidadBrazo)
        self.brazo_valor.setText(str(self.brazoDerInicio))
        self.brazoSlider.setValue(self.brazoDerInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.brazoDerPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.brazoDerPin},{self.brazoDerInicio},0,0,0,{self.valorEsperaBrazo}\n")        
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
        self.enviar_comando(f"3,{self.brazoDerPin},0,0,0,0,0\n")
        self.brazoDerProgressBar.hide()

    def brazoOnOffPwm(self):        
        if self.brazoOnOff.isChecked()==True:
            self.etiquetaBrazoOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaBrazoOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.brazoDerPin},0,0,0,0,0\n")
        else:
            self.etiquetaBrazoOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaBrazoOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.brazoDerPin},0,0,0,0,0\n") 
       
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
            self.enviar_comando(f"4,{self.brazoDerPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaBrazo=self.definirServos.convertirVelocidadValor(self.valorVelocidadBrazo)
            self.enviar_comando(f"6,{self.brazoDerPin},{self.brazoDerMinimo},{self.brazoDerMaximo},{self.brazoDerInicio},{self.brazoDerRetraso},{self.valorEsperaBrazo}\n")
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
        self.enviar_comando(f"1,{self.rotacionDerPin},{value},0,0,0,{self.valorEsperaRotacion}\n")

    def rotacionPushButtonPwm(self):
        self.brazoDerProgressBar.show()
        self.rotacionOnOff.setChecked(True)            
        self.etiquetaRotacionOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaRotacionOnOff.setText(str('ON')) 
        self.valorEsperaRotacion=self.definirServos.convertirVelocidadValor(self.valorVelocidadRotacion)
        self.rotacion_valor.setText(str(self.rotacionDerInicio))
        self.rotacionSlider.setValue(self.rotacionDerInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.rotacionDerPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.rotacionDerPin},{self.rotacionDerInicio},0,0,0,{self.valorEsperaRotacion}\n")        
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
        self.enviar_comando(f"3,{self.rotacionDerPin},0,0,0,0,0\n")
        self.brazoDerProgressBar.hide()

    def rotacionOnOffPwm(self):        
        if self.rotacionOnOff.isChecked()==True:
            self.etiquetaRotacionOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaRotacionOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.rotacionDerPin},0,0,0,0,0\n")
        else:
            self.etiquetaRotacionOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaRotacionOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.rotacionDerPin},0,0,0,0,0\n") 
       
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
            self.enviar_comando(f"4,{self.rotacionDerPin},0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaRotacion=self.definirServos.convertirVelocidadValor(self.valorVelocidadRotacion)
            self.enviar_comando(f"6,{self.rotacionDerPin},{self.rotacionDerMinimo},{self.rotacionDerMaximo},{self.rotacionDerInicio},{self.rotacionDerRetraso},{self.valorEsperaRotacion}\n")
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
        self.enviar_comando(f"1,{self.omoplatoDerPin},{value},0,0,0,{self.valorEsperaOmoplato}\n")
        
    def omoplatoPushButtonPwm(self):
        self.brazoDerProgressBar.show()
        self.omoplatoOnOff.setChecked(True)            
        self.etiquetaOmoplatoOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaOmoplatoOnOff.setText(str('ON')) 
        self.valorEsperaOmoplato=self.definirServos.convertirVelocidadValor(self.valorVelocidadOmoplato)
        self.omoplato_valor.setText(str(self.omoplatoDerInicio))
        self.omoplatoSlider.setValue(self.omoplatoDerInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.omoplatoDerPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.omoplatoDerPin},{self.omoplatoDerInicio},0,0,0,{self.valorEsperaOmoplato}\n")        
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
        self.enviar_comando(f"3,{self.omoplatoDerPin},0,0,0,0,0\n")
        self.brazoDerProgressBar.hide()
    
    def omoplatoOnOffPwm(self):        
        if self.omoplatoOnOff.isChecked()==True:
            self.etiquetaOmoplatoOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaOmoplatoOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.omoplatoDerPin},0,0,0,0,0\n")
        else:
            self.etiquetaOmoplatoOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaOmoplatoOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.omoplatoDerPin},0,0,0,0,0\n") 
       
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
            self.enviar_comando(f"4,{self.omoplatoDerPin},0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaOmoplato=self.definirServos.convertirVelocidadValor(self.valorVelocidadOmoplato)
            self.enviar_comando(f"6,{self.omoplatoDerPin},{self.omoplatoDerMinimo},{self.omoplatoDerMaximo},{self.omoplatoDerInicio},{self.omoplatoDerRetraso},{self.valorEsperaOmoplato}\n")
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
        self.arduino_der.write(comando.encode())
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
    my_app = BrazoDerecho()
    my_app.show()
    sys.exit(app.exec_())
