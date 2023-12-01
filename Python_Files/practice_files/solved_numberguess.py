

import random
import math


def screen_number(z):
    if z.isdigit():
         print(" ")

    else:
         print("Please use only numbers")
         quit()


a = input("upper?" )
b = input("lower?" )
screen_number(a)
screen_number(b)
c = int(a)
d = int(b)
comp_choice = random.randrange(d, c)
count = 1
e = round((c - d) / 12)
print("You have ", e, "guesses.")
z = int(0)

while count <= e:
 new = input("Pick a number  ")

 z = int(new)

 if e == count:
  print("Try Again")
  break

 elif z < comp_choice:
  print("too low")
  count += 1

 elif z > comp_choice:
  print("too high")
  count += 1

 elif z == comp_choice:
  print("YOU WIN")
  break





