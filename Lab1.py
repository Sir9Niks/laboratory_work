import doctest


class Car:
    def __init__(self, power: float, cost: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param power: Мощность автомобиля
        :param cost: Стоимость автомобиля

        Примеры:
        >>> car = Car(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(power, (int, float)):
            raise TypeError("Мощность автомобиля должна быть типа int или float")
        if power <=0:
            raise ValueError("Мощность автомобиля не должна быть отрицательным числом")
        self.power = power

        if not isinstance(cost, (int, float)):
            raise TypeError("Стоимость должна быть int или float")
        if cost < 0:
            raise ValueError("Стоимость не может быть отрицательным числом")
        self.cost = cost

    def the_engine_is_missing(self) -> bool:
        """
        Функция которая проверяет, есть ли у автомобиля двигатель

        :return: Есть ли двигатель

        Примеры:
        >>> car = Car(500, 500)
        >>> car.the_engine_is_missing()
        """
        ...

    def add_a_chip(self, added_power: float) -> None:
        """
        Добавление мощности двигателю.
        :param added_power: Добавляемая мощность

        :return: Новая мощность автомобиля

        Примеры:
        >>> car = Car(500, 0)
        >>> car.add_a_chip(200)
        """
        if not isinstance(added_power, (int, float)):
            raise TypeError("Добавляемая мощность должна быть типа int или float")
        if added_power <= 0:
            raise ValueError("Добавляемая мощность должна быть положительным числом")


class City:
    def __init__(self, population: int, square: float):
        """
        Создание и подготовка к работе объекта "Город"

        :param population: Население города
        :param square: Площадь города

        Примеры:
        >>> city = City(500, 354)  # инициализация экземпляра класса
        """
        if not isinstance(population, (int)):
            raise TypeError("Население должно быть типа int")
        if population < 0:
            raise ValueError("Население города не должно быть отрицательным числом")
        self.population = population

        if not isinstance(square, (int, float)):
            raise TypeError("Площадь города должна быть int или float")
        if square <= 0:
            raise ValueError("Площадь города должна быть положительным числом")
        self.square = square

    def population_growth(self, population_gro: int):
        """
        Рост населения города.
        :param population_gro: Прирост населения

        :return: Актуальное население города

        Примеры:
        >>> city = City(500, 435)
        >>> city.population_growth(200)
        """
        if not isinstance(population_gro, (int)):
            raise TypeError("Прирост населения должен быть типа int")
        ...

    def increasing_the_area(self, area: float):
        """
        Увеличение площади города.
        :param area: Добавленная площадь

        :return: Актуальная площадь города

        Примеры:
        >>> city = City(500, 564)
        >>> city.population_growth(200)
        """
        if not isinstance(area, (int, float)):
            raise TypeError("Добавляемая площадь должна быть типа int или float")
        ...


class Tank:
    def __init__(self, capacity: float, fuel: float):
        """
        Создание и подготовка к работе объекта "Бак"

        :param capacity: Объем бака
        :param fuel: Количество топлива

        Примеры:
        >>> tank = Tank(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Объём бака должен быть типа int или float")
        if capacity <= 0:
            raise ValueError("Объём бака должен быть положительным числом")
        self.capacity = capacity

        if not isinstance(fuel, (int, float)):
            raise TypeError("Количество топлива должно быть int или float")
        if fuel < 0:
            raise ValueError("Количество топлива не может быть отрицательным числом")
        self.fuel = fuel

    def additional_tank(self, add_capacity: float):
        """
        Установка дополнительного бака
        :param add_capacity: Объем добавляемого бака

        :return: Общий объём баков

        Примеры:
        >>> tank = Tank(500, 564)
        >>> tank.additional_tank(200)
        """
        if not isinstance(add_capacity, (int, float)):
            raise TypeError("Объём дополнительного бака должен быть типа int или float")
        if add_capacity <= 0:
            raise ValueError("Объём дополнительного бака должен быть положительным числом")
        ...

    def refueling(self, new_fuel: float):
        """
        Заправка.
        :param new_fuel: Заправленное топливо

        :raise ValueError: Если заправленное топливо превышает объём баков, то вызываем ошибку

        :return: Актуальное количество топлива

        Примеры:
        >>> tank = Tank(500, 0)
        >>> tank.refueling(200)
        """
        if not isinstance(new_fuel, (int, float)):
            raise TypeError("Заправленное топливо должно быть типа int или float")
        if new_fuel < 0:
            raise ValueError("Заправленное топливо должно быть положительным числом")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
