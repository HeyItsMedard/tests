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
  def __init__(self, body, arm):
    self.body = body
    self.arm = arm

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

  def change_arm(self, arm):
    self.arm = arm

arm = Arm()
body = Body()

robi = Robot(body, arm)

robi.rotate_arm_left()
robi.rotate_body_left()

new_arm = Arm()
robi.change_arm(new_arm)
