marks = [5, 2, 21, 5, 7]
extra_marks = [45, 67, 89]
print(marks)

marks.append(63)  # adds 63 to the end of the list
marks.pop()     # removes the last element from the list
marks.sort()    # sorts the list in ascending order
marks.reverse() # reverses the list
marks.insert(2, 23) # inserts 23 at index 2
marks.remove(23) # removes the first occurrence of 23
marks.count(5) # counts the number of occurrences of 5
marks.index(5) # returns the index of the first occurrence of 5
marks.extend(extra_marks) # extends the list by adding elements from another list
marks.clear() # clears the list
marks.copy() # returns a shallow copy of the list

print(marks)