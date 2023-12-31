import serial
import time
from voz import Voz
from arduino import Arduino
from definirServos import DefinirServos

class Testprueba():
    def __init__(self):
        self.arduino = Arduino()
        self.definirServos = DefinirServos()
        self.voz= Voz()
        
        self.arduino_port_derecha=self.arduino.arduinoPuertoDer
        self.baud_rate_der=self.arduino.arduinoBaudiosDer
        self.arduino_der = serial.Serial(self.arduino.arduino_port_derecha, self.arduino.baud_rate_der)
        time.sleep(2)
        
        self.arduino_port_izquierda=self.arduino.arduinoPuertoIzq
        self.baud_rate_izq=self.arduino.arduinoBaudiosIzq
        self.arduino_izq = serial.Serial(self.arduino.arduino_port_izquierda, self.arduino.baud_rate_izq)
        time.sleep(2)

    def comenzarTest(self):
        texto = "Comienzo del test de prueba, de los sistemas del robot"
        self.voz.procesarVoz(texto)
        time.sleep(1)
        
        texto = "Testeo de los dedos de la mano derecha"
        self.voz.procesarVoz(texto)
        time.sleep(1)
        self.cerrarManoDerecha()
        time.sleep(2)
        self.abrirManoDerecha()
        time.sleep(2)       
        texto = "Testeo de los dedos de la mano izquierda"
        self.voz.procesarVoz(texto)
        time.sleep(1)
        self.cerrarManoIzquierda()
        time.sleep(2)
        self.abrirManoIzquierda()
        time.sleep(2)
        texto = "Testeo de los dedos de ambas manos"
        self.voz.procesarVoz(texto)
        time.sleep(1)
        self.cerrarManoDerecha()
        self.cerrarManoIzquierda()
        time.sleep(2)
        self.abrirManoDerecha()
        self.abrirManoIzquierda()
        time.sleep(1)
        self.apagarManoDerecha()
        self.apagarManoIzquierda()
        
        texto = "Testeo de los brazos"
        self.voz.procesarVoz(texto)
        time.sleep(1)
        self.brazos()
        
        texto = "Testeo de la cadera"
        self.voz.procesarVoz(texto)
        time.sleep(1)
        self.cadera()
        texto = "Testeo de la cabeza"
        self.voz.procesarVoz(texto)
        self.cabeza()
        time.sleep(1)
        texto = "Testeo del anillo de leds"
        self.voz.procesarVoz(texto)
        self.led()
        
        time.sleep(1)
        texto = "Testeo finalizado"
        self.voz.procesarVoz(texto)
        return
        

    def cerrarManoDerecha(self):
        comando=(f"2,{self.definirServos.meniqueDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.meniqueDerPin},{self.definirServos.meniqueDerMaximo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        
        comando=(f"2,{self.definirServos.anularDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.anularDerPin},{self.definirServos.anularDerMaximo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        
        comando=(f"2,{self.definirServos.medioDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.medioDerPin},{self.definirServos.medioDerMaximo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        
        comando=(f"2,{self.definirServos.indiceDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.indiceDerPin},{self.definirServos.indiceDerMaximo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        
        comando=(f"2,{self.definirServos.pulgarDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.pulgarDerPin},{self.definirServos.pulgarDerMaximo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())        
        return        

    def abrirManoDerecha(self):
        comando=(f"2,{self.definirServos.meniqueDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.meniqueDerPin},{self.definirServos.meniqueDerMinimo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        
        comando=(f"2,{self.definirServos.anularDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.anularDerPin},{self.definirServos.anularDerMinimo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        
        comando=(f"2,{self.definirServos.medioDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.medioDerPin},{self.definirServos.medioDerMinimo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        
        comando=(f"2,{self.definirServos.indiceDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.indiceDerPin},{self.definirServos.indiceDerMinimo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        
        comando=(f"2,{self.definirServos.pulgarDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.pulgarDerPin},{self.definirServos.pulgarDerMinimo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())        
        return
    
    def apagarManoDerecha(self):
        comando=(f"3,{self.definirServos.meniqueDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"3,{self.definirServos.anularDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"3,{self.definirServos.medioDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"3,{self.definirServos.indiceDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"3,{self.definirServos.pulgarDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())        
        return

    def cerrarManoIzquierda(self):
        comando=(f"2,{self.definirServos.meniqueIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.meniqueIzqPin},{self.definirServos.meniqueIzqMaximo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        
        comando=(f"2,{self.definirServos.anularIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.anularIzqPin},{self.definirServos.anularIzqMaximo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        
        comando=(f"2,{self.definirServos.medioIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.medioIzqPin},{self.definirServos.medioIzqMaximo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        
        comando=(f"2,{self.definirServos.indiceIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.indiceIzqPin},{self.definirServos.indiceIzqMaximo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        
        comando=(f"2,{self.definirServos.pulgarIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.pulgarIzqPin},{self.definirServos.pulgarIzqMaximo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())        
        return        

    def abrirManoIzquierda(self):
        comando=(f"2,{self.definirServos.meniqueIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.meniqueIzqPin},{self.definirServos.meniqueIzqMinimo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        
        comando=(f"2,{self.definirServos.anularIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.anularIzqPin},{self.definirServos.anularIzqMinimo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        
        comando=(f"2,{self.definirServos.medioIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.medioIzqPin},{self.definirServos.medioIzqMinimo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        
        comando=(f"2,{self.definirServos.indiceIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.indiceIzqPin},{self.definirServos.indiceIzqMinimo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        
        comando=(f"2,{self.definirServos.pulgarIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.pulgarIzqPin},{self.definirServos.pulgarIzqMinimo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())        
        return
    
    def apagarManoIzquierda(self):
        comando=(f"3,{self.definirServos.meniqueIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"3,{self.definirServos.anularIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"3,{self.definirServos.medioIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"3,{self.definirServos.indiceIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"3,{self.definirServos.pulgarIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        return
        
    def brazos(self):
        
        comando=(f"2,{self.definirServos.antebrazoDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"2,{self.definirServos.antebrazoIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.antebrazoDerPin},{self.definirServos.antebrazoDerMaximo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.antebrazoIzqPin},{self.definirServos.antebrazoIzqMaximo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        comando=(f"2,{self.definirServos.munecaDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"2,{self.definirServos.munecaIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.munecaDerPin},{self.definirServos.munecaDerMinimo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.munecaIzqPin},{self.definirServos.munecaIzqMaximo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        comando=(f"1,{self.definirServos.munecaDerPin},{self.definirServos.munecaDerInicio},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.munecaIzqPin},{self.definirServos.munecaIzqInicio},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(2)
        
        comando=(f"2,{self.definirServos.brazoDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"2,{self.definirServos.brazoIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.brazoDerPin},{self.definirServos.brazoDerMaximo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.brazoIzqPin},{self.definirServos.brazoIzqMaximo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(2)
        comando=(f"1,{self.definirServos.antebrazoDerPin},{self.definirServos.antebrazoDerMinimo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.antebrazoIzqPin},{self.definirServos.antebrazoIzqMinimo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(3)
        
        comando=(f"2,{self.definirServos.rotacionDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"2,{self.definirServos.rotacionIzqPin},0,0,0,0,0\n")
        print(f"Comando enviado: {comando}") 
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.rotacionDerPin},{self.definirServos.rotacionDerMinimo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.rotacionIzqPin},{self.definirServos.rotacionIzqMinimo},0,0,0,15\n")
        print(f"Comando enviado: {comando}") 
        self.arduino_izq.write(comando.encode())
        time.sleep(3)
        comando=(f"1,{self.definirServos.rotacionDerPin},{self.definirServos.rotacionDerInicio},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.rotacionIzqPin},{self.definirServos.rotacionIzqInicio},0,0,0,15\n")
        print(f"Comando enviado: {comando}") 
        self.arduino_izq.write(comando.encode())
        time.sleep(3)
        comando=(f"1,{self.definirServos.rotacionDerPin},{self.definirServos.rotacionDerMaximo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.rotacionIzqPin},{self.definirServos.rotacionIzqMaximo},0,0,0,15\n")
        time.sleep(0.3)
        self.arduino_izq.write(comando.encode())
        time.sleep(3)
        comando=(f"1,{self.definirServos.rotacionDerPin},{self.definirServos.rotacionDerInicio},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.rotacionIzqPin},{self.definirServos.rotacionIzqInicio},0,0,0,15\n")
        time.sleep(0.3)
        self.arduino_izq.write(comando.encode())
        time.sleep(4)
        
        comando=(f"2,{self.definirServos.omoplatoDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"2,{self.definirServos.omoplatoIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.brazoDerPin},{self.definirServos.brazoDerInicio},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.brazoIzqPin},{self.definirServos.brazoIzqInicio},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"1,{self.definirServos.omoplatoDerPin},{self.definirServos.omoplatoDerMaximo},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.omoplatoIzqPin},{self.definirServos.omoplatoIzqMaximo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(7)
        comando=(f"1,{self.definirServos.omoplatoDerPin},{self.definirServos.omoplatoDerInicio},0,0,0,15\n")
        self.arduino_der.write(comando.encode())
        comando=(f"1,{self.definirServos.omoplatoIzqPin},{self.definirServos.omoplatoIzqInicio},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        
        time.sleep(6)
        comando=(f"3,{self.definirServos.munecaIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"3,{self.definirServos.munecaDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"3,{self.definirServos.antebrazoIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"3,{self.definirServos.antebrazoDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"3,{self.definirServos.brazoIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"3,{self.definirServos.brazoDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"3,{self.definirServos.rotacionIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"3,{self.definirServos.rotacionDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        comando=(f"3,{self.definirServos.omoplatoIzqPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"3,{self.definirServos.omoplatoDerPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        return
    
    def cadera(self):        
        comando=(f"2,{self.definirServos.caderaPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.caderaPin},{self.definirServos.caderaInicio},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"1,{self.definirServos.caderaPin},{self.definirServos.caderaMaximo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(2)
        comando=(f"1,{self.definirServos.caderaPin},{self.definirServos.caderaInicio},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(2)
        comando=(f"1,{self.definirServos.caderaPin},{self.definirServos.caderaMinimo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(2)
        comando=(f"1,{self.definirServos.caderaPin},{self.definirServos.caderaInicio},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(2)
        comando=(f"3,{self.definirServos.caderaPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        return
        
    def cabeza(self):
        comando=(f"2,{self.definirServos.rotacioncPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.rotacioncPin},{self.definirServos.rotacioncInicio},0,0,0,50\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"1,{self.definirServos.rotacioncPin},{self.definirServos.rotacioncMinimo},0,0,0,50\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        comando=(f"1,{self.definirServos.rotacioncPin},{self.definirServos.rotacioncInicio},0,0,0,50\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        comando=(f"1,{self.definirServos.rotacioncPin},{self.definirServos.rotacioncMaximo},0,0,0,50\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        comando=(f"1,{self.definirServos.rotacioncPin},{self.definirServos.rotacioncInicio},0,0,0,50\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        
        comando=(f"2,{self.definirServos.cabezaABPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.cabezaABPin},{self.definirServos.cabezaABInicio},0,0,0,20\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"1,{self.definirServos.cabezaABPin},{self.definirServos.cabezaABMinimo},0,0,0,20\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        comando=(f"1,{self.definirServos.cabezaABPin},{self.definirServos.cabezaABInicio},0,0,0,20\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        comando=(f"1,{self.definirServos.cabezaABPin},{self.definirServos.cabezaABMaximo},0,0,0,20\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        comando=(f"1,{self.definirServos.cabezaABPin},{self.definirServos.cabezaABInicio},0,0,0,20\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        
        comando=(f"2,{self.definirServos.cabezaDIPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(0.3)
        comando=(f"1,{self.definirServos.cabezaDIPin},{self.definirServos.cabezaDIInicio},0,0,0,20\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"1,{self.definirServos.cabezaDIPin},{self.definirServos.cabezaDIMinimo},0,0,0,20\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        comando=(f"1,{self.definirServos.cabezaDIPin},{self.definirServos.cabezaDIInicio},0,0,0,20\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        comando=(f"1,{self.definirServos.cabezaDIPin},{self.definirServos.cabezaDIMaximo},0,0,0,20\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        comando=(f"1,{self.definirServos.cabezaDIPin},{self.definirServos.cabezaDIInicio},0,0,0,20\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        
        comando=(f"1,{self.definirServos.cabezaABPin},{self.definirServos.cabezaDIMaximo},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"1,{self.definirServos.rotacioncPin},40,0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"1,{self.definirServos.cabezaDIPin},55,0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(2)
        comando=(f"1,{self.definirServos.cabezaABPin},{self.definirServos.cabezaABInicio},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"1,{self.definirServos.rotacioncPin},{self.definirServos.rotacioncInicio},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"1,{self.definirServos.cabezaDIPin},{self.definirServos.cabezaDIInicio},0,0,0,15\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)
        
        comando=(f"3,{self.definirServos.rotacioncPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"3,{self.definirServos.cabezaABPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        comando=(f"3,{self.definirServos.cabezaDIPin},0,0,0,0,0\n")
        self.arduino_izq.write(comando.encode())
        time.sleep(1)                        
        return
    
    def led(self):
        comando=(f"7,{self.definirServos.anilloPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)  
        comando=(f"10,{self.definirServos.anilloPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(0.3)  
        comando=(f"11,{self.definirServos.anilloPin},0,0,0,0,0\n")
        self.arduino_der.write(comando.encode())
        time.sleep(8)
        comando=(f"R")
        self.arduino_der.write(comando.encode())
        return