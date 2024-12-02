class Smartphone:

    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.__battery_percentage = battery_percentage  # private attribute

    def make_call(self, number):
        return f"Calling...... {number}"

    def charge(self, charge_amount):
        if 0 < charge_amount <= 100:
            self.__battery_percentage = min(
                self.__battery_percentage + charge_amount, 100
            )
            return f"Charging complete. Battery is now at {self.__battery_percentage}%"
        else:
            return "Battery Full. Please Unplug"

    def get_battery_life(self):
        return self.__battery_percentage

    def __str__(self):
        return f"{self.brand} {self.model} with {self.__battery_percentage}% battery."


class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_percentage, camera_resolution):
        super().__init__(brand, model, battery_percentage)
        self.camera_resolution = camera_resolution

    def take_photo(self):
        return f"Taking a photo with {self.camera_resolution} MP camera."

    def __str__(self):
        return f"{super().__str__()} and a {self.camera_resolution}"


phone1 = Smartphone("Apple", "iphone 15", 80)
print(phone1)
print(phone1.charge(15))
print(phone1.make_call("+2547235689658"))
print(phone1.get_battery_life())

print("\n" * 2)
camera_phone = SmartphoneWithCamera("Samsung", "S24", 90, 108)
print(camera_phone)
print(camera_phone.take_photo)


class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚣"


def demonstrate_move(vehicle):
    print(vehicle.move())


car = Car()
plane = Plane()
boat = Boat()


demonstrate_move(car)
demonstrate_move(plane)
demonstrate_move(boat)
