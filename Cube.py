import math
from Quanterion import Quanterion




def rotate(vector, point):
    vector = vector.norm()
    rotate_angle = math.pi / 70
    
    q_re = math.cos(rotate_angle / 2)
    q_x  = vector.x * math.sin(rotate_angle / 2)
    q_y  = vector.y * math.sin(rotate_angle / 2)
    q_z  = vector.z * math.sin(rotate_angle / 2)
    
    quant_vect = Quanterion(q_re, q_x, q_y, q_z)

    p_re = 0
    p_x  = point.x 
    p_y  = point.y
    p_z  = point.z

    quant_point = Quanterion(p_re, p_x, p_y, p_z)

    tmp_quant = quant_vect.mult(quant_point)
    new_quant = tmp_quant.mult(quant_vect.reverse())
    point.x = new_quant.i
    point.y = new_quant.j
    point.z = new_quant.k

class Cube:
    def __init__(self, point, v1, v2, length): 
        v1 = v1.norm()
        v2 = v2.norm()

        v1 = v1.vect_mult(length)
        v2 = v2.vect_mult(length)

        v3 = v1.vect_prod(v2).vect_divide(length) 

        p1 = point.add_Vector3D(v1)
        p2 = point.add_Vector3D(v2)
        p3 = point.add_Vector3D(v3)
        
        p4 = p2.add_Vector3D(v1)
        p5 = p2.add_Vector3D(v3)
        p6 = p1.add_Vector3D(v3)
        p7 = p4.add_Vector3D(v3)
    
        self.points = [point, p1, p2, p3, p4, p5, p6, p7]    
    
    def rotate(self, vector):
        for point in self.points:
            rotate(vector, point)

    def get_sides(self):
        return [
                [self.points[0], self.points[1]],
                [self.points[0], self.points[2]],
                [self.points[0], self.points[3]],

                [self.points[1], self.points[4]],
                [self.points[1], self.points[6]],

                [self.points[2], self.points[4]],
                [self.points[2], self.points[5]],

                [self.points[3], self.points[6]],
                [self.points[3], self.points[5]],

                [self.points[4], self.points[7]],

                [self.points[5], self.points[7]],

                [self.points[6], self.points[7]],
                ]
    
    def print_Cube(self):
        print(self.points[0].get_Point3D(), self.points[1].get_Point3D(), self.points[2].get_Point3D(), self.points[3].get_Point3D(),
              self.points[4].get_Point3D() ,self.points[5].get_Point3D(), self.points[6].get_Point3D(), self.points[7].get_Point3D())

