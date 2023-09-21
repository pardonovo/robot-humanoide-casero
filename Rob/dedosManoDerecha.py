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

class DedosDerecha(QMainWindow):
    def __init__(self):
        super(DedosDerecha,self).__init__()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, "dedosManoDerecha.ui")
        loadUi(ui_file, self)          
         
        self.definirServos = DefinirServos()
        self.arduino = Arduino()
        self.servos = Servos()        
         
        # Inicialización de la conexión serial
        self.arduino_port_derecha=self.arduino.arduinoPuertoDer
        self.baud_rate_der=self.arduino.arduinoBaudiosDer
        self.arduino_der = serial.Serial(self.arduino.arduino_port_derecha, self.arduino.baud_rate_der)
        time.sleep(2)  # Esperar a que se establezca la conexión            
        
        # Datos servos dedos
        self.meniqueDerPin=self.definirServos.meniqueDerPin
        self.meniqueDerMinimo=self.definirServos.meniqueDerMinimo
        self.meniqueDerMaximo=self.definirServos.meniqueDerMaximo
        self.meniqueDerInicio=self.definirServos.meniqueDerInicio
        self.meniqueDerRetraso=self.definirServos.meniqueDerRetraso
        self.anularDerPin=self.definirServos.anularDerPin
        self.anularDerMinimo=self.definirServos.anularDerMinimo
        self.anularDerMaximo=self.definirServos.anularDerMaximo
        self.anularDerInicio=self.definirServos.anularDerInicio
        self.anularDerRetraso=self.definirServos.anularDerRetraso
        self.medioDerPin=self.definirServos.medioDerPin
        self.medioDerMinimo=self.definirServos.medioDerMinimo
        self.medioDerMaximo=self.definirServos.medioDerMaximo
        self.medioDerInicio=self.definirServos.medioDerInicio
        self.medioDerRetraso=self.definirServos.medioDerRetraso
        self.indiceDerPin=self.definirServos.indiceDerPin
        self.indiceDerMinimo=self.definirServos.indiceDerMinimo
        self.indiceDerMaximo=self.definirServos.indiceDerMaximo
        self.indiceDerInicio=self.definirServos.indiceDerInicio
        self.indiceDerRetraso=self.definirServos.indiceDerRetraso
        self.pulgarDerPin=self.definirServos.pulgarDerPin
        self.pulgarDerMinimo=self.definirServos.pulgarDerMinimo
        self.pulgarDerMaximo=self.definirServos.pulgarDerMaximo
        self.pulgarDerInicio=self.definirServos.pulgarDerInicio
        self.pulgarDerRetraso=self.definirServos.pulgarDerRetraso            
        
        #Iniciar dedos
        self.servos.iniciarServoDer(self.meniqueDerPin,self.meniqueDerInicio,self.meniqueDerRetraso)
        self.servos.iniciarServoDer(self.anularDerPin,self.anularDerInicio,self.anularDerRetraso)
        self.servos.iniciarServoDer(self.medioDerPin,self.medioDerInicio,self.medioDerRetraso)
        self.servos.iniciarServoDer(self.indiceDerPin,self.indiceDerInicio,self.indiceDerRetraso)
        self.servos.iniciarServoDer(self.pulgarDerPin,self.pulgarDerInicio,self.pulgarDerRetraso)
        
        self.manoDerProgressBar.hide()
        
        self.setWindowTitle("Dedos Mano Derecha")

        # Botones de la barra superior
        self.click_posicion = QPoint()
        self.bt_close_mano_der.clicked.connect(lambda: self.close())
        self.bt_minimize_mano_der.clicked.connect(lambda: self.showMinimized())
    

        # Eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Sliders        
        self.meniqueSlider.setMinimum(self.meniqueDerMinimo)
        self.meniqueSlider.setMaximum(self.meniqueDerMaximo)
        self.menique_valor.setText(str(self.meniqueDerInicio))
        self.meniqueSlider.setValue(self.meniqueDerInicio)
        self.etiquetaMeniquePin.setText(self.meniqueDerPin)
        self.etiquetaMeniqueMinimo.setText(str(self.meniqueDerMinimo))
        self.etiquetaMeniqueMedio.setText(str(int(self.meniqueDerMaximo/2)))
        self.etiquetaMeniqueMaximo.setText(str(self.meniqueDerMaximo))
        self.meniqueSlider.valueChanged.connect(self.meniqueSliderPwm)
        self.valorVelocidadMenique=self.meniqueSpinBox.value()        
        self.meniqueSpinBox.valueChanged.connect(self.meniqueSpinBoxPwm)
        
        self.anularSlider.setMinimum(self.anularDerMinimo)
        self.anularSlider.setMaximum(self.anularDerMaximo)
        self.anular_valor.setText(str(self.anularDerMinimo))
        self.etiquetaAnularPin.setText(self.anularDerPin)
        self.etiquetaAnularMinimo.setText(str(self.anularDerMinimo))
        self.etiquetaAnularMedio.setText(str(int(self.anularDerMaximo/2)))
        self.etiquetaAnularMaximo.setText(str(self.anularDerMaximo))
        self.anularSlider.valueChanged.connect(self.anularSliderPwm)
        self.valorVelocidadAnular=self.anularSpinBox.value()        
        self.anularSpinBox.valueChanged.connect(self.anularSpinBoxPwm)
       
        self.medioSlider.setMinimum(self.medioDerMinimo)
        self.medioSlider.setMaximum(self.medioDerMaximo)
        self.medio_valor.setText(str(self.medioDerInicio))
        self.medioSlider.setValue(self.medioDerInicio)
        self.etiquetaMedioPin.setText(self.medioDerPin)
        self.etiquetaMedioMinimo.setText(str(self.medioDerMinimo))
        self.etiquetaMedioMedio.setText(str(int(self.medioDerMaximo/2)))
        self.etiquetaMedioMaximo.setText(str(self.medioDerMaximo))
        self.medioSlider.valueChanged.connect(self.medioSliderPwm)
        self.valorVelocidadMedio=self.medioSpinBox.value()        
        self.medioSpinBox.valueChanged.connect(self.medioSpinBoxPwm)
        
        self.indiceSlider.setMinimum(self.indiceDerMinimo)
        self.indiceSlider.setMaximum(self.indiceDerMaximo)
        self.indice_valor.setText(str(self.indiceDerInicio))
        self.indiceSlider.setValue(self.indiceDerInicio)
        self.etiquetaIndicePin.setText(self.indiceDerPin)
        self.etiquetaIndiceMinimo.setText(str(self.indiceDerMinimo))
        self.etiquetaIndiceMedio.setText(str(int(self.indiceDerMaximo/2)))
        self.etiquetaIndiceMaximo.setText(str(self.indiceDerMaximo))
        self.indiceSlider.valueChanged.connect(self.indiceSliderPwm)
        self.valorVelocidadIndice=self.indiceSpinBox.value()        
        self.indiceSpinBox.valueChanged.connect(self.indiceSpinBoxPwm)
        
        self.pulgarSlider.setMinimum(self.pulgarDerMinimo)
        self.pulgarSlider.setMaximum(self.pulgarDerMaximo)
        self.pulgar_valor.setText(str(self.pulgarDerMinimo))
        self.etiquetaPulgarPin.setText(self.pulgarDerPin)
        self.etiquetaPulgarMinimo.setText(str(self.pulgarDerMinimo))
        self.etiquetaPulgarMedio.setText(str(int(self.pulgarDerMaximo/2)))
        self.etiquetaPulgarMaximo.setText(str(self.pulgarDerMaximo))
        self.pulgarSlider.valueChanged.connect(self.pulgarSliderPwm)
        self.valorVelocidadPulgar=self.pulgarSpinBox.value()        
        self.pulgarSpinBox.valueChanged.connect(self.pulgarSpinBoxPwm)         
        
        # Botones
        self.meniqueOnOff.clicked.connect(self.meniqueOnOffPwm)
        self.meniqueBucle.clicked.connect(self.meniqueBuclePwm)
        self.meniquePushButton.clicked.connect(self.meniquePushButtonPwm)   
        self.anularOnOff.clicked.connect(self.anularOnOffPwm)
        self.anularBucle.clicked.connect(self.anularBuclePwm)
        self.anularPushButton.clicked.connect(self.anularPushButtonPwm)  
        self.medioOnOff.clicked.connect(self.medioOnOffPwm)
        self.medioBucle.clicked.connect(self.medioBuclePwm)
        self.medioPushButton.clicked.connect(self.medioPushButtonPwm)  
        self.indiceOnOff.clicked.connect(self.indiceOnOffPwm)
        self.indiceBucle.clicked.connect(self.indiceBuclePwm)
        self.indicePushButton.clicked.connect(self.indicePushButtonPwm)  
        self.pulgarOnOff.clicked.connect(self.pulgarOnOffPwm)
        self.pulgarBucle.clicked.connect(self.pulgarBuclePwm)
        self.pulgarPushButton.clicked.connect(self.pulgarPushButtonPwm)  
        
    def meniqueSpinBoxPwm(self, value):       
        self.valorVelocidadMenique = value;
        
    def meniqueSliderPwm(self, value):
        self.valorEsperaMenique=self.definirServos.convertirVelocidadValor(self.valorVelocidadMenique)  
        self.menique_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.meniqueDerPin},{value},0,0,0,{self.valorEsperaMenique}\n")
    
    def meniquePushButtonPwm(self):
        self.manoDerProgressBar.show()
        self.meniqueOnOff.setChecked(True)            
        self.etiquetaMeniqueOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaMeniqueOnOff.setText(str('ON')) 
        self.valorEsperaMenique=self.definirServos.convertirVelocidadValor(self.valorVelocidadMenique)
        self.menique_valor.setText(str(self.meniqueDerInicio))
        self.meniqueSlider.setValue(self.meniqueDerInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.meniqueDerPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.meniqueDerPin},{self.meniqueDerInicio},0,0,0,{self.valorEsperaMenique}\n")               
        time.sleep(self.valorVelocidadMenique/2)
        self.meniqueOnOff.setChecked(False)            
        self.etiquetaMeniqueOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaMeniqueOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.meniqueDerPin},0,0,0,0,0\n")
        self.manoDerProgressBar.hide()
    
    def meniqueOnOffPwm(self):        
        if self.meniqueOnOff.isChecked()==True:
            self.etiquetaMeniqueOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMeniqueOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.meniqueDerPin},0,0,0,0,0\n")
        else:
            self.etiquetaMeniqueOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMeniqueOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.meniqueDerPin},0,0,0,0,0\n") 
       
    def meniqueBuclePwm(self):        
        if self.meniqueBucle.isChecked()==True:
            self.etiquetaMeniqueBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMeniqueBucle.setText(str('ON'))
            self.meniqueSlider.setEnabled(False)
            self.meniquePushButton.setEnabled(False)
            self.meniqueSpinBox.setEnabled(False)
            self.meniqueOnOff.setChecked(True)
            self.etiquetaMeniqueOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMeniqueOnOff.setText(str('ON'))          
            self.meniqueOnOff.setEnabled(False)            
            self.Deshabilitar_anular()
            self.Deshabilitar_medio()
            self.Deshabilitar_indice()
            self.Deshabilitar_pulgar()
            self.enviar_comando(f"4,{self.meniqueDerPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaMenique=self.definirServos.convertirVelocidadValor(self.valorVelocidadMenique)
            self.enviar_comando(f"6,{self.meniqueDerPin},{self.meniqueDerMinimo},{self.meniqueDerMaximo},{self.meniqueDerInicio},{self.meniqueDerRetraso},{self.valorEsperaMenique}\n")
        else:
            self.etiquetaMeniqueBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMeniqueBucle.setText(str('OFF'))
            self.meniqueSlider.setEnabled(True)
            self.meniquePushButton.setEnabled(True)
            self.meniqueSpinBox.setEnabled(True)
            self.meniqueOnOff.setChecked(False)
            self.etiquetaMeniqueOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMeniqueOnOff.setText(str('OFF'))
            self.meniqueOnOff.setEnabled(True)
            self.Habilitar_anular()        
            self.Habilitar_medio()
            self.Habilitar_indice()
            self.Habilitar_pulgar()
            self.enviar_comando(f"S")

    def anularSpinBoxPwm(self, value):       
        self.valorVelocidadAnular = value;

    def anularSliderPwm(self, value):
        self.valorEsperaAnular=self.definirServos.convertirVelocidadValor(self.valorVelocidadAnular)        
        self.anular_valor.setText(str(value))
        self.enviar_comando(f"1,{self.anularDerPin},{value},0,0,0,{self.valorEsperaAnular}\n")
        
    def anularPushButtonPwm(self):
        self.manoDerProgressBar.show()
        self.anularOnOff.setChecked(True)            
        self.etiquetaAnularOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaAnularOnOff.setText(str('ON')) 
        self.valorEsperaAnular=self.definirServos.convertirVelocidadValor(self.valorVelocidadAnular)
        self.anular_valor.setText(str(self.anularDerInicio))
        self.anularSlider.setValue(self.anularDerInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.anularDerPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.anularDerPin},{self.anularDerInicio},0,0,0,{self.valorEsperaAnular}\n")        
        time.sleep(self.valorVelocidadAnular/3)
        self.anularOnOff.setChecked(False)            
        self.etiquetaAnularOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaAnularOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.anularDerPin},0,0,0,0,0\n")
        self.manoDerProgressBar.hide()
        
    def anularOnOffPwm(self):        
        if self.anularOnOff.isChecked()==True:
            self.etiquetaAnularOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaAnularOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.anularDerPin},0,0,0,0,0\n")
        else:
            self.etiquetaAnularOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaAnularOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.anularDerPin},0,0,0,0,0\n")         

    def anularBuclePwm(self):        
        if self.anularBucle.isChecked()==True:
            self.etiquetaAnularBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaAnularBucle.setText(str('ON'))
            self.anularSlider.setEnabled(False)
            self.anularPushButton.setEnabled(False)
            self.anularSpinBox.setEnabled(False)
            self.anularOnOff.setChecked(True)
            self.etiquetaAnularOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaAnularOnOff.setText(str('ON'))          
            self.anularOnOff.setEnabled(False)
            self.Deshabilitar_menique()   
            self.Deshabilitar_medio()
            self.Deshabilitar_indice()
            self.Deshabilitar_pulgar()   
            self.enviar_comando(f"4,{self.anularDerPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaAnular=self.definirServos.convertirVelocidadValor(self.valorVelocidadAnular)
            self.enviar_comando(f"6,{self.anularDerPin},{self.anularDerMinimo},{self.anularDerMaximo},{self.anularDerInicio},{self.anularDerRetraso},{self.valorEsperaAnular}\n")
        else:
            self.etiquetaAnularBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaAnularBucle.setText(str('OFF'))
            self.anularSlider.setEnabled(True)
            self.anularPushButton.setEnabled(True)
            self.anularSpinBox.setEnabled(True)
            self.anularOnOff.setChecked(False)
            self.etiquetaAnularOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaAnularOnOff.setText(str('OFF'))
            self.anularOnOff.setEnabled(True)
            self.Habilitar_menique()
            self.Habilitar_medio()
            self.Habilitar_indice()
            self.Habilitar_pulgar()
            self.enviar_comando(f"S")   

    def medioSpinBoxPwm(self, value):       
        self.valorVelocidadMedio = value;

    def medioSliderPwm(self, value):
        self.valorEsperaMedio=self.definirServos.convertirVelocidadValor(self.valorVelocidadMedio)        
        self.medio_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.medioDerPin},{value},0,0,0,{self.valorEsperaMedio}\n")

    def medioPushButtonPwm(self):
        self.manoDerProgressBar.show()
        self.medioOnOff.setChecked(True)            
        self.etiquetaMedioOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaMedioOnOff.setText(str('ON'))
        self.valorEsperaMedio=self.definirServos.convertirVelocidadValor(self.valorVelocidadMedio)
        self.medio_valor.setText(str(self.medioDerInicio))
        self.medioSlider.setValue(self.medioDerInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.medioDerPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.medioDerPin},{self.medioDerInicio},0,0,0,{self.valorEsperaMedio}\n")        
        time.sleep(self.valorVelocidadMedio/2)
        self.medioOnOff.setChecked(False)            
        self.etiquetaMedioOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaMedioOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.medioDerPin},0,0,0,0,0\n")
        self.manoDerProgressBar.hide()

    def medioOnOffPwm(self):        
        if self.medioOnOff.isChecked()==True:
            self.etiquetaMedioOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMedioOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.medioDerPin},0,0,0,0,0\n")
        else:
            self.etiquetaMedioOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMedioOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.medioDerPin},0,0,0,0,0\n") 
       
    def medioBuclePwm(self):        
        if self.medioBucle.isChecked()==True:
            self.etiquetaMedioBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMedioBucle.setText(str('ON'))
            self.medioSlider.setEnabled(False)
            self.medioPushButton.setEnabled(False)
            self.medioSpinBox.setEnabled(False)
            self.medioOnOff.setChecked(True)
            self.etiquetaMedioOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMedioOnOff.setText(str('ON'))          
            self.medioOnOff.setEnabled(False)
            self.Deshabilitar_menique()
            self.Deshabilitar_anular()
            self.Deshabilitar_indice()
            self.Deshabilitar_pulgar()
            self.enviar_comando(f"4,{self.medioDerPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaMedio=self.definirServos.convertirVelocidadValor(self.valorVelocidadMedio)
            self.enviar_comando(f"6,{self.medioDerPin},{self.medioDerMinimo},{self.medioDerMaximo},{self.medioDerInicio},{self.medioDerRetraso},{self.valorEsperaMedio}\n")
        else:
            self.etiquetaMedioBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMedioBucle.setText(str('OFF'))
            self.medioSlider.setEnabled(True)
            self.medioPushButton.setEnabled(True)
            self.medioSpinBox.setEnabled(True)
            self.medioOnOff.setChecked(False)
            self.etiquetaMedioOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMedioOnOff.setText(str('OFF'))
            self.medioOnOff.setEnabled(True)
            self.Habilitar_menique()
            self.Habilitar_anular()
            self.Habilitar_indice()
            self.Habilitar_pulgar()
            self.enviar_comando(f"S")
            
    def indiceSpinBoxPwm(self, value):       
        self.valorVelocidadIndice = value;
        
    def indiceSliderPwm(self, value):
        self.valorEsperaIndice=self.definirServos.convertirVelocidadValor(self.valorVelocidadIndice)
        self.indice_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.indiceDerPin},{value},0,0,0,{self.valorEsperaIndice}\n")        
    
    def indiceOnOffPwm(self):        
        if self.indiceOnOff.isChecked()==True:
            self.etiquetaIndiceOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaIndiceOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.indiceDerPin},0,0,0,0,0\n")
        else:
            self.etiquetaIndiceOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaIndiceOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.indiceDerPin},0,0,0,0,0\n") 

    def indicePushButtonPwm(self):
        self.manoDerProgressBar.show()
        self.indiceOnOff.setChecked(True)            
        self.etiquetaIndiceOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaIndiceOnOff.setText(str('ON')) 
        self.valorEsperaIndice=self.definirServos.convertirVelocidadValor(self.valorVelocidadIndice)
        self.indice_valor.setText(str(self.indiceDerInicio))
        self.indiceSlider.setValue(self.indiceDerInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.indiceDerPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.indiceDerPin},{self.indiceDerInicio},0,0,0,{self.valorEsperaIndice}\n")        
        time.sleep(self.valorVelocidadIndice/2)
        self.indiceOnOff.setChecked(False)            
        self.etiquetaIndiceOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaIndiceOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.indiceDerPin},0,0,0,0,0\n")
        self.manoDerProgressBar.hide()

    def indiceBuclePwm(self):        
        if self.indiceBucle.isChecked()==True:
            self.etiquetaIndiceBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaIndiceBucle.setText(str('ON'))
            self.indiceSlider.setEnabled(False)
            self.indicePushButton.setEnabled(False)
            self.indiceSpinBox.setEnabled(False)
            self.indiceOnOff.setChecked(True)
            self.etiquetaIndiceOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaIndiceOnOff.setText(str('ON'))          
            self.indiceOnOff.setEnabled(False)
            self.Deshabilitar_menique()
            self.Deshabilitar_anular()
            self.Deshabilitar_medio()
            self.Deshabilitar_pulgar() 
            self.enviar_comando(f"4,{self.indiceDerPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaIndice=self.definirServos.convertirVelocidadValor(self.valorVelocidadIndice)
            self.enviar_comando(f"6,{self.indiceDerPin},{self.indiceDerMinimo},{self.indiceDerMaximo},{self.indiceDerInicio},{self.indiceDerRetraso},{self.valorEsperaIndice}\n")
        else:
            self.etiquetaIndiceBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaIndiceBucle.setText(str('OFF'))
            self.indiceSlider.setEnabled(True)
            self.indicePushButton.setEnabled(True)
            self.indiceSpinBox.setEnabled(True)
            self.indiceOnOff.setChecked(False)
            self.etiquetaIndiceOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaIndiceOnOff.setText(str('OFF'))
            self.indiceOnOff.setEnabled(True)
            self.Habilitar_menique()
            self.Habilitar_anular()
            self.Habilitar_medio()
            self.Habilitar_pulgar()
            self.enviar_comando(f"S")

    def pulgarSpinBoxPwm(self, value):       
        self.valorVelocidadPulgar = value;

    def pulgarSliderPwm(self, value):
        self.valorEsperaPulgar=self.definirServos.convertirVelocidadValor(self.valorVelocidadPulgar)
        self.pulgar_valor.setText(str(value))        
        self.enviar_comando(f"1,{self.pulgarDerPin},{value},0,0,0,{self.valorEsperaPulgar}\n")
    
    def pulgarOnOffPwm(self):        
        if self.pulgarOnOff.isChecked()==True:
            self.etiquetaPulgarOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaPulgarOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.pulgarDerPin},0,0,0,0,0\n")
        else:
            self.etiquetaPulgarOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaPulgarOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.pulgarDerPin},0,0,0,0,0\n") 

    def pulgarPushButtonPwm(self):
        self.manoDerProgressBar.show()
        self.pulgarOnOff.setChecked(True)            
        self.etiquetaPulgarOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaPulgarOnOff.setText(str('ON')) 
        self.valorEsperaPulgar=self.definirServos.convertirVelocidadValor(self.valorVelocidadPulgar)
        self.pulgar_valor.setText(str(self.pulgarDerInicio))
        self.pulgarSlider.setValue(self.pulgarDerInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.pulgarDerPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.pulgarDerPin},{self.pulgarDerInicio},0,0,0,{self.valorEsperaPulgar}\n")        
        time.sleep(self.valorVelocidadPulgar/2)
        self.pulgarOnOff.setChecked(False)            
        self.etiquetaPulgarOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaPulgarOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.pulgarDerPin},0,0,0,0,0\n")
        self.manoDerProgressBar.hide()

    def pulgarBuclePwm(self):        
        if self.pulgarBucle.isChecked()==True:
            self.etiquetaPulgarBucle.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaPulgarBucle.setText(str('ON'))
            self.pulgarSlider.setEnabled(False)
            self.pulgarPushButton.setEnabled(False)
            self.pulgarSpinBox.setEnabled(False)
            self.pulgarOnOff.setChecked(True)
            self.etiquetaPulgarOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaPulgarOnOff.setText(str('ON'))          
            self.pulgarOnOff.setEnabled(False)
            self.Deshabilitar_menique()
            self.Deshabilitar_anular()
            self.Deshabilitar_medio()
            self.Deshabilitar_indice() 
            self.enviar_comando(f"4,{self.pulgarDerPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaPulgar=self.definirServos.convertirVelocidadValor(self.valorVelocidadPulgar)
            self.enviar_comando(f"6,{self.pulgarDerPin},{self.pulgarDerMinimo},{self.pulgarDerMaximo},{self.pulgarDerInicio},{self.pulgarDerRetraso},{self.valorEsperaPulgar}\n")
        else:
            self.etiquetaPulgarBucle.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaPulgarBucle.setText(str('OFF'))
            self.pulgarSlider.setEnabled(True)
            self.pulgarPushButton.setEnabled(True)
            self.pulgarSpinBox.setEnabled(True)
            self.pulgarOnOff.setChecked(False)
            self.etiquetaPulgarOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaPulgarOnOff.setText(str('OFF'))
            self.pulgarOnOff.setEnabled(True)
            self.Habilitar_menique()
            self.Habilitar_anular()
            self.Habilitar_medio()
            self.Habilitar_indice()
            self.enviar_comando(f"S")


    def enviar_comando(self, comando):
        self.arduino_der.write(comando.encode())
        print(f"Comando enviado: {comando}")        
        
    def Deshabilitar_menique(self):
        self.meniqueSlider.setEnabled(False)
        self.meniqueOnOff.setEnabled(False)
        self.meniqueBucle.setEnabled(False)
        self.meniqueSpinBox.setEnabled(False)
        self.meniquePushButton.setEnabled(False)
          
    def Deshabilitar_anular(self):
        self.anularSlider.setEnabled(False)
        self.anularOnOff.setEnabled(False)
        self.anularBucle.setEnabled(False)
        self.anularSpinBox.setEnabled(False)
        self.anularPushButton.setEnabled(False)        
          
    def Deshabilitar_medio(self):
        self.medioSlider.setEnabled(False)
        self.medioOnOff.setEnabled(False)
        self.medioBucle.setEnabled(False)
        self.medioSpinBox.setEnabled(False)
        self.medioPushButton.setEnabled(False)        
        
    def Deshabilitar_indice(self):
        self.indiceSlider.setEnabled(False)
        self.indiceOnOff.setEnabled(False)
        self.indiceBucle.setEnabled(False)
        self.indiceSpinBox.setEnabled(False)
        self.indicePushButton.setEnabled(False)        
        
    def Deshabilitar_pulgar(self):
        self.pulgarSlider.setEnabled(False)
        self.pulgarOnOff.setEnabled(False)
        self.pulgarBucle.setEnabled(False)
        self.pulgarSpinBox.setEnabled(False)
        self.pulgarPushButton.setEnabled(False)        
          
    def Habilitar_menique(self):
        self.meniqueSlider.setEnabled(True)
        self.meniqueOnOff.setEnabled(True)
        self.meniqueBucle.setEnabled(True)
        self.meniqueSpinBox.setEnabled(True)
        self.meniquePushButton.setEnabled(True)        
        
    def Habilitar_anular(self):
        self.anularSlider.setEnabled(True)
        self.anularOnOff.setEnabled(True)
        self.anularBucle.setEnabled(True)
        self.anularSpinBox.setEnabled(True)
        self.anularPushButton.setEnabled(True)                
        
    def Habilitar_medio(self):
        self.medioSlider.setEnabled(True)
        self.medioOnOff.setEnabled(True)
        self.medioBucle.setEnabled(True)
        self.medioSpinBox.setEnabled(True)
        self.medioPushButton.setEnabled(True)                
        
    def Habilitar_indice(self):
        self.indiceSlider.setEnabled(True)
        self.indiceOnOff.setEnabled(True)
        self.indiceBucle.setEnabled(True)
        self.indiceSpinBox.setEnabled(True)
        self.indicePushButton.setEnabled(True)                

    def Habilitar_pulgar(self):
        self.pulgarSlider.setEnabled(True)
        self.pulgarOnOff.setEnabled(True)
        self.pulgarBucle.setEnabled(True)
        self.pulgarSpinBox.setEnabled(True)
        self.pulgarPushButton.setEnabled(True)        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = DedosDerecha()
    my_app.show()
    sys.exit(app.exec_())
