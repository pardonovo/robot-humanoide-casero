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

class DedosIzquierda(QMainWindow):
    def __init__(self):
        super(DedosIzquierda,self).__init__()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, "dedosManoIzquierda.ui")
        loadUi(ui_file, self)       
         
        self.definirServos = DefinirServos()
        self.arduino = Arduino()
        self.servos = Servos()        
         
        # Inicialización de la conexión serial
        self.arduino_port_izquierda=self.arduino.arduinoPuertoIzq
        self.baud_rate_izq=self.arduino.arduinoBaudiosIzq
        self.arduino_izq = serial.Serial(self.arduino.arduino_port_izquierda, self.arduino.baud_rate_izq)
        time.sleep(2)  # Esperar a que se establezca la conexión            
        
        # Datos servos dedos
        self.meniqueIzqPin=self.definirServos.meniqueIzqPin
        self.meniqueIzqMinimo=self.definirServos.meniqueIzqMinimo
        self.meniqueIzqMaximo=self.definirServos.meniqueIzqMaximo
        self.meniqueIzqInicio=self.definirServos.meniqueIzqInicio
        self.meniqueIzqRetraso=self.definirServos.meniqueIzqRetraso
        self.anularIzqPin=self.definirServos.anularIzqPin
        self.anularIzqMinimo=self.definirServos.anularIzqMinimo
        self.anularIzqMaximo=self.definirServos.anularIzqMaximo
        self.anularIzqInicio=self.definirServos.anularIzqInicio
        self.anularIzqRetraso=self.definirServos.anularIzqRetraso
        self.medioIzqPin=self.definirServos.medioIzqPin
        self.medioIzqMinimo=self.definirServos.medioIzqMinimo
        self.medioIzqMaximo=self.definirServos.medioIzqMaximo
        self.medioIzqInicio=self.definirServos.medioIzqInicio
        self.medioIzqRetraso=self.definirServos.medioIzqRetraso
        self.indiceIzqPin=self.definirServos.indiceIzqPin
        self.indiceIzqMinimo=self.definirServos.indiceIzqMinimo
        self.indiceIzqMaximo=self.definirServos.indiceIzqMaximo
        self.indiceIzqInicio=self.definirServos.indiceIzqInicio
        self.indiceIzqRetraso=self.definirServos.indiceIzqRetraso
        self.pulgarIzqPin=self.definirServos.pulgarIzqPin
        self.pulgarIzqMinimo=self.definirServos.pulgarIzqMinimo
        self.pulgarIzqMaximo=self.definirServos.pulgarIzqMaximo
        self.pulgarIzqInicio=self.definirServos.pulgarIzqInicio
        self.pulgarIzqRetraso=self.definirServos.pulgarIzqRetraso            
        
        #Iniciar dedos
        self.servos.iniciarServoIzq(self.meniqueIzqPin,self.meniqueIzqInicio,self.meniqueIzqRetraso)
        self.servos.iniciarServoIzq(self.anularIzqPin,self.anularIzqInicio,self.anularIzqRetraso)
        self.servos.iniciarServoIzq(self.medioIzqPin,self.medioIzqInicio,self.medioIzqRetraso)
        self.servos.iniciarServoIzq(self.indiceIzqPin,self.indiceIzqInicio,self.indiceIzqRetraso)
        self.servos.iniciarServoIzq(self.pulgarIzqPin,self.pulgarIzqInicio,self.pulgarIzqRetraso)
        
        self.manoIzqProgressBar.hide()
        
        self.setWindowTitle("Dedos Mano Izquierda")

        # Botones de la barra superior
        self.click_posicion = QPoint()
        self.bt_close_mano_izq.clicked.connect(lambda: self.close())
        self.bt_minimize_mano_izq.clicked.connect(lambda: self.showMinimized())
    

        # Eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Sliders        
        self.meniqueSlider.setMinimum(self.meniqueIzqMinimo)
        self.meniqueSlider.setMaximum(self.meniqueIzqMaximo)
        self.menique_valor.setText(str(self.meniqueIzqInicio))
        self.meniqueSlider.setValue(self.meniqueIzqInicio)
        self.etiquetaMeniquePin.setText(self.meniqueIzqPin)
        self.etiquetaMeniqueMinimo.setText(str(self.meniqueIzqMinimo))
        self.etiquetaMeniqueMedio.setText(str(int(self.meniqueIzqMaximo/2)))
        self.etiquetaMeniqueMaximo.setText(str(self.meniqueIzqMaximo))
        self.meniqueSlider.valueChanged.connect(self.meniqueSliderPwm)
        self.valorVelocidadMenique=self.meniqueSpinBox.value()        
        self.meniqueSpinBox.valueChanged.connect(self.meniqueSpinBoxPwm)
        
        self.anularSlider.setMinimum(self.anularIzqMinimo)
        self.anularSlider.setMaximum(self.anularIzqMaximo)
        self.anular_valor.setText(str(self.anularIzqMinimo))
        self.etiquetaAnularPin.setText(self.anularIzqPin)
        self.etiquetaAnularMinimo.setText(str(self.anularIzqMinimo))
        self.etiquetaAnularMedio.setText(str(int(self.anularIzqMaximo/2)))
        self.etiquetaAnularMaximo.setText(str(self.anularIzqMaximo))
        self.anularSlider.valueChanged.connect(self.anularSliderPwm)
        self.valorVelocidadAnular=self.anularSpinBox.value()        
        self.anularSpinBox.valueChanged.connect(self.anularSpinBoxPwm)
       
        self.medioSlider.setMinimum(self.medioIzqMinimo)
        self.medioSlider.setMaximum(self.medioIzqMaximo)
        self.medio_valor.setText(str(self.medioIzqInicio))
        self.medioSlider.setValue(self.medioIzqInicio)
        self.etiquetaMedioPin.setText(self.medioIzqPin)
        self.etiquetaMedioMinimo.setText(str(self.medioIzqMinimo))
        self.etiquetaMedioMedio.setText(str(int(self.medioIzqMaximo/2)))
        self.etiquetaMedioMaximo.setText(str(self.medioIzqMaximo))
        self.medioSlider.valueChanged.connect(self.medioSliderPwm)
        self.valorVelocidadMedio=self.medioSpinBox.value()        
        self.medioSpinBox.valueChanged.connect(self.medioSpinBoxPwm)
        
        self.indiceSlider.setMinimum(self.indiceIzqMinimo)
        self.indiceSlider.setMaximum(self.indiceIzqMaximo)
        self.indice_valor.setText(str(self.indiceIzqInicio))
        self.indiceSlider.setValue(self.indiceIzqInicio)
        self.etiquetaIndicePin.setText(self.indiceIzqPin)
        self.etiquetaIndiceMinimo.setText(str(self.indiceIzqMinimo))
        self.etiquetaIndiceMedio.setText(str(int(self.indiceIzqMaximo/2)))
        self.etiquetaIndiceMaximo.setText(str(self.indiceIzqMaximo))
        self.indiceSlider.valueChanged.connect(self.indiceSliderPwm)
        self.valorVelocidadIndice=self.indiceSpinBox.value()        
        self.indiceSpinBox.valueChanged.connect(self.indiceSpinBoxPwm)
        
        self.pulgarSlider.setMinimum(self.pulgarIzqMinimo)
        self.pulgarSlider.setMaximum(self.pulgarIzqMaximo)
        self.pulgar_valor.setText(str(self.pulgarIzqMinimo))
        self.etiquetaPulgarPin.setText(self.pulgarIzqPin)
        self.etiquetaPulgarMinimo.setText(str(self.pulgarIzqMinimo))
        self.etiquetaPulgarMedio.setText(str(int(self.pulgarIzqMaximo/2)))
        self.etiquetaPulgarMaximo.setText(str(self.pulgarIzqMaximo))
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
        self.enviar_comando(f"1,{self.meniqueIzqPin},{value},0,0,0,{self.valorEsperaMenique}\n")
    
    def meniquePushButtonPwm(self):
        self.manoIzqProgressBar.show()
        self.meniqueOnOff.setChecked(True)            
        self.etiquetaMeniqueOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaMeniqueOnOff.setText(str('ON')) 
        self.valorEsperaMenique=self.definirServos.convertirVelocidadValor(self.valorVelocidadMenique)
        self.menique_valor.setText(str(self.meniqueIzqInicio))
        self.meniqueSlider.setValue(self.meniqueIzqInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.meniqueIzqPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.meniqueIzqPin},{self.meniqueIzqInicio},0,0,0,{self.valorEsperaMenique}\n")               
        time.sleep(self.valorVelocidadMenique/2)
        self.meniqueOnOff.setChecked(False)            
        self.etiquetaMeniqueOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaMeniqueOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.meniqueIzqPin},0,0,0,0,0\n")
        self.manoIzqProgressBar.hide()
    
    def meniqueOnOffPwm(self):        
        if self.meniqueOnOff.isChecked()==True:
            self.etiquetaMeniqueOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMeniqueOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.meniqueIzqPin},0,0,0,0,0\n")
        else:
            self.etiquetaMeniqueOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMeniqueOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.meniqueIzqPin},0,0,0,0,0\n") 
       
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
            self.enviar_comando(f"4,{self.meniqueIzqPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaMenique=self.definirServos.convertirVelocidadValor(self.valorVelocidadMenique)
            self.enviar_comando(f"6,{self.meniqueIzqPin},{self.meniqueIzqMinimo},{self.meniqueIzqMaximo},{self.meniqueIzqInicio},{self.meniqueIzqRetraso},{self.valorEsperaMenique}\n")
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
        self.enviar_comando(f"1,{self.anularIzqPin},{value},0,0,0,{self.valorEsperaAnular}\n")
        
    def anularPushButtonPwm(self):
        self.manoIzqProgressBar.show()
        self.anularOnOff.setChecked(True)            
        self.etiquetaAnularOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaAnularOnOff.setText(str('ON')) 
        self.valorEsperaAnular=self.definirServos.convertirVelocidadValor(self.valorVelocidadAnular)
        self.anular_valor.setText(str(self.anularIzqInicio))
        self.anularSlider.setValue(self.anularIzqInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.anularIzqPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.anularIzqPin},{self.anularIzqInicio},0,0,0,{self.valorEsperaAnular}\n")        
        time.sleep(self.valorVelocidadAnular/3)
        self.anularOnOff.setChecked(False)            
        self.etiquetaAnularOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaAnularOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.anularIzqPin},0,0,0,0,0\n")
        self.manoIzqProgressBar.hide()
        
    def anularOnOffPwm(self):        
        if self.anularOnOff.isChecked()==True:
            self.etiquetaAnularOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaAnularOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.anularIzqPin},0,0,0,0,0\n")
        else:
            self.etiquetaAnularOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaAnularOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.anularIzqPin},0,0,0,0,0\n")         

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
            self.enviar_comando(f"4,{self.anularIzqPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaAnular=self.definirServos.convertirVelocidadValor(self.valorVelocidadAnular)
            self.enviar_comando(f"6,{self.anularIzqPin},{self.anularIzqMinimo},{self.anularIzqMaximo},{self.anularIzqInicio},{self.anularIzqRetraso},{self.valorEsperaAnular}\n")
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
        self.enviar_comando(f"1,{self.medioIzqPin},{value},0,0,0,{self.valorEsperaMedio}\n")

    def medioPushButtonPwm(self):
        self.manoIzqProgressBar.show()
        self.medioOnOff.setChecked(True)            
        self.etiquetaMedioOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaMedioOnOff.setText(str('ON'))
        self.valorEsperaMedio=self.definirServos.convertirVelocidadValor(self.valorVelocidadMedio)
        self.medio_valor.setText(str(self.medioIzqInicio))
        self.medioSlider.setValue(self.medioIzqInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.medioIzqPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.medioIzqPin},{self.medioIzqInicio},0,0,0,{self.valorEsperaMedio}\n")        
        time.sleep(self.valorVelocidadMedio/2)
        self.medioOnOff.setChecked(False)            
        self.etiquetaMedioOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaMedioOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.medioIzqPin},0,0,0,0,0\n")
        self.manoIzqProgressBar.hide()

    def medioOnOffPwm(self):        
        if self.medioOnOff.isChecked()==True:
            self.etiquetaMedioOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaMedioOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.medioIzqPin},0,0,0,0,0\n")
        else:
            self.etiquetaMedioOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaMedioOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.medioIzqPin},0,0,0,0,0\n") 
       
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
            self.enviar_comando(f"4,{self.medioIzqPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaMedio=self.definirServos.convertirVelocidadValor(self.valorVelocidadMedio)
            self.enviar_comando(f"6,{self.medioIzqPin},{self.medioIzqMinimo},{self.medioIzqMaximo},{self.medioIzqInicio},{self.medioIzqRetraso},{self.valorEsperaMedio}\n")
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
        self.enviar_comando(f"1,{self.indiceIzqPin},{value},0,0,0,{self.valorEsperaIndice}\n")        
    
    def indiceOnOffPwm(self):        
        if self.indiceOnOff.isChecked()==True:
            self.etiquetaIndiceOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaIndiceOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.indiceIzqPin},0,0,0,0,0\n")
        else:
            self.etiquetaIndiceOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaIndiceOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.indiceIzqPin},0,0,0,0,0\n") 

    def indicePushButtonPwm(self):
        self.manoIzqProgressBar.show()
        self.indiceOnOff.setChecked(True)            
        self.etiquetaIndiceOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaIndiceOnOff.setText(str('ON')) 
        self.valorEsperaIndice=self.definirServos.convertirVelocidadValor(self.valorVelocidadIndice)
        self.indice_valor.setText(str(self.indiceIzqInicio))
        self.indiceSlider.setValue(self.indiceIzqInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.indiceIzqPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.indiceIzqPin},{self.indiceIzqInicio},0,0,0,{self.valorEsperaIndice}\n")        
        time.sleep(self.valorVelocidadIndice/2)
        self.indiceOnOff.setChecked(False)            
        self.etiquetaIndiceOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaIndiceOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.indiceIzqPin},0,0,0,0,0\n")
        self.manoIzqProgressBar.hide()

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
            self.enviar_comando(f"4,{self.indiceIzqPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaIndice=self.definirServos.convertirVelocidadValor(self.valorVelocidadIndice)
            self.enviar_comando(f"6,{self.indiceIzqPin},{self.indiceIzqMinimo},{self.indiceIzqMaximo},{self.indiceIzqInicio},{self.indiceIzqRetraso},{self.valorEsperaIndice}\n")
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
        self.enviar_comando(f"1,{self.pulgarIzqPin},{value},0,0,0,{self.valorEsperaPulgar}\n")
    
    def pulgarOnOffPwm(self):        
        if self.pulgarOnOff.isChecked()==True:
            self.etiquetaPulgarOnOff.setStyleSheet("color: green; margin-top: 6px;")
            self.etiquetaPulgarOnOff.setText(str('ON'))
            self.enviar_comando(f"2,{self.pulgarIzqPin},0,0,0,0,0\n")
        else:
            self.etiquetaPulgarOnOff.setStyleSheet("color: red; margin-top: 6px;")
            self.etiquetaPulgarOnOff.setText(str('OFF')) 
            self.enviar_comando(f"3,{self.pulgarIzqPin},0,0,0,0,0\n") 

    def pulgarPushButtonPwm(self):
        self.manoIzqProgressBar.show()
        self.pulgarOnOff.setChecked(True)            
        self.etiquetaPulgarOnOff.setStyleSheet("color: green; margin-top: 6px;")
        self.etiquetaPulgarOnOff.setText(str('ON')) 
        self.valorEsperaPulgar=self.definirServos.convertirVelocidadValor(self.valorVelocidadPulgar)
        self.pulgar_valor.setText(str(self.pulgarIzqInicio))
        self.pulgarSlider.setValue(self.pulgarIzqInicio)
        QApplication.processEvents()
        self.enviar_comando(f"2,{self.pulgarIzqPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.enviar_comando(f"1,{self.pulgarIzqPin},{self.pulgarIzqInicio},0,0,0,{self.valorEsperaPulgar}\n")        
        time.sleep(self.valorVelocidadPulgar/2)
        self.pulgarOnOff.setChecked(False)            
        self.etiquetaPulgarOnOff.setStyleSheet("color: red; margin-top: 6px;")
        self.etiquetaPulgarOnOff.setText(str('OFF')) 
        self.enviar_comando(f"3,{self.pulgarIzqPin},0,0,0,0,0\n")
        self.manoIzqProgressBar.hide()

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
            self.enviar_comando(f"4,{self.pulgarIzqPin},0,0,0,0,0\n")
            time.sleep(0.3)
            self.valorEsperaPulgar=self.definirServos.convertirVelocidadValor(self.valorVelocidadPulgar)
            self.enviar_comando(f"6,{self.pulgarIzqPin},{self.pulgarIzqMinimo},{self.pulgarIzqMaximo},{self.pulgarIzqInicio},{self.pulgarIzqRetraso},{self.valorEsperaPulgar}\n")
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
        self.arduino_izq.write(comando.encode())
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
    my_app = DedosIzquierda()
    my_app.show()
    sys.exit(app.exec_())
