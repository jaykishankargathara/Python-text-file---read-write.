"""
name = ["jk", "jay kay", "Jaykishan"]
for x in name:
        print (x)

name = ['jk', 'jay kay', 'jaykishan']
for x in 'jay kay':
    print (x)

name = ['jk', 'jay kay', 'jaykishan']
for x in name:
    print (x)
    if x == 'jay kay':
        break

name = ['jk', 'jay kay', 'jaykishan']
for x in name:
    if x == 'jay kay':
        break
    print (x)

name = ['jk', 'jay kay', 'jaykishan']
for x in name:
    if x == 'jay kay':
        continue
    print (x)

for x in range(5):
    print (x)

for x in range (1, 5):
    print (x)

for x in range (1, 10, 2):
        print (x)

for x in range (5):
        print (x)
else:
        print ("Five numbers found")
"""

name = ['jaykishan', 'jay kay', 'jk']
age = [26,25,24]
for x in name:
    for y in age:
        print (x,y)