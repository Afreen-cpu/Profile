print("Afreen - 03")
class Car:
    
    brand = ""
    model = ""
    
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


car1 = Car()
car1.brand = "Toyota"
car1.model = "Corolla"


car1.display_info()
