class Body:
  def __init__(self):
    self.rotation = 0

  def rotate_left(self, degree):
    self.rotation -= degree
    print(f'Rotating body left {degree}°')

  def rotate_right(self, degree):
    self.rotation += degree
    print(f'Rotating body right {degree}°')

class Arm:
  def __init__(self):
    self.rotation = 0

  def rotate_left(self, degree):
    self.rotation -= degree
    print(f'Rotating arm left {degree}°')

  def rotate_right(self, degree):
    self.rotation += degree
    print(f'Rotating arm right {degree}°')


class Robot:
  def __init__(self):
    self.body = Body()
    self.arm = Arm()

  def rotate_body_left(self, degree=90):
    self.body.rotate_left(degree)

  def rotate_arm_left(self, degree=45):
    self.arm.rotate_left(degree)

  def rotate_body_right(self, degree=90):
    self.body.rotate_right(degree)

  def rotate_arm_right(self, degree=45):
    self.arm.rotate_right(degree)

  def rotate_arm_and_body_left(self, degree):
    self.body.rotate_left(degree)
    self.arm.rotate_left(degree)

  def rotate_arm_and_body_right(self, degree):
    self.body.rotate_right(degree)
    self.arm.rotate_right(degree)

robi = Robot()

robi.rotate_arm_left()
robi.rotate_body_left()
