import serial
import time
from arduino import Arduino

class Servos():
    def __init__(self):
        self.arduino = Arduino()
        
        self.arduino_port_derecha=self.arduino.arduinoPuertoDer
        self.baud_rate_der=self.arduino.arduinoBaudiosDer
        self.arduino_der = serial.Serial(self.arduino.arduino_port_derecha, self.arduino.baud_rate_der)
        time.sleep(2)
        
        self.arduino_port_izquierda=self.arduino.arduinoPuertoIzq
        self.baud_rate_izq=self.arduino.arduinoBaudiosIzq
        self.arduino_izq = serial.Serial(self.arduino.arduino_port_izquierda, self.arduino.baud_rate_izq)
        time.sleep(2)
         
    def iniciarServoDer(self,pin=0,inicio=False,espera=0):
        comando=(f"5,{pin},0,0,{inicio},{espera},15\n")
        self.arduino_der.write(comando.encode())
        print(f"Iniciar enviado: {comando}")
        return

    def iniciarServoIzq(self,pin=0,inicio=False,espera=0):
        comando=(f"5,{pin},0,0,{inicio},{espera},15\n")
        self.arduino_izq.write(comando.encode())
        print(f"Iniciar enviado: {comando}")
        return
    
    
        