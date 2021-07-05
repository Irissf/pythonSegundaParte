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
    pass

#podemos ver que nos sale las propiedades de vehiculo ya que hereda de ésta
miMoto = Moto("Honda","CBR")
miMoto.arrancar()
miMoto.estado()
