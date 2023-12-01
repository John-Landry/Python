rows = 5
for i in range(rows + 1):
    for j in range(i):
      print(i, end=" ")
    print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(i):
      print(i, end=" ")
    print(" ")

x = 0
while (x < 20):
  x = x + 2
print(x)

x = 0
while (x < 20):
  print(x, end=" ")
  print(" start")
  x = x + 1
  print(x, end=" ")
  print(" -------------")
print(x)

x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)

x = 1
for x in range(2,5):
    y = x%2
    print(y)

for i in range(1,6,2):
    if (i==4):
        break
    print(i,end=" ")

    x = 'abcd'

    for i in range(x):
        print(i)