#Class of Vehicle

class vehicle:
    def __init__ (self, model, year):
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.model} made in {self.year} is starting")
    
    def stop(self):
        print(f"{self.model} made in {self.year} is stopping")

Vehicle1 = vehicle("Toyota", 2020)
Vehicle2 = vehicle("Honda", 2019)

Vehicle1.start()
Vehicle1.stop()
Vehicle2.start()
Vehicle2.stop()
