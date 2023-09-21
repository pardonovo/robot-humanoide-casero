class DefinirServos():
    def __init__(self):
        # Definicion de pins y maximo y minimo
        
        #Dedos Derecha
        self.meniqueDerPin="2"
        self.meniqueDerMinimo=30
        self.meniqueDerMaximo=150
        self.meniqueDerInicio=30
        self.meniqueDerRetraso=300
        
        self.anularDerPin="3"
        self.anularDerMinimo=30
        self.anularDerMaximo=150
        self.anularDerInicio=30
        self.anularDerRetraso=750
        
        self.medioDerPin="4"
        self.medioDerMinimo=30
        self.medioDerMaximo=160
        self.medioDerInicio=30
        self.medioDerRetraso=350
        
        self.indiceDerPin="5"
        self.indiceDerMinimo=30
        self.indiceDerMaximo=150
        self.indiceDerInicio=30
        self.indiceDerRetraso=250
        
        self.pulgarDerPin="6"
        self.pulgarDerMinimo=20
        self.pulgarDerMaximo=130
        self.pulgarDerInicio=20
        self.pulgarDerRetraso=250
        
        #Dedos Izquierda
        self.meniqueIzqPin="2"
        self.meniqueIzqMinimo=30
        self.meniqueIzqMaximo=150
        self.meniqueIzqInicio=30
        self.meniqueIzqRetraso=300
        
        self.anularIzqPin="3"
        self.anularIzqMinimo=30
        self.anularIzqMaximo=150
        self.anularIzqInicio=30
        self.anularIzqRetraso=750
        
        self.medioIzqPin="4"
        self.medioIzqMinimo=10
        self.medioIzqMaximo=160
        self.medioIzqInicio=10
        self.medioIzqRetraso=350
        
        self.indiceIzqPin="5"
        self.indiceIzqMinimo=30
        self.indiceIzqMaximo=150
        self.indiceIzqInicio=30
        self.indiceIzqRetraso=250
        
        self.pulgarIzqPin="6"
        self.pulgarIzqMinimo=20
        self.pulgarIzqMaximo=130
        self.pulgarIzqInicio=20
        self.pulgarIzqRetraso=250
        
        #Brazo derecho
        self.munecaDerPin="7"
        self.munecaDerMinimo=10
        self.munecaDerMaximo=100
        self.munecaDerInicio=95
        self.munecaDerRetraso=250
        
        self.antebrazoDerPin="8"
        self.antebrazoDerMinimo=15
        self.antebrazoDerMaximo=120
        self.antebrazoDerInicio=15
        self.antebrazoDerRetraso=700
        
        self.brazoDerPin="11"
        self.brazoDerMinimo=0
        self.brazoDerMaximo=180
        self.brazoDerInicio=94
        self.brazoDerRetraso=3500
        
        self.rotacionDerPin="10"
        self.rotacionDerMinimo=10
        self.rotacionDerMaximo=135
        self.rotacionDerInicio=87
        self.rotacionDerRetraso=2000
        
        self.omoplatoDerPin="9"
        self.omoplatoDerMinimo=80
        self.omoplatoDerMaximo=170
        self.omoplatoDerInicio=80
        self.omoplatoDerRetraso=1600
        
        #Brazo izquierda
        self.munecaIzqPin="7"
        self.munecaIzqMinimo=10
        self.munecaIzqMaximo=100
        self.munecaIzqInicio=20
        self.munecaIzqRetraso=250
        
        self.antebrazoIzqPin="8"
        self.antebrazoIzqMinimo=55
        self.antebrazoIzqMaximo=165
        self.antebrazoIzqInicio=50
        self.antebrazoIzqRetraso=700
        
        self.brazoIzqPin="11"
        self.brazoIzqMinimo=20
        self.brazoIzqMaximo=180
        self.brazoIzqInicio=94
        self.brazoIzqRetraso=3500
        
        self.rotacionIzqPin="10"
        self.rotacionIzqMinimo=50
        self.rotacionIzqMaximo=130
        self.rotacionIzqInicio=90
        self.rotacionIzqRetraso=2000
        
        self.omoplatoIzqPin="9"
        self.omoplatoIzqMinimo=88
        self.omoplatoIzqMaximo=155
        self.omoplatoIzqInicio=88
        self.omoplatoIzqRetraso=1200
        
        #Cabeza
        self.rotacioncPin="42"
        self.rotacioncMinimo=10
        self.rotacioncMaximo=170
        self.rotacioncInicio=80
        self.rotacioncRetraso=300
        
        self.cabezaABPin="30"
        self.cabezaABMinimo=40
        self.cabezaABMaximo=135
        self.cabezaABInicio=105
        self.cabezaABRetraso=300
        
        self.cabezaDIPin="28"
        self.cabezaDIMinimo=20
        self.cabezaDIMaximo=160
        self.cabezaDIInicio=100
        self.cabezaDIRetraso=300
        
        self.ojosABPin="44"
        self.ojosABMinimo=70
        self.ojosABMaximo=110
        self.ojosABInicio=90
        self.ojosABRetraso=300
        
        self.ojosDIPin="46"
        self.ojosDIMinimo=60
        self.ojosDIMaximo=120
        self.ojosDIInicio=90
        self.ojosDIRetraso=300
        
        self.caderaPin="32"
        self.caderaMinimo=127
        self.caderaMaximo=143
        self.caderaInicio=135
        self.caderaRetraso=1000
        
        self.bocaPin="40"
        self.bocaMinimo=25
        self.bocaMaximo=90
        self.bocaInicio=25
        self.bocaRetraso=300
        
        self.anilloPin="24"        
        self.anilloInicio=128
        self.anilloRetraso=90

    #Dedos Mano Derecha
    def meniqueDerPin(self):
        return self.meniqueDerPin
    def meniqueDerMinimo(self):
        return self.meniqueDerMinimo
    def meniqueDerMaximo(self):
        return self.meniqueDerMaximo
    def meniqueDerInicio(self):
        return self.meniqueDerInicio
    def meniqueDerRetraso(self):
        return self.meniqueDerRetraso
    def anularDerPin(self):
        return self.anularDerPin
    def anularDerMinimo(self):
        return self.anularDerMinimo
    def anularDerMaximo(self):
        return self.anularDerMaximo
    def anularDerInicio(self):
        return self.anularDerInicio
    def anularDerRetraso(self):
        return self.anularDerRetraso
    def medioDerPin(self):
        return self.medioDerPin
    def medioDerMinimo(self):
        return self.medioDerMinimo
    def medioDerMaximo(self):
        return self.medioDerMaximo
    def medioDerInicio(self):
        return self.medioDerInicio    
    def medioDerRetraso(self):
        return self.medioDerRetraso
    def indiceDerPin(self):
        return self.indiceDerPin
    def indiceDerMinimo(self):
        return self.indiceDerMinimo
    def indiceDerMaximo(self):
        return self.indiceDerMaximo
    def indiceDerInicio(self):
        return self.indiceDerInicio
    def indiceDerRetraso(self):
        return self.indiceDerRetraso
    def pulgarDerPin(self):
        return self.pulgarDerPin
    def pulgarDerMinimo(self):
        return self.pulgarDerMinimo
    def pulgarDerMaximo(self):
        return self.pulgarDerMaximo
    def pulgarDerInicio(self):
        return self.pulgarDerInicio
    def pulgarDerRetraso(self):
        return self.pulgarDerRetraso

    #Dedos mano izquierda
    def meniqueIzqPin(self):
        return self.meniqueIzqPin
    def meniqueIzqMinimo(self):
        return self.meniqueIzqMinimo
    def meniqueIzqMaximo(self):
        return self.meniqueIzqMaximo
    def meniqueIzqInicio(self):
        return self.meniqueIzqInicio
    def meniqueIzqRetraso(self):
        return self.meniqueIzqRetraso
    def anularIzqPin(self):
        return self.anularIzqPin
    def anularIzqMinimo(self):
        return self.anularIzqMinimo
    def anularIzqMaximo(self):
        return self.anularIzqMaximo
    def anularIzqInicio(self):
        return self.anularIzqInicio
    def anularIzqRetraso(self):
        return self.anularIzqRetraso
    def medioIzqPin(self):
        return self.medioIzqPin
    def medioIzqMinimo(self):
        return self.medioIzqMinimo
    def medioIzqMaximo(self):
        return self.medioIzqMaximo
    def medioIzqInicio(self):
        return self.medioIzqInicio    
    def medioIzqRetraso(self):
        return self.medioIzqRetraso
    def indiceIzqPin(self):
        return self.indiceIzqPin
    def indiceIzqMinimo(self):
        return self.indiceIzqMinimo
    def indiceIzqMaximo(self):
        return self.indiceIzqMaximo
    def indiceIzqInicio(self):
        return self.indiceIzqInicio
    def indiceIzqRetraso(self):
        return self.indiceIzqRetraso
    def pulgarIzqPin(self):
        return self.pulgarIzqPin
    def pulgarIzqMinimo(self):
        return self.pulgarIzqMinimo
    def pulgarIzqMaximo(self):
        return self.pulgarIzqMaximo
    def pulgarIzqInicio(self):
        return self.pulgarIzqInicio
    def pulgarIzqRetraso(self):
        return self.pulgarIzqRetraso
    
        #Brazo derecho
    def munecaDerPin(self):
        return self.munecaDerPin
    def munecaDerMinimo(self):
        return self.munecaDerMinimo
    def munecaDerMaximo(self):
        return self.munecaDerMaximo
    def munecaDerInicio(self):
        return self.munecaDerInicio
    def munecaDerRetraso(self):
        return self.munecaDerRetraso
    def antebrazoDerPin(self):
        return self.antebrazoDerPin
    def antebrazoDerMinimo(self):
        return self.antebrazoDerMinimo
    def antebrazoDerMaximo(self):
        return self.antebrazoDerMaximo
    def antebrazoDerInicio(self):
        return self.antebrazoDerInicio
    def antebrazoDerRetraso(self):
        return self.antebrazoDerRetraso
    def brazoDerPin(self):
        return self.brazoDerPin
    def brazoDerMinimo(self):
        return self.brazoDerMinimo
    def brazoDerMaximo(self):
        return self.brazoDerMaximo
    def brazoDerInicio(self):
        return self.brazoDerInicio
    def brazoDerRetraso(self):
        return self.brazoDerRetraso
    def rotacionDerPin(self):
        return self.rotacionDerPin
    def rotacionDerMinimo(self):
        return self.rotacionDerMinimo
    def rotacionDerMaximo(self):
        return self.rotacionDerMaximo
    def rotacionDerInicio(self):
        return self.rotacionDerInicio
    def rotacionDerRetraso(self):
        return self.rotacionDerRetraso
    def omoplatoDerPin(self):
        return self.omoplatoDerPin
    def omoplatoDerMinimo(self):
        return self.omoplatoDerMinimo
    def omoplatoDerMaximo(self):
        return self.omoplatoDerMaximo
    def omoplatoDerInicio(self):
        return self.omoplatoDerInicio
    def omoplatoDerRetraso(self):
        return self.omoplatoDerRetraso
    
    #Brazo izquierdo
    def munecaIzqPin(self):
        return self.munecaIzqPin
    def munecaIzqMinimo(self):
        return self.munecaIzqMinimo
    def munecaIzqMaximo(self):
        return self.munecaIzqMaximo
    def munecaIzqInicio(self):
        return self.munecaIzqInicio
    def munecaIzqRetraso(self):
        return self.munecaIzqRetraso
    def antebrazoIzqPin(self):
        return self.antebrazoIzqPin
    def antebrazoIzqMinimo(self):
        return self.antebrazoIzqMinimo
    def antebrazoIzqMaximo(self):
        return self.antebrazoIzqMaximo
    def antebrazoIzqInicio(self):
        return self.antebrazoIzqInicio
    def antebrazoIzqRetraso(self):
        return self.antebrazoIzqRetraso
    def brazoIzqPin(self):
        return self.brazoIzqPin
    def brazoIzqMinimo(self):
        return self.brazoIzqMinimo
    def brazoIzqMaximo(self):
        return self.brazoIzqMaximo
    def brazoIzqInicio(self):
        return self.brazoIzqInicio
    def brazoIzqRetraso(self):
        return self.brazoIzqRetraso
    def rotacionIzqPin(self):
        return self.rotacionIzqPin
    def rotacionIzqMinimo(self):
        return self.rotacionIzqMinimo
    def rotacionIzqMaximo(self):
        return self.rotacionIzqMaximo
    def rotacionIzqInicio(self):
        return self.rotacionIzqInicio
    def rotacionIzqRetraso(self):
        return self.rotacionIzqRetraso
    def omoplatoIzqPin(self):
        return self.omoplatoIzqPin
    def omoplatoIzqMinimo(self):
        return self.omoplatoIzqMinimo
    def omoplatoIzqMaximo(self):
        return self.omoplatoIzqMaximo
    def omoplatoIzqInicio(self):
        return self.omoplatoIzqInicio
    def omoplatoIzqRetraso(self):
        return self.omoplatoIzqRetraso
    
    #Cabeza
    def rotacioncPin(self):
        return self.rotacioncPin
    def rotacioncMinimo(self):
        return self.rotacioncMinimo
    def rotacioncMaximo(self):
        return self.rotacioncMaximo
    def rotacioncInicio(self):
        return self.rotacioncInicio
    def rotacioncRetraso(self):
        return self.rotacioncRetraso    
    def cabezaABPin(self):
        return self.cabezaABPin
    def cabezaABMinimo(self):
        return self.cabezaABMinimo
    def cabezaABMaximo(self):
        return self.cabezaABMaximo
    def cabezaABInicio(self):
        return self.cabezaABInicio
    def cabezaABRetraso(self):
        return self.cabezaABRetraso
    def cabezaDIPin(self):
        return self.cabezaDIPin
    def cabezaDIMinimo(self):
        return self.cabezaDIMinimo
    def cabezaDIMaximo(self):
        return self.cabezaDIMaximo
    def cabezaDIInicio(self):
        return self.cabezaDIInicio
    def cabezaDIRetraso(self):
        return self.cabezaDIRetraso
    def ojosABPin(self):
        return self.ojosABPin
    def ojosABMinimo(self):
        return self.ojosABMinimo
    def ojosABMaximo(self):
        return self.ojosABMaximo
    def ojosABInicio(self):
        return self.ojosABInicio
    def ojosABRetraso(self):
        return self.ojosABRetraso
    def ojosDIPin(self):
        return self.ojosDIPin
    def ojosDIMinimo(self):
        return self.ojosDIMinimo
    def ojosDIMaximo(self):
        return self.ojosDIMaximo
    def ojosDIInicio(self):
        return self.ojosDIInicio
    def ojosDIRetraso(self):
        return self.ojosDIRetraso
    def caderaPin(self):
        return self.caderaPin
    def caderaMinimo(self):
        return self.caderaMinimo
    def caderaMaximo(self):
        return self.caderaMaximo
    def caderaInicio(self):
        return self.caderaInicio
    def caderaRetraso(self):
        return self.caderaRetraso
    def bocaPin(self):
        return self.bocaPin
    def bocaMinimo(self):
        return self.bocaMinimo
    def bocaMaximo(self):
        return self.bocaMaximo
    def bocaInicio(self):
        return self.bocaInicio
    def bocaRetraso(self):
        return self.bocaRetraso
    
    def convertirVelocidadValor(self,valorBox):       
        self.valorEspera=30
        if valorBox==1:
            self.valorEspera=130
        if valorBox==2:
            self.valorEspera=75
        if valorBox==3:
            self.valorEspera=30
        if valorBox==4:
            self.valorEspera=13
        if valorBox==5:
            self.valorEspera=5
        return self.valorEspera
        