class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

#tenemos 3 clases con un método con el mismo nombre
#al recibir un objeto, sabe identificar a que función debe acudir
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)
    