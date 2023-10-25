class Vehicles:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._started = False

    def start(self):
        print('Starting engine')
        self._started = True

    def stop(self):
        print('Stopping engine')
        self._started = False

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicles):
    def __init__(self, make, model, year, seat_number):
        super().__init__(make, model, year)
        self.seat_number = seat_number

    def drive(self):
        print(f'Driving {self.make} car with {self.seat_number} seats')


class Motorcycle(Vehicles):
    def __init__(self, make, model, year, wheel_count):
        super().__init__(make, model, year)
        self.wheel_count = wheel_count

    def drive(self):
        print(f'Riding my {self.make} cycle with {self.wheel_count} wheels.')

auto = Car('Tesla', 'X', 2020, 4)
cycle = Motorcycle('Harley', '12', 1980, 2)
auto.start()
auto.drive()
auto.stop()

cycle.start()
# cycle.ride()
cycle.stop()

def drive_a_vehicle(v: Vehicles):
    v.drive()

drive_a_vehicle(cycle)
