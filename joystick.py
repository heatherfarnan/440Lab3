from PCF8591 import PCF8591

class joystick:

  def __init__ (self, address):
    self.PCF = PCF8591(address)

  def getX(self):
    return self.PCF.read(0)

  def getY(self):
    return self.PCF.read(1)