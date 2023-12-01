print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
]

for x in FLAVORS:
    print(x, 'x')
    for y in FLAVORS:
        if x < y:
            print(y, 'y')
           # print(x, y, sep=", ")

print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")           

for i in range(len(FLAVORS) - 1):
    for j in range(i + 1, len(FLAVORS)):
         print(FLAVORS[i] + " " + FLAVORS[j])

print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")


 