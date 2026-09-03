from vector import Vector

class Ray():

    def __init__(self, origin: Vector, direction: Vector):
        self.origin = origin
        self.direction = direction.normalize()

    def at(self, t: float) -> Vector:
        return self.origin + self.direction * t

    def __repr__(self):
        return f"Ray(origin={self.origin}, direction={self.direction})"