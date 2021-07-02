class Coche():
    
    #propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    #comportamiento para los futuros objetos de la clase
    #Es decir, métodos
    def arrancar(self):
        #self en python viene a ser el this, pero tenemos
        #que ponerlo en los métodos como primer parámetro
        self.enmarcha = True
        print("rum-ruuum")
    
    def estado(self):
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

#Aqui se acaba la clase coche


#instanciamos un objeto, en python no usamos new
miCoche = Coche()
print(miCoche.estado())
miCoche.arrancar()
print(miCoche.estado())