# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
coordinates = (4, 5)
print(coordinates)
coordinates[0] = 50  # TypeError: 'tuple' object does not support item assignment
