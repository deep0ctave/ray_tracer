from vector import Vector

class Color(Vector):

    def __init__(self, r, g, b):
        super().__init__(r, g, b)

    def __repr__(self):
        return f"Color({self.x}, {self.y}, {self.z})"

    def write_color(self):
        r = int(self.x * 255)
        g = int(self.y * 255)
        b = int(self.z * 255)
        return f"{r} {g} {b}"    