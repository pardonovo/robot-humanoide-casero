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

class Cabeza(QMainWindow):
    def __init__(self):
        super(Cabeza,self).__init__()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, "cabeza.ui")
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
        self.rotacioncPin=self.definirServos.rotacioncPin
        self.rotacioncMinimo=self.definirServos.rotacioncMinimo
        self.rotacioncMaximo=self.definirServos.rotacioncMaximo
        self.rotacioncInicio=self.definirServos.rotacioncInicio
        self.rotacioncRetraso=self.definirServos.rotacioncRetraso
        self.cabezaABPin=self.definirServos.cabezaABPin
        self.cabezaABMinimo=self.definirServos.cabezaABMinimo
        self.cabezaABMaximo=self.definirServos.cabezaABMaximo
        self.cabezaABInicio=self.definirServos.cabezaABInicio
        self.cabezaABRetraso=self.definirServos.cabezaABRetraso
        self.cabezaDIPin=self.definirServos.cabezaDIPin
        self.cabezaDIMinimo=self.definirServos.cabezaDIMinimo
        self.cabezaDIMaximo=self.definirServos.cabezaDIMaximo
        self.cabezaDIInicio=self.definirServos.cabezaDIInicio
        self.cabezaDIRetraso=self.definirServos.cabezaDIRetraso
        self.ojosABPin=self.definirServos.ojosABPin
        self.ojosABMinimo=self.definirServos.ojosABMinimo
        self.ojosABMaximo=self.definirServos.ojosABMaximo
        self.ojosABInicio=self.definirServos.ojosABInicio
        self.ojosABRetraso=self.definirServos.ojosABRetraso
        self.ojosDIPin=self.definirServos.ojosDIPin
        self.ojosDIMinimo=self.definirServos.ojosDIMinimo
        self.ojosDIMaximo=self.definirServos.ojosDIMaximo
        self.ojosDIInicio=self.definirServos.ojosDIInicio
        self.ojosDIRetraso=self.definirServos.ojosDIRetraso            
        
        #Iniciar cabeza
        self.servos.iniciarServoIzq(self.ojosDIPin,self.ojosDIInicio,self.ojosDIRetraso)
        self.servos.iniciarServoIzq(self.rotacioncPin,self.rotacioncInicio,self.rotacioncRetraso)       
        self.servos.iniciarServoIzq(self.cabezaABPin,self.cabezaABInicio,self.cabezaABRetraso)    
        self.servos.iniciarServoIzq(self.cabezaDIPin,self.cabezaDIInicio,self.cabezaDIRetraso)
        self.servos.iniciarServoIzq(self.ojosABPin,self.ojosABInicio,self.ojosABRetraso)
        
        
        self.enviar_comando(f"2,{self.cabezaABPin},0,0,0,0,0\n")
        self.enviar_comando(f"1,{self.cabezaABPin},{self.cabezaABInicio+10},0,0,0,{self.cabezaABRetraso}\n")
        time.sleep(0.3)
        self.enviar_comando(f"3,{self.cabezaABPin},0,0,0,0,0\n")
        
        self.cabezaProgressBar.hide()
        
        self.setWindowTitle("Cabeza")

        # Botones de la barra superior
        self.click_posicion = QPoint()
        self.bt_close_cabeza_izq.clicked.connect(lambda: self.close())
        self.bt_minimize_cabeza_izq.clicked.connect(lambda: self.showMinimized())
    

        # Eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Sliders
        self.rotacioncSlider.setMinimum(self.rotacioncMinimo)
        self.rotacioncSlider.setMaximum(self.rotacioncMaximo)
        self.rotacionc_valor.setText(str(self.rotacioncInicio))
        self.rotacioncSlider.setValue(self.rotacioncInicio)
        self.etiquetaRotacioncPin.setText(self.rotacioncPin)
        self.etiquetaRotacioncMinimo.setText(str(self.rotacioncMinimo))
        self.etiquetaRotacioncMedio.setText(str(int(self.rotacioncMaximo/2)))
        self.etiquetaRotacioncMaximo.setText(str(self.rotacioncMaximo))
        self.rotacioncSlider.valueChanged.connect(self.rotacioncSliderPwm)
        self.valorVelocidadRotacionc=self.rotacioncSpinBox.value()        
        self.rotacioncSpinBox.valueChanged.connect(self.rotacioncSpinBoxPwm)
        
        self.cabezaABSlider.setMinimum(self.cabezaABMinimo)
        self.cabezaABSlider.setMaximum(self.cabezaABMaximo)
        self.cabezaAB_valor.setText(str(self.cabezaABInicio))
        self.cabezaABSlider.setValue(self.cabezaABInicio)
        self.etiquetaCabezaABPin.setText(self.cabezaABPin)
        self.etiquetaCabezaABMinimo.setText(str(self.cabezaABMinimo))
        self.etiquetaCabezaABMedio.setText(str(int(self.cabezaABMaximo/2)))
        self.etiquetaCabezaABMaximo.setText(str(self.cabezaABMaximo))
        self.cabezaABSlider.valueChanged.connect(self.cabezaABSliderPwm)
        self.valorVelocidadCabezaAB=self.cabezaABSpinBox.value()        
        self.cabezaABSpinBox.valueChanged.connect(self.cabezaABSpinBoxPwm)
        
        self.cabezaDISlider.setMinimum(self.cabezaDIMinimo)
        self.cabezaDISlider.setMaximum(self.cabezaDIMaximo)
        self.cabezaDI_valor.setText(str(self.cabezaDIInicio))
        self.cabezaDISlider.setValue(self.cabezaDIInicio)
        self.etiquetaCabezaDIPin.setText(self.cabezaDIPin)
        self.etiquetaCabezaDIMinimo.setText(str(self.cabezaDIMinimo))
        self.etiquetaCabezaDIMedio.setText(str(int(self.cabezaDIMaximo/2)))
        self.etiquetaCabezaDIMaximo.setText(str(self.cabezaDIMaximo))
        self.cabezaDISlider.valueChanged.connect(self.cabezaDISliderPwm)
        self.valorVelocidadCabezaDI=self.cabezaDISpinBox.value()        
        self.cabezaDISpinBox.valueChanged.connect(self.cabezaDISpinBoxPwm)
        
        self.ojosABSlider.setMinimum(self.ojosABMinimo)
        self.ojosABSlider.setMaximum(self.ojosABMaximo)
        self.ojosAB_valor.setText(str(self.ojosABInicio))
        self.ojosABSlider.setValue(self.ojosABInicio)
        self.etiquetaOjosABPin.setText(self.ojosABPin)
        self.etiquetaOjosABMinimo.setText(str(self.ojosABMinimo))
        self.etiquetaOjosABMedio.setText(str(int(self.ojosABMaximo/2)))
        self.etiquetaOjosABMaximo.setText(str(self.ojosABMaximo))
        self.ojosABSlider.valueChanged.connect(self.ojosABSliderPwm)
        self.valorVelocidadOjosAB=self.ojosABSpinBox.value()        
        self.ojosABSpinBox.valueChanged.connect(self.ojosABSpinBoxPwm)
        
        self.ojosDISlider.setMinimum(self.ojosDIMinimo)
        self.ojosDISlider.setMaximum(self.ojosDIMaximo)
        self.ojosDI_valor.setText(str(self.ojosDIInicio))
        self.ojosDISlider.setValue(self.ojosDIInicio)
        self.etiquetaOjosDIPin.setText(self.ojosDIPin)
        self.etiquetaOjosDIMinimo.setText(str(self.ojosDIMinimo))
        self.etiquetaOjosDIMedio.setText(str(int(90)))
        self.etiquetaOjosDIMaximo.setText(str(self.ojosDIMaximo))
        self.ojosDISlider.valueChanged.connect(self.ojosDISliderPwm)
        self.valorVelocidadOjosDI=self.ojosDISpinBox.value()        
        self.ojosDISpinBox.valueChanged.connect(self.ojosDISpinBoxPwm)            
        
        # Botones
        self.rotacioncOnOff.clicked.connect(self.rotacioncOnOffPwm)
        self.rotacioncBucle.clicked.connect(self.rotacioncBuclePwm)
        self.rotacioncPushButton.clicked.connect(self.rotacioncPushButtonPwm)   
        self.cabezaABOnOff.clicked.connect(self.cabezaABOnOffPwm)
        self.cabezaABBucle.clicked.connect(self.cabezaABBuclePwm)
        self.cabezaABPushButton.clicked.connect(self.cabezaABPushButtonPwm)
        self.cabezaDIOnOff.clicked.connect(self.cabezaDIOnOffPwm)
        self.cabezaDIBucle.clicked.connect(self.cabezaDIBuclePwm)
        self.cabezaDIPushButton.clicked.connect(self.cabezaDIPushButtonPwm)        
        self.ojosABOnOff.clicked.connect(self.ojosABOnOffPwm)
        self.ojosABBucle.clicked.connect(self.ojosABBuclePwm)
        self.ojosABPushButton.clicked.connect(self.ojosABPushButtonPwm)   
        self.ojosDIOnOff.clicked.connect(self.ojosDIOnOffPwm)
        self.ojosDIBucle.clicked.connect(self.ojosDIBuclePwm)        
        self.ojosDIPushButton.clicked.connect(self.ojosDIPushButtonPwm)            

    def rotacioncSpinBoxPwm(self, value):       
        self.valorVelocidadRotacionc = value;
        
    def rotacioncSliderPwm(self, value):
        self.valorEsperaRotacionc=self.definirServos.convertirVelocidadValor(self.valorVelocidadRotacionc)                
        self.rotacionc_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.rotacioncPin},{value},0,0,0,{self.valorEsperaRotacionc}\n")
        
    def rotacioncPushButtonPwm(self):
        self.cabezaProgressBar.show()
        self.rotacioncOnOff.setChecked(True)            
        self.etiquetaRotacioncOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaRotacioncOnOff.setText(str('ON'))
        self.valorEsperaRotacionc=self.definirServos.convertirVelocidadValor(self.valorVelocidadRotacionc)
        self.rotacionc_valor.setText(str(self.rotacioncInicio))
        self.rotacioncSlider.setValue(self.rotacioncInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.rotacioncPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.rotacioncPin},{self.rotacioncInicio},0,0,0,{self.valorEsperaRotacionc}\n")               
        time.sleep(self.valorVelocidadRotacionc/3)
        self.rotacioncOnOff.setChecked(False)            
        self.etiquetaRotacioncOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaRotacioncOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.rotacioncPin},0,0,0,0,0\n")
        self.cabezaProgressBar.hide()
    
    def rotacioncOnOffPwm(self):        
        if self.rotacioncOnOff.isChecked()==True:
            self.etiquetaRotacioncOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaRotacioncOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.rotacioncPin},0,0,0,0,0\n")
        else:
            self.etiquetaRotacioncOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaRotacioncOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.rotacioncPin},0,0,0,0,0\n") 
       
    def rotacioncBuclePwm(self):        
        if self.rotacioncBucle.isChecked()==True:
            self.etiquetaRotacioncBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaRotacioncBucle.setText(str('ON'))
            self.rotacioncSlider.setEnabled(False)
            self.rotacioncOnOff.setChecked(True)
            self.etiquetaRotacioncOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaRotacioncOnOff.setText(str('ON'))          
            self.rotacioncOnOff.setEnabled(False)            
            self.Deshabilitar_cabezaAB()
            self.Deshabilitar_cabezaDI()
            self.Deshabilitar_ojosAB()
            self.Deshabilitar_cabezaDI()
            self.enviar_comando(f"4,{self.rotacioncPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaRotacionc=self.definirServos.convertirVelocidadValor(self.valorVelocidadRotacionc)
            self.enviar_comando(f"6,{self.rotacioncPin},{self.rotacioncMinimo},{self.rotacioncMaximo},{self.rotacioncInicio},{self.rotacioncRetraso},{self.valorEsperaRotacionc}\n")
        else:
            self.etiquetaRotacioncBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaRotacioncBucle.setText(str('OFF'))
            self.rotacioncSlider.setEnabled(True)
            self.rotacioncOnOff.setChecked(False)
            self.etiquetaRotacioncOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaRotacioncOnOff.setText(str('OFF'))
            self.rotacioncOnOff.setEnabled(True)
            self.Habilitar_cabezaAB()        
            self.Habilitar_cabezaDI()
            self.Habilitar_ojosAB()
            self.Habilitar_ojosDI()
            self.enviar_comando(f"S")

    def cabezaABSpinBoxPwm(self, value):       
        self.valorVelocidadCabezaAB = value;        

    def cabezaABSliderPwm(self, value):
        self.valorEsperaCabezaAB=self.definirServos.convertirVelocidadValor(self.valorVelocidadCabezaAB)        
        self.cabezaAB_valor.setText(str(value))
        self.enviar_comando(f"1,{self.cabezaABPin},{value},0,0,0,{self.valorEsperaCabezaAB}\n")        
        
    def cabezaABPushButtonPwm(self):
        self.cabezaProgressBar.show()
        self.cabezaABOnOff.setChecked(True)            
        self.etiquetaCabezaABOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaCabezaABOnOff.setText(str('ON')) 
        self.valorEsperaCabezaAB=self.definirServos.convertirVelocidadValor(self.valorVelocidadCabezaAB)
        self.cabezaAB_valor.setText(str(self.cabezaABInicio))
        self.cabezaABSlider.setValue(self.cabezaABInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.cabezaABPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.cabezaABPin},{self.cabezaABInicio},0,0,0,{self.valorEsperaCabezaAB}\n")               
        time.sleep(self.valorVelocidadCabezaAB/3)
        self.cabezaABOnOff.setChecked(False)            
        self.etiquetaCabezaABOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaCabezaABOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.cabezaABPin},0,0,0,0,0\n")
        self.cabezaProgressBar.hide()
        
    def cabezaABOnOffPwm(self):        
        if self.cabezaABOnOff.isChecked()==True:
            self.etiquetaCabezaABOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaCabezaABOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.cabezaABPin},0,0,0,0,0\n")
        else:
            self.etiquetaCabezaABOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaCabezaABOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.cabezaABPin},0,0,0,0,0\n")         

    def cabezaABBuclePwm(self):        
        if self.cabezaABBucle.isChecked()==True:
            self.etiquetaCabezaABBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaCabezaABBucle.setText(str('ON'))
            self.cabezaABSlider.setEnabled(False)
            self.cabezaABOnOff.setChecked(True)
            self.etiquetaCabezaABOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaCabezaABOnOff.setText(str('ON'))          
            self.cabezaABOnOff.setEnabled(False)
            self.Deshabilitar_rotacionc()   
            self.Deshabilitar_cabezaDI()
            self.Deshabilitar_ojosAB()
            self.Deshabilitar_ojosDI()   
            self.enviar_comando(f"4,{self.cabezaABPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaCabezaAB=self.definirServos.convertirVelocidadValor(self.valorVelocidadCabezaAB)
            self.enviar_comando(f"6,{self.cabezaABPin},{self.cabezaABMinimo},{self.cabezaABMaximo},{self.cabezaABInicio},{self.cabezaABRetraso},{self.valorEsperaCabezaAB}\n")
        else:
            self.etiquetaCabezaABBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaCabezaABBucle.setText(str('OFF'))
            self.cabezaABSlider.setEnabled(True)
            self.cabezaABOnOff.setChecked(False)
            self.etiquetaCabezaABOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaCabezaABOnOff.setText(str('OFF'))
            self.cabezaABOnOff.setEnabled(True)
            self.Habilitar_rotacionc()
            self.Habilitar_cabezaDI()
            self.Habilitar_ojosAB()
            self.Habilitar_ojosDI()
            self.enviar_comando(f"S")   

    def cabezaDISpinBoxPwm(self, value):       
        self.valorVelocidadCabezaDI = value;        

    def cabezaDISliderPwm(self, value):
        self.valorEsperaCabezaDI=self.definirServos.convertirVelocidadValor(self.valorVelocidadCabezaDI)        
        self.cabezaDI_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.cabezaDIPin},{value},0,0,0,{self.valorEsperaCabezaDI}\n")

    def cabezaDIPushButtonPwm(self):
        self.cabezaProgressBar.show()
        self.cabezaDIOnOff.setChecked(True)            
        self.etiquetaCabezaDIOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaCabezaDIOnOff.setText(str('ON'))
        self.valorEsperaCabezaDI=self.definirServos.convertirVelocidadValor(self.valorVelocidadCabezaDI)
        self.cabezaDI_valor.setText(str(self.cabezaDIInicio))
        self.cabezaDISlider.setValue(self.cabezaDIInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.cabezaDIPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.cabezaDIPin},{self.cabezaDIInicio},0,0,0,{self.valorEsperaCabezaDI}\n")               
        time.sleep(self.valorVelocidadCabezaDI/3)
        self.cabezaDIOnOff.setChecked(False)            
        self.etiquetaCabezaDIOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaCabezaDIOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.cabezaDIPin},0,0,0,0,0\n")
        self.cabezaProgressBar.hide()

    def cabezaDIOnOffPwm(self):        
        if self.cabezaDIOnOff.isChecked()==True:
            self.etiquetaCabezaDIOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaCabezaDIOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.cabezaDIPin},0,0,0,0,0\n")
        else:
            self.etiquetaCabezaDIOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaCabezaDIOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.cabezaDIPin},0,0,0,0,0\n") 
       
    def cabezaDIBuclePwm(self):        
        if self.cabezaDIBucle.isChecked()==True:
            self.etiquetaCabezaDIBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaCabezaDIBucle.setText(str('ON'))
            self.cabezaDISlider.setEnabled(False)
            self.cabezaDIOnOff.setChecked(True)
            self.etiquetaCabezaDIOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaCabezaDIOnOff.setText(str('ON'))          
            self.cabezaDIOnOff.setEnabled(False)
            self.Deshabilitar_rotacionc()
            self.Deshabilitar_cabezaAB()
            self.Deshabilitar_ojosAB()
            self.Deshabilitar_ojosDI()
            self.enviar_comando(f"4,{self.cabezaDIPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaCabezaDI=self.definirServos.convertirVelocidadValor(self.valorVelocidadCabezaDI)
            self.enviar_comando(f"6,{self.cabezaDIPin},{self.cabezaDIMinimo},{self.cabezaDIMaximo},{self.cabezaDIInicio},{self.cabezaDIRetraso},{self.valorEsperaCabezaDI}\n")
        else:
            self.etiquetaCabezaDIBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaCabezaDIBucle.setText(str('OFF'))
            self.cabezaDISlider.setEnabled(True)
            self.cabezaDIOnOff.setChecked(False)
            self.etiquetaCabezaDIOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaCabezaDIOnOff.setText(str('OFF'))
            self.cabezaDIOnOff.setEnabled(True)
            self.Habilitar_rotacionc()
            self.Habilitar_cabezaAB()
            self.Habilitar_ojosAB()
            self.Habilitar_ojosDI()
            self.enviar_comando(f"S")

    def ojosABSpinBoxPwm(self, value):       
        self.valorVelocidadOjosAB = value;
        
    def ojosABSliderPwm(self, value):
        self.valorEsperaOjosAB=self.definirServos.convertirVelocidadValor(self.valorVelocidadOjosAB)
        self.ojosAB_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.ojosABPin},{value},0,0,0,{self.valorEsperaOjosAB}\n")

    def ojosABPushButtonPwm(self):
        self.cabezaProgressBar.show()
        self.ojosABOnOff.setChecked(True)            
        self.etiquetaOjosABOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaOjosABOnOff.setText(str('ON')) 
        self.valorEsperaOjosAB=self.definirServos.convertirVelocidadValor(self.valorVelocidadOjosAB)
        self.ojosAB_valor.setText(str(self.ojosABInicio))
        self.ojosABSlider.setValue(self.ojosABInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.ojosABPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.ojosABPin},{self.ojosABInicio},0,0,0,{self.valorEsperaOjosAB}\n")                
        time.sleep(self.valorVelocidadOjosAB/3)
        self.ojosABOnOff.setChecked(False)            
        self.etiquetaOjosABOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaOjosABOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.ojosABPin},0,0,0,0,0\n")
        self.cabezaProgressBar.hide()

    def ojosABOnOffPwm(self):        
        if self.ojosABOnOff.isChecked()==True:
            self.etiquetaOjosABOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaOjosABOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.ojosABPin},0,0,0,0,0\n")
        else:
            self.etiquetaOjosABOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaOjosABOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.ojosABPin},0,0,0,0,0\n") 
       
    def ojosABBuclePwm(self):        
        if self.ojosABBucle.isChecked()==True:
            self.etiquetaOjosABBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaOjosABBucle.setText(str('ON'))
            self.ojosABSlider.setEnabled(False)
            self.ojosABOnOff.setChecked(True)
            self.etiquetaOjosABOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaOjosABOnOff.setText(str('ON'))          
            self.ojosABOnOff.setEnabled(False)
            self.Deshabilitar_rotacionc()
            self.Deshabilitar_cabezaAB()
            self.Deshabilitar_cabezaDI()
            self.Deshabilitar_ojosDI() 
            self.enviar_comando(f"4,{self.ojosABPin},0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaOjosAB=self.definirServos.convertirVelocidadValor(self.valorVelocidadOjosAB)
            self.enviar_comando(f"6,{self.ojosABPin},{self.ojosABMinimo},{self.ojosABMaximo},{self.ojosABInicio},{self.ojosABRetraso},{self.valorEsperaOjosAB}\n")
        else:
            self.etiquetaOjosABBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaOjosABBucle.setText(str('OFF'))
            self.ojosABSlider.setEnabled(True)
            self.ojosABOnOff.setChecked(False)
            self.etiquetaOjosABOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaOjosABOnOff.setText(str('OFF'))
            self.ojosABOnOff.setEnabled(True)
            self.Habilitar_rotacionc()
            self.Habilitar_cabezaAB()
            self.Habilitar_cabezaDI()
            self.Habilitar_ojosDI()
            self.enviar_comando(f"S")

    def ojosDISpinBoxPwm(self, value):       
        self.valorVelocidadOjosDI = value;

    def ojosDISliderPwm(self, value):
        self.valorEsperaOjosDI=self.definirServos.convertirVelocidadValor(self.valorVelocidadOjosDI)
        self.ojosDI_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.ojosDIPin},{value},0,0,0,{self.valorEsperaOjosDI}\n")
        
    def ojosDIPushButtonPwm(self):
        self.cabezaProgressBar.show()
        self.ojosDIOnOff.setChecked(True)            
        self.etiquetaOjosDIOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaOjosDIOnOff.setText(str('ON')) 
        self.valorEsperaOjosDI=self.definirServos.convertirVelocidadValor(self.valorVelocidadOjosDI)
        self.ojosDI_valor.setText(str(self.ojosDIInicio))
        self.ojosDISlider.setValue(self.ojosDIInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.ojosDIPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.ojosDIPin},{self.ojosDIInicio},0,0,0,{self.valorEsperaOjosDI}\n")              
        time.sleep(self.valorVelocidadOjosDI/3)
        self.ojosDIOnOff.setChecked(False)            
        self.etiquetaOjosDIOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaOjosDIOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.ojosDIPin},0,0,0,0,0\n")
        self.cabezaProgressBar.hide()
    
    def ojosDIOnOffPwm(self):        
        if self.ojosDIOnOff.isChecked()==True:
            self.etiquetaOjosDIOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaOjosDIOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.ojosDIPin},0,0,0,0,0\n")
        else:
            self.etiquetaOjosDIOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaOjosDIOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.ojosDIPin},0,0,0,0,0\n") 
       
    def ojosDIBuclePwm(self):        
        if self.ojosDIBucle.isChecked()==True:
            self.etiquetaOjosDIBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaOjosDIBucle.setText(str('ON'))
            self.ojosDISlider.setEnabled(False)
            self.ojosDIOnOff.setChecked(True)
            self.etiquetaOjosDIOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaOjosDIOnOff.setText(str('ON'))          
            self.ojosDIOnOff.setEnabled(False)
            self.Deshabilitar_rotacionc()
            self.Deshabilitar_cabezaAB()
            self.Deshabilitar_cabezaDI()
            self.Deshabilitar_ojosAB() 
            self.enviar_comando(f"4,{self.ojosDIPin},0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaOjosDI=self.definirServos.convertirVelocidadValor(self.valorVelocidadOjosDI)
            self.enviar_comando(f"6,{self.ojosDIPin},{self.ojosDIMinimo},{self.ojosDIMaximo},{self.ojosDIInicio},{self.ojosDIRetraso},{self.valorEsperaOjosDI}\n")
        else:
            self.etiquetaOjosDIBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaOjosDIBucle.setText(str('OFF'))
            self.ojosDISlider.setEnabled(True)
            self.ojosDIOnOff.setChecked(False)
            self.etiquetaOjosDIOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaOjosDIOnOff.setText(str('OFF'))
            self.ojosDIOnOff.setEnabled(True)
            self.Habilitar_rotacionc()
            self.Habilitar_cabezaAB()
            self.Habilitar_cabezaDI()
            self.Habilitar_ojosAB()
            self.enviar_comando(f"S")


    def enviar_comando(self, comando):
        self.arduino_izq.write(comando.encode())
        print(f"Comando enviado: {comando}")           
        
    def Deshabilitar_rotacionc(self):
        self.rotacioncSlider.setEnabled(False)
        self.rotacioncOnOff.setEnabled(False)
        self.rotacioncBucle.setEnabled(False)
        self.rotacioncSpinBox.setEnabled(False)
        self.rotacioncPushButton.setEnabled(False)
          
    def Deshabilitar_cabezaAB(self):
        self.cabezaABSlider.setEnabled(False)
        self.cabezaABOnOff.setEnabled(False)
        self.cabezaABBucle.setEnabled(False)
        self.cabezaABSpinBox.setEnabled(False)
        self.cabezaABPushButton.setEnabled(False)
          
    def Deshabilitar_cabezaDI(self):
        self.cabezaDISlider.setEnabled(False)
        self.cabezaDIOnOff.setEnabled(False)
        self.cabezaDIBucle.setEnabled(False)
        self.cabezaDISpinBox.setEnabled(False)
        self.cabezaDIPushButton.setEnabled(False)
        
    def Deshabilitar_ojosAB(self):
        self.ojosABSlider.setEnabled(False)
        self.ojosABOnOff.setEnabled(False)
        self.ojosABBucle.setEnabled(False)
        self.ojosABSpinBox.setEnabled(False)
        self.ojosABPushButton.setEnabled(False)
        
    def Deshabilitar_ojosDI(self):
        self.ojosDISlider.setEnabled(False)
        self.ojosDIOnOff.setEnabled(False)
        self.ojosDIBucle.setEnabled(False)
        self.ojosDISpinBox.setEnabled(False)
        self.ojosDIPushButton.setEnabled(False)
          
    def Habilitar_rotacionc(self):
        self.rotacioncSlider.setEnabled(True)
        self.rotacioncOnOff.setEnabled(True)
        self.rotacioncBucle.setEnabled(True)
        self.rotacioncSpinBox.setEnabled(True)
        self.rotacioncPushButton.setEnabled(True)
        
    def Habilitar_cabezaAB(self):
        self.cabezaABSlider.setEnabled(True)
        self.cabezaABOnOff.setEnabled(True)
        self.cabezaABBucle.setEnabled(True)
        self.cabezaABSpinBox.setEnabled(True)
        self.cabezaABPushButton.setEnabled(True)
        
    def Habilitar_cabezaDI(self):
        self.cabezaDISlider.setEnabled(True)
        self.cabezaDIOnOff.setEnabled(True)
        self.cabezaDIBucle.setEnabled(True)
        self.cabezaDISpinBox.setEnabled(True)
        self.cabezaDIPushButton.setEnabled(True)
        
    def Habilitar_ojosAB(self):
        self.ojosABSlider.setEnabled(True)
        self.ojosABOnOff.setEnabled(True)
        self.ojosABBucle.setEnabled(True)
        self.ojosABSpinBox.setEnabled(True)
        self.ojosABPushButton.setEnabled(True)

    def Habilitar_ojosDI(self):
        self.ojosDISlider.setEnabled(True)
        self.ojosDIOnOff.setEnabled(True)
        self.ojosDIBucle.setEnabled(True)
        self.ojosDISpinBox.setEnabled(True)
        self.ojosDIPushButton.setEnabled(True)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = Cabeza()
    my_app.show()
    sys.exit(app.exec_())
