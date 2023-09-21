#include <Servo.h>
#include <Adafruit_NeoPixel.h>

#define NUMPIXELS 16
#define MAXIMO_SERVOS   64
Servo servos[MAXIMO_SERVOS];

bool  servoBucle = false;
bool  neopixel = false;
bool  neopixelBucle = false;


Adafruit_NeoPixel pixels(NUMPIXELS, 24, NEO_GRB + NEO_KHZ800);
int losColores[20][3];

void setup() {  
  Serial.begin(115200); 
}

void loop() {
  
  if (Serial.available() > 0) {       
      String data = Serial.readStringUntil('\n');  
      // Variables para almacenar los datos recibidos
      int   comando;
      int   servoPin;
      int   grados;
      int   maxgrados;
      int   inicio;
      int   retraso;
      int   velocidad;

      const char* dataChars = data.c_str();            
      sscanf(dataChars, "%d,%d,%d,%d,%d,%d,%d", &comando, &servoPin, &grados, &maxgrados, &inicio, &retraso, &velocidad);
               
    if (comando == 2) { //Encender el servo        
      servos[servoPin].attach(servoPin);
    } else if (comando == 3) { //Apagar el servo     
      servos[servoPin].detach();
    } else if (comando == 1) { //Mover Servo                  
        servos[servoPin].write(grados);
        delay(velocidad);      
    } else if (comando == 4) { //Encender el bucle
        servos[servoPin].attach(servoPin);
        servoBucle = true;  
    } else if (comando == 5) { //Resetear servo
        servos[servoPin].attach(servoPin);
        servos[servoPin].write(inicio);
        delay(retraso);
        servos[servoPin].detach();                            
    } else if (comando == 6 && servoBucle==true) { //Mover el bucle
      if (servoPin==7 || servoPin==10 || servoPin==11 || servoPin==28 || servoPin==30 || servoPin==32 || servoPin==42 || servoPin==44 || servoPin==46){
        servos[servoPin].write(inicio); 
      } else {
        servos[servoPin].write(grados); 
      }                   
      delay(retraso); 
        int mover=0;           
      if (servoPin==7 || servoPin==10 || servoPin==11 || servoPin==28 || servoPin==30 || servoPin==32 || servoPin==42 || servoPin==44 || servoPin==46){
        mover=inicio;
      } else {
        mover=grados;
      }      
      String movimiento="adelante";
      int contadorBucle=1;
      while (servoBucle==true) {            
        char incoming = Serial.read();                   
        if (incoming == 'S') {         
          servos[servoPin].detach();
          servoBucle = false;                  
        }                                   
        servos[servoPin].write(mover);        
        delay(velocidad);             
        if (mover>maxgrados){
          if (contadorBucle>1) {
            if (velocidad==5){
              delay(retraso*3); 
            } else if(velocidad==13){
              delay(retraso*2);                
            } else {
              delay(retraso);  
            }           
          }          
          movimiento = "atras";         
        }
        if (mover<grados){
          if (contadorBucle>1) {
            if (velocidad==5){
              delay(retraso*3); 
            } else if(velocidad==13){
              delay(retraso*2); 
            } else {
              delay(retraso);  
            }       
          }              
          movimiento = "adelante";
        }
        if (movimiento=="adelante"){
          mover++;  
        } else if (movimiento=="atras"){
          mover--;
        }
        contadorBucle++;
      }
    } else if (comando == 7) { //Encender el neopixel  
        neopixel=true;      
        pixels.begin();
        for (int i = 0; i < NUMPIXELS; i++) {
          pixels.setPixelColor(i, pixels.Color(255, 255, 255));
        }  
        pixels.show(); 
    } else if (comando == 8) { //Apagar el neopixel        
        neopixel=false;
        pixels.clear();   
        pixels.show();            
    } else if (comando == 9 && neopixel==true) { //Cambiar el color neopixel
        for (int i = 0; i < NUMPIXELS; i++) {
          pixels.setPixelColor(i, pixels.Color(grados, maxgrados, inicio));
        }  
        pixels.show(); 
    } else if (comando == 10) { //Encender el bucle del neopixel
        pixels.begin();        
        pixels.show();                   
        neopixelBucle = true;                  
    }  else if (comando == 11 && neopixelBucle==true) { //Bucle del neopixel   
          int cuentacolor=0;          
          losColores[0][0]= 255; losColores[0][1]= 0;   losColores[0][2]= 0;
          losColores[1][0]= 255; losColores[1][1]= 165; losColores[1][2]= 0;
          losColores[2][0]= 255; losColores[2][1]= 0;   losColores[2][2]= 255;
          losColores[3][0]= 255; losColores[3][1]= 192; losColores[3][2]= 203;
          losColores[4][0]= 128; losColores[4][1]= 0;   losColores[4][2]= 128;
          losColores[5][0]= 0;   losColores[5][1]= 0;   losColores[5][2]= 128;
          losColores[6][0]= 0;   losColores[6][1]= 0;   losColores[6][2]= 255;
          losColores[7][0]= 133; losColores[7][1]= 193; losColores[7][2]= 233;
          losColores[8][0]= 0;   losColores[8][1]= 255; losColores[8][2]= 255;
          losColores[9][0]= 0;   losColores[9][1]= 128; losColores[9][2]= 0;
          losColores[10][0]= 0;  losColores[10][1]= 255; losColores[10][2]= 0;
          losColores[11][0]= 130; losColores[11][1]= 224; losColores[11][2]= 170;
          losColores[12][0]= 255; losColores[12][1]= 255; losColores[12][2]= 255;
          losColores[13][0]= 128; losColores[13][1]= 128; losColores[13][2]= 0;
          losColores[14][0]= 183; losColores[14][1]= 149; losColores[14][2]= 11;
          losColores[15][0]= 255; losColores[15][1]= 255; losColores[15][2]= 0;
          
          char incoming = "";
          while (neopixelBucle==true) { 
            incoming = Serial.read();                   
            if (incoming == 'R') {         
              pixels.begin();
              pixels.clear();
              pixels.show();  
              neopixelBucle = false;                  
            }                
            if (neopixelBucle==true){
              for (int i=0; i<NUMPIXELS; i++) {
                pixels.setPixelColor(i, pixels.Color(losColores[cuentacolor][0],losColores[cuentacolor][1],losColores[cuentacolor][2]));
                pixels.show();   
                delay(90);    
              }                                    
            } else {
              pixels.clear();   
              pixels.show(); 
            }
            cuentacolor++;
            if (cuentacolor>15){cuentacolor=0;}
        }
    } else if (comando == 12) { //Sensor de Humo
        int humoValor;
        humoValor= digitalRead(servoPin);  
        if (humoValor==0){
          Serial.println("HUMO");
        }
    }
  }
}
