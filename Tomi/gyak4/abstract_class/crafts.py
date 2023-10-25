class Vehicle:
  def __init__(self, make, model, color):
    self.make = make
    self.model = model
    self.color = color

  def start(self):
    print("Starting engine")

  def stop(self):
    print('Stopping engine')

  def show_tech_data(self):
    print('Make: ', self.make)
    print('Model: ', self.model)
    print('Color: ', self.color)

class Car(Vehicle):
  def drive(self):
    print('Driving on the road')

class Aircraft(Vehicle):
  def fly(self):
    print('Flying in the sky')


class FlyingCar(Car, Aircraft):
  pass

fc = FlyingCar('Space', 'Falcon', 'black')
fc.start()
fc.fly()
fc.drive()
fc.stop()
