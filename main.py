from joystick import joystick
import time

j = joystick(0x48)

while True:
  print("{},\t{}" .format(j.getX(), j.getY()))
  time.sleep(.1)