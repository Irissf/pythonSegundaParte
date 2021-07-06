class Vehiculo():

    #constructor
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    
    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelerar = True

    def frenar(self):
        self.frenar = True
    
    def estado(self):
        print ("Marca: ",self.marca, "\nModelo: ",self.modelo,
        "\nAcelerado: ",self.acelera, "\nFrenado: ",self.frena,
        "\nEn marcha: ",self.enmarcha)


#Al poner Vehiculo en los paréntesis, decimos que hereda de vehiculo
class Moto(Vehiculo):
    hacerCaballito = ""
    
    def caballito(self):
        self.hacerCaballito = "voy haciendo el caballito"

    #Sobreescribir para que muestre si hace el caballito
    #consiste en poner el mismo nombre que la clase padre y los mismo parámetros más los nuevos
    def estado(self):
        print ("Marca: ",self.marca, "\nModelo: ",self.modelo,
        "\nAcelerado: ",self.acelera, "\nFrenado: ",self.frena,
        "\nEn marcha: ",self.enmarcha, "\nCaballito :", self.hacerCaballito)
        

#¿Qué pasa si por ejemplo ahora queremos vehiculos eléctricos?
class VElectricos():
    def __init__(self, marca, modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100
    
    def cargaEnergia(self):
        self.cagando = True

#Y tenemos una bicicleta eléctrica que hereda de ambas, vehículo y vElectrico
class BiciElectrica(VElectricos,Vehiculo):
    pass


#podemos ver que nos sale las propiedades de vehiculo ya que hereda de ésta
miMoto = Moto("Honda","CBR")
miMoto.caballito()
miMoto.arrancar()
miMoto.estado()
print()

#Podemos ver que ambas clases de las que hereda tienen un contructor con parámetros
#pues usamos las de la primera clase que usa la clase, en este caso VElectrico
#miBici = BiciElectrica()
#para pasar marca y modelo usamos super() en VElectricos
miBici = BiciElectrica("Bomda","Hg223")
miBici.estado()


