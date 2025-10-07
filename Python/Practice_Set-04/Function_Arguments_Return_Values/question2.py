'''
Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

Both length and width
Only length (use default width)
'''
def calculate_area(length, width=10):
    return length * width

area1 = calculate_area(13, 20)  
area2 = calculate_area(13)     

print(f"Area of rectangle with length 5 and width 4: {area1}")
print(f"Area of rectangle with length 5 and default width: {area2}")