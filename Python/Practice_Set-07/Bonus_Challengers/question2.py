# Implement __add__ in a Vector class so that adding two Vector objects returns a new Vector with summed components.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Adds the corresponding components of two vectors
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Example usage
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2   # Calls v1.__add__(v2)
print(v3)      # Output: Vector(4, 6)