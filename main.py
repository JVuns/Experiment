class Car:
    def __init__ (self,model,speed,tank_capacity,fuel_usage):
        self.model = model
        self.speed = speed
        self.tank_capacity = tank_capacity
        self.fuel_usage = fuel_usage
        
    
    def max_distance(self):
        return(self.tank_capacity * 100/self.fuel_usage)
    def max_duration(self):
        return(self.max_distance() / self.speed)#hour unit
    def is_better_than(self, other_car):
        if self.max_distance() > other_car.max_distance() and self.max_duration() > other_car.max_duration():
            return "yes"
        elif self.max_distance() < other_car.max_distance() and self.max_duration() < other_car.max_duration():
            return "no"
        else:
            return "maybe"
    def compare_cars(self, other_company):
        low = 0
        high= 0
        for a in other_company:
            if self.is_better_than(a) == "yes":
                low += 1
                high += 1
            elif self.is_better_than(a) == "no":
                high += 1
        return (f"Our car, {self.model} is better than {low} out of {high} of all the cars in {other_company} company.")

class Company():
    def __init__(self, name, cars):
        self.name = name
        self.cars = cars

car1 = Car("Model S", 50, 37, 8.5)
car2 = Car("Model 3", 45, 40, 10.2)
car3 = Car("Model X", 55, 46, 7.9)
car4 = Car("Rock", 50, 45, 9.4)

Tebsla = [car1, car2, car3, car4]
print(car4.compare_cars(Tebsla))

print(car4.is_better_than(car1)) # Prints "yes"
print(car2.is_better_than(car3)) # Prints "no"
print(car1.is_better_than(car2)) # Prints "maybe"
