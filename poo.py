class Coche():
  
    #constructor
    def __init__(self):
         #propiedades del objeto se pueden poner así
        self.largoChasis = 250
        self.anchoChasis = 120
        self.enmarcha = False

        #si queremos poner privada("encapsular") una variable con dos guiones bajos
        self.__ruedas = 4 #así no será accesible desde fuera de la clase
        self.__funcionPrvada()
        

    #comportamiento para los futuros objetos de la clase
    #Es decir, métodos
    def arrancar(self):
        #self en python viene a ser el this, pero tenemos
        #que ponerlo en los métodos como primer parámetro
        self.enmarcha = True
        print("rum-ruuum")
    
    #cuando recibe parámetros
    def arrancaDecideTu(self, arrancamos):
        self.enmarcha = arrancamos
        if (self.enmarcha):
            return "Arrancamos el coche"
        else:
            return "Paramos el coche"
            
    
    def estado(self):
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def __funcionPrvada(self):
        print("Analizo el coche")

#Aqui se acaba la clase coche


#instanciamos un objeto, en python no usamos new
miCoche = Coche()
print(miCoche.estado())
miCoche.arrancar()
print(miCoche.estado())

print(miCoche.arrancaDecideTu(True))
print(miCoche.arrancaDecideTu(False))