a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b) # Union of two sets
print("Union:", c)
d = a.intersection(b) # Intersection of two sets
print("Intersection:", d)
e = a.difference(b) # Elements in a but not in b
print("Difference (a-b):", e)
f = b.difference(a) # Elements in b but not in a
print("Difference (b-a):", f)
g = a.symmetric_difference(b) # Elements in either a or b but not in both
print("Symmetric Difference:", g)
h = a.issubset(b) # Check if a is subset of b
print("Is a subset of b:", h)
i = a.issuperset(b) # Check if a is superset of b
print("Is a superset of b:", i)
j = a.isdisjoint(b) # Check if a and b have no elements in common
print("Are a and b disjoint:", j)
k = a.copy() # Shallow copy of set a
print("Copy of a:", k)
l = a.clear() # Clear all elements from set a
print("Cleared a:", a)