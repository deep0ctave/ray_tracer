class Vector():

    def __init__(self,x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self._coords = (x, y, z)

    @property
    def x(self):
        return self._coords[0]
    @property
    def y(self):
        return self._coords[1]

    @property
    def z(self):
        return self._coords[2]

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __length__(self):
        return abs(self)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Unsupported operand type for +: 'Vector' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Unsupported operand type for -: 'Vector' and '{}'".format(type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Unsupported operand type for *: 'Vector' and '{}'".format(type(other).__name__))

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError("Unsupported operand type for /: 'Vector' and '{}'".format(type(other).__name__))