class Arduino():
    def __init__(self):
        self.arduino_port_derecha = "/dev/ttyACM0" 
        self.baud_rate_der = 115200
        self.arduino_port_izquierda = "/dev/ttyACM1" 
        self.baud_rate_izq = 115200
    
    def arduinoPuertoDer(self):
        return self.arduino_port_derecha
    def arduinoBaudiosDer(self):
        return self.baud_rate_der
    def arduinoPuertoIzq(self):
        return self.arduino_port_izquierda
    def arduinoBaudiosIzq(self):
        return self.baud_rate_izq
    