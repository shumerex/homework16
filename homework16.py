class Car:
    def __init__(self):
        self.price = 1000000


    def horse_powers(self):
        return "Неуказано количество лошадиных сил"


class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 1500000


    def horse_powers(self):
        return "300 лошадиных сил"


class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price = 1200000

    def horse_powers(self):
        return "250 лошадиных сил"


if __name__ == "__main__":
    car = Car()
    print(f"Цена базового автомобиля: {car.price}")
    print(f"Количество лошадиных сил базового автомобиля: {car.horse_powers()}")

    nissan_car = Nissan()
    print(f"Цена автомобиля Nissan: {nissan_car.price}")
    print(f"Количество лошадиных сил автомобиля Nissan: {nissan_car.horse_powers()}")

    kia_car = Kia()
    print(f"Цена автомобиля Kia: {kia_car.price}")
    print(f"Количество лошадиных сил автомобиля Kia: {kia_car.horse_powers()}")