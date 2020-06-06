class Vehicle:
    """Класс Vehicle используется для описания транспортного средства

            Основное применение - создание объекта транспортного средства.

            Attributes
            ----------

            model : str
                модель поезда
            fuel_type : str
                тип двигателя
            weight : int
                масса транспортного средства (кг)
            length : int
                длина транспортного средаства (м)

            Methods
            -------
            get_distance_traveled(speed_travel, driving_time)
                Возвращает пройденное расстояние (m)

                speed_travel - скорость движения (км/ч)
                driving_time - время (мин)
        """

    def __init__(self, model, fuel_type=None, weight=None, length=None):
        self.model = model
        self.fuel_type = fuel_type
        self.weight = weight
        self.length = length

    def __str__(self):
        return f"{self.model}, {self.fuel_type}"

    @classmethod
    def get_distance_traveled(cls, speed_travel, driving_time):
        return speed_travel * driving_time


class Locomotive(Vehicle):
    pass


class Wagon(Vehicle):
    pass


class Train(Vehicle):

    """Класс Train используется для описания поезда

        Основное применение - создание объекта поезда
        по указанному разделителю.

        Attributes
        ----------

        wagon : object
            обьект вагона
        locomotive : object
            обьект локоматива
        number_passengers: int
            количество пассажиров
        number_wagons: int
            количество вагонов

        Methods
        -------
        get_weight()
            Возвращает вес поезда
        get_length()
            Возвращает длину поезда
        """

    average_person_weight = 80

    def __init__(self, model, fuel_type,
                 wagon,
                 locomotive,
                 number_passengers,
                 number_wagons):
        super().__init__(model, fuel_type)
        self.wagon = wagon
        self.locomotive = locomotive
        self.number_wagons = number_wagons
        self.number_passengers = number_passengers

    @property
    def total_weight_passengers(self):
        return self.number_passengers * self.average_person_weight

    @property
    def total_weight_wagons(self):
        return self.wagon.weight * self.number_wagons

    @property
    def total_wagon_length(self):
        return self.wagon.length * self.number_wagons

    def get_weight(self):
        return self.locomotive.weight + self.total_weight_passengers + self.total_weight_wagons

    def get_length(self):
        return self.locomotive.length + self.total_wagon_length


class Plane(Vehicle):

    """Класс Plane используется для описания самолета

        Основное применение - создание объекта самолета
        по указанному разделителю.

        Attributes
        ----------

        flight_range : int
            дальность полета (км)
        number_passengers : int
            количество пассажиров
        fuel_consumption: int
            масса расходуемого в течении полета топлива (кг)
        take_off_mass: int
            взлетная масса самолета (кг)

        Methods
        -------
        get_fuel_efficiency()
            Возвращает показатель топливной эффективности
        get_weight_efficiency()
            Возвращает показатель весовой эффективности
    """

    def __init__(self, model, fuel_type,
                 flight_range,
                 number_passengers,
                 fuel_consumption,
                 take_off_mass):

        super().__init__(model, fuel_type)
        self.flight_range = flight_range
        self.number_passengers = number_passengers
        self.fuel_consumption = fuel_consumption
        self.take_off_mass = take_off_mass

    def get_fuel_efficiency(self):
        fuel_efficiency = self.flight_range * (self.fuel_consumption / self.number_passengers)
        return fuel_efficiency

    def get_weight_efficiency(self):
        weight_efficiency = self.take_off_mass / self.number_passengers
        return weight_efficiency


if __name__ == "__main__":

    locomative = Locomotive('GH-2020', 13870, 24000)
    wagon = Wagon('SD-5', 23000, 12870)

    train = Train('KM-2516556651', 'diesel', wagon, locomative, 420, 5)
    print(train.get_distance_traveled(1000, 60))

    plane = Plane('Boeing 777', 'jet', 1852, 250, 9100, 49900)
    print(plane.get_fuel_efficiency())
    print(plane.get_weight_efficiency())
    print(plane.get_distance_traveled(654.51, 5464))
