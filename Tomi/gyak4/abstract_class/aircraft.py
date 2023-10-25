class Aircraft:
    def __init__(self, thrust, lift, max_speed):
        self.thrust = thrust
        self.lift = lift
        self.max_speed = max_speed

    def show_technical_data(self):
        print('Thrust:', self.thrust)
        print('Lift:', self.lift)
        print('Max speed:', self.max_speed)

class Helicopter(Aircraft):
    def __init__(self, thrust, lift, max_speed, num_rotors):
        super().__init__(thrust, lift, max_speed)
        self.num_rotors = num_rotors

    def show_technical_data(self):
        super().show_technical_data()
        print('Num of rotors', self.num_rotors)

h = Helicopter(1000, 100, 20, 2)
h.show_technical_data()
