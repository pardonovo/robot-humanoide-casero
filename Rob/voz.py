import threading
import subprocess
import serial
import time
from arduino import Arduino
from definirServos import DefinirServos

class Voz():
    def __init__(self):        
        self.arduino = Arduino()
        self.definirServos = DefinirServos()
        
        self.arduino_port_izquierda=self.arduino.arduinoPuertoIzq
        self.baud_rate_izq=self.arduino.arduinoBaudiosIzq
        self.arduino_izq = serial.Serial(self.arduino.arduino_port_izquierda, self.arduino.baud_rate_izq)
        time.sleep(2)
        
        # Datos servos boca
        self.bocaPin=self.definirServos.bocaPin
        self.bocaMinimo=self.definirServos.bocaMinimo
        self.bocaMaximo=self.definirServos.bocaMaximo
        self.bocaInicio=self.definirServos.bocaInicio
        self.bocaRetraso=self.definirServos.bocaRetraso

    def control_servo(self, comando):            
        self.arduino_izq.write(comando.encode())
        print(f"Comando enviado: {comando}")          
        
    def texto_a_voz(self,texto):    
        archivo_temporal = 'vozTextoTemporal.txt'
        with open(archivo_temporal, 'w', encoding='latin-1') as archivo:
            archivo.write(texto)
        
        archivo_salida = 'output.wav'
        velocidad_habla = 1.2 
        comando = f'text2wave -eval "(voice_JuntaDeAndalucia_es_pa_diphone)" -eval "(Parameter.set \'Duration_Stretch {velocidad_habla})" {archivo_temporal} -o {archivo_salida}'
    
        subprocess.run(comando, shell=True, check=True)
        
        ajuste_command = f'sox output.wav temp_adjusted.wav vol 1.0'
        subprocess.run(ajuste_command, shell=True, check=True)
        
        equalizar_command = 'sox temp_adjusted.wav temp_adjusted_equalized.wav equalizer 100 2.0q -40'
        subprocess.run(equalizar_command, shell=True, check=True)
       
        play_command = 'aplay temp_adjusted_equalized.wav'
        subprocess.run(play_command, shell=True, check=True)
        subprocess.run('rm vozTextoTemporal.txt output.wav temp_adjusted.wav temp_adjusted_equalized.wav', shell=True, check=True)
        
    def procesarVoz(self,texto_a_convertir):        
        self.control_servo(f"2,{self.bocaPin},0,0,0,0,0\n")
        time.sleep(0.3)
        self.control_servo(f"1,{self.bocaPin},{self.bocaInicio},0,0,0,13\n")
        
        voz_thread = threading.Thread(target=self.texto_a_voz, args=(texto_a_convertir,))
        voz_thread.start()
        time.sleep(1)
        while voz_thread.is_alive():
            if voz_thread.is_alive():
                for angulo in range(25, 65, 5):
                    self.control_servo(f"1,{self.bocaPin},{angulo},0,0,0,1\n")                               
                    #voz_thread.join(timeout=0.08)
            else:
                break;
            
            if voz_thread.is_alive():
                for angulo in range(65, 85, -5):
                    self.control_servo(f"1,{self.bocaPin},{angulo},0,0,0,1\n")                               
                    #voz_thread.join(timeout=0.05)
            else:
                break;
            
            if voz_thread.is_alive():
                for angulo in range(85, 25, 5):
                    self.control_servo(f"1,{self.bocaPin},{angulo},0,0,0,1\n")                                        
                    #voz_thread.join(timeout=0.05)
            else:
                break;
            
            voz_thread.join(timeout=0.01)    
                       
        voz_thread.join()        
        self.control_servo(f"1,{self.bocaPin},{self.bocaInicio},0,0,0,15\n")
        time.sleep(0.2)
        self.control_servo(f"3,{self.bocaPin},0,0,0,0,0\n")        