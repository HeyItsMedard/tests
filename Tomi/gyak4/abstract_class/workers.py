class Worker:
    def __init__(self, name, address, hourly_rate):
        self.name = name
        self.address = address
        self.hourly_rate = hourly_rate

    def show_profile(self):
        print("Name", self.name)
        print("Address", self.address)
        print("Hourly rate", self.hourly_rate)

    def calculator(self, hours = 40):
        return self.hourly_rate * hours

class Manager(Worker):
    def __init__(self, name, address, hourly_rate, hourly_bonus):
        super.__init__(name, address, hourly_rate)
        self.hourly_bonus = hourly_bonus

    def calculator(self, hours=40):
        return (self.hourly_bonus + self.hourly_rate) * hours


w = Manager('Asd', '123', 10, 0)
