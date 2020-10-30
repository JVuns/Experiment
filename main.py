class Car:
    def __init__ (self,model,speed,tank_capacity,fuel_usage):
        self.model = model
        self.speed = speed
        self.tank_capacity = tank_capacity
        self.fuel_usage = fuel_usage

car1 = Car("Model S", 50, 37, 8.5)
car2 = Car("Model 3", 45, 40, 10.2)
car3 = Car("Model X", 55, 46, 7.9)
car4 = Car("Rock", 50, 45, 9.4)

# company1 = Company("Tebsla", [car1, car2, car3])
print(car1.model)