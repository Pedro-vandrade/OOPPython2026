

class Truck:

    def __init__(self, model, plate, maxpayload,currentpayload):
        self.model = model
        self.plate = plate
        self.maxpayload = maxpayload
        self.currentpayload = currentpayload

    def truckinfo(self):
        print(f'Truck Model: {self.model}')
        print(f'Plate: {self.plate}')
        print(f'Max Payload: {self.maxpayload} KG.')

    def loadcargo(self):
        print('-' * 20)
        while True:
            try:
                cargo = float(input("Inform the cargo payload: " ))
                if cargo < 0:
                    print("Cargo needs to be over 0 KG.")
                    continue

                if self.currentpayload + cargo > self.maxpayload:
                    print(f'Max payload is exceeded. Max payload is {self.maxpayload}.')
                    continue
                else:
                    self.currentpayload += cargo
                    print(f'Cargo loaded succesfully. Current payload is {self.currentpayload} KG.')
                    break
            except ValueError:
                print('Numbers only.\n')

    def unloadcargo(self):
        print('-' * 20)

        while True:
            try:
                minuscargo = float(input("Inform how much cargo will be unloaded (KG only): "))
                if minuscargo < 0:
                    print("Cargo needs to be over 0 KG.")
                    continue

                if minuscargo > self.currentpayload:
                    print(f"Error: Cannot unload {minuscargo} KG. Current payload is only {self.currentpayload} KG.")
                    continue
                else:
                    self.currentpayload -= minuscargo
                    print(f'Cargo unloaded sucessfully. Current payload is {self.currentpayload}')
                    break


            except ValueError:
                print('Numbers only.')

class Driver:
    def __init__(self,name, age, driverlivence,dlexpiration, truck=None):
        self.name = name
        self.age = age
        self.driverlicense = driverlivence
        self.dlexpiration = dlexpiration
        self.truck = truck

    def driving(self):
        # self.truck.truckinfo()
        print(f'Current driver: {self.name} on truck {self.truck.model}')




truck1 = Truck('Scania', 1568, 50000, 55 )
driver1 = Driver('Tommy', 55, 1520, '19/12/2028', truck1)
truck1.truckinfo()
truck1.loadcargo()
truck1.unloadcargo()
driver1.driving()