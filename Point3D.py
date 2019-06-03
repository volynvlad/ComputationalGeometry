

class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def add_Vector3D(self, v):
        return Point3D(self.x + v.x, self.y + v.y, self.z + v.z)

    def get_Point3D(self):
        return [self.x, self.y, self.z]

