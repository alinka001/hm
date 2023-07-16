class Car :
    def __init__(self, model, year, speed):
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, value) :
        self.speed += value

    def brake(self, value):
        self.speed -= value

    def get_speed(self):
        return self.speed
    

car = Car("g82", 2021, 160)
car.accelerate(40)
print(car.get_speed())
car.brake(100)
print(car.get_speed())
    
