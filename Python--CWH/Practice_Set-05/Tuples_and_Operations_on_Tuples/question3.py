# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

t = (1, 2, 3, 4, 5)

temp_list = list(t)

temp_list[0] = 50

t = tuple(temp_list)
print(t)  
