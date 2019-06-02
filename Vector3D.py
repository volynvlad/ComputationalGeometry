import math


class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def set_Vector3D_by_coord(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set_Vector3D_by_Point3D(self, p):
        self.x = p.x
        self.y = p.y
        self.z = p.z

    def set_Vector3D_by_Point3Ds(self, p1, p2):
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y
        self.z = p2.z - p1.z

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def norm(self):
        x = self.x / int(self.length())
        y = self.y / int(self.length())
        z = self.z / int(self.length())
        return Vector3D(x, y, z)

    def vect_prod(self, v):        
        x = self.y * v.z - self.z * v.y
        y = self.z * v.x - self.x * v.z
        z = self.x * v.y - self.y * v.x
        return Vector3D(x, y, z)

    def vect_mult(self, num):
        return Vector3D(self.x * num, self.y * num, self.z * num)



