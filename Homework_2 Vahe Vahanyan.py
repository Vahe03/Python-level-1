# 1
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_noise(self):
        print("Makes noise")

    def fly(self):
        print("Flies")

    def walk(self):
        print("Walks")


class Bird(Animal):
    def __init__(self, name, color, can_fly=True):
        super().__init__(name, color)
        self.can_fly = can_fly

        def make_noise(self):
            super().make_noise()

        def fly(self):
            print("Fly")

        def walk(self):
            print("I'm too lazy to walk, I can only fly")


class Feline(Animal):
    def __init__(self, name, color, can_fly=False):
        super().__init__(name, color)
        self.can_fly = can_fly

        def make_noise(self):
            super().make_noise()

        def fly(self):
            print("I can't fly")

        def walk(self):
            print("Walk")


# 2
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


# 3
class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass


# 4
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return self.radius * 3.14 * 2

    def area(self):
        return 3.14 * (self.radius ** 2)


# 5
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def area(self):
        return self.width * self.length


# 6
class Triange(Shape):
    def __init__(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c

            def perimeter(self):
                return self.a + self.b + self.c

            def area(self):
                x = (self.a + self.b + self.c) / 2
                return x * (((x - a) * (x - b) * (x - c)) ** 0.5)

        else:
            raise TypeError


# 7
class Vehicle:
    def __init__(self, name, mileage, condition, price, max_speed, current_speed, engine_on=False):
        self.name = name
        self.mileage = mileage
        self.condition = condition
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.engine_on = engine_on

    def start_engine(self):
        pass

    def accelerate(self):
        pass

    def stop(self):
        pass


class ElectricVehicle(Vehicle):
    def __init__(self, name, mileage, condition, price, max_speed, current_speed, engine_on, driving_range,
                 charging_time):
        super().__init__(name, mileage, condition, price, max_speed, current_speed, engine_on)
        self.driving_range = driving_range
        self.charging_time = charging_time

    def start_engine(self):
        if self.current_speed < self.max_speed:
            self.engine_on = True
            print("Engine started")

    def accelerate(self):
        if self.engine_on == True:
            self.current_speed += 30
            print("Accelerated")

    def stop(self):
        self.current_speed = 0
        self.engine_on = False
        print("Stopped")


class PetrolVehicle(Vehicle):
    def __init__(self, name, mileage, condition, price, max_speed, current_speed, engine_on, engine, transmission,
                 num_of_gears, current_gear):
        super().__init__(name, mileage, condition, price, max_speed, current_speed, engine_on)
        self.engine = engine
        self.transmission = transmission
        self.num_of_gears = num_of_gears
        self.current_gear = current_gear

    def start_engine(self):
        if self.current_speed < self.max_speed:
            self.engine_on = True
            print("Engine started")

    def accelerate(self):
        if self.engine_on == True:
            self.current_speed += 30
            print("Accelerated")
            if self.transmission == "Manual" and self.current_gear < self.num_of_gears:
                self.current_gear += 1
                print("Gear changed")

    def stop(self):
        self.current_speed = 0
        self.engine_on = False
        if self.transmission == "Manual":
            self.current_gear = 0
            print("Gear changed")
        print("Stopped")


bmw = PetrolVehicle("bmw", 100000, "good", 12000, 220, 0, False, 2.5, "Manual", 8, 0)
bmw.start_engine()
bmw.accelerate()
bmw.stop()

tesla = ElectricVehicle("Tesla", 70000, "good", 25000, 260, 0, False, 150, "6 hours")
tesla.start_engine()
tesla.accelerate()
tesla.stop()