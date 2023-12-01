class Boat:

  def __init__(self):
      (self)
      print(self)
      print(type(self))
      print("--------")
      print("--------")

  def port_tack(self):
    print("I'm on port tack.")
    print(self)
    print(type(self))
    print("--------")
    print("--------")

  def starboard_tack(self):
    print("--------")
    print("I'm on starboard tack.")
    print(self)
    print(type(self))
    print("--------")
    print("--------")

boat1 = Boat()
print(type(boat1))
print(type(boat1))
boat1.starboard_tack()
boat1.port_tack()
