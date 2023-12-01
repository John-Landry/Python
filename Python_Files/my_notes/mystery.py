[print(2**x, end="  ") for x in range(10)]

print(f" \n ==============================")

x = set(range(0, 10))

for i in x:
  print(2**i, end="  ")

print(f" \n ==============================")

for num in range(1, 6):
    print(num, end="  ")

print("xxxxx\n".join(str(2**n)) for n in range(10))
