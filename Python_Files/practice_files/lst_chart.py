row1_content= ["  ", "mutable", "ordered", "slicing", "duplicate"]
row2_content = ["LIST", "yes", "yes", "yes", "yes"]
row3_content = ["TUPLE", "no", "yes", "yes", "yes"]
row4_content = ["SET", "yes", " no", "no", "no"]

x = row1_content
for i in x:
    for g in x:
      print(i, g, end=" ")

year = 2016

event = 'Referendum'

print(f'{year} {event}')

