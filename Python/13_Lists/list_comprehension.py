# Create a list containing a table of 5

a = 5
table = []

for i in range(1, 11):
    table.append(5 * i)
    
print(table)
# Using List Comprehension
table_comp = [5 * i for i in range(1, 11)]
print(table_comp)
