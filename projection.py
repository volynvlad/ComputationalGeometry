def central_projection(cube_sides, cent_point):
    lines = []
    for cube_side in cube_sides:
        
        x1 = (cube_side[0].x - cent_point.x) * ((cube_side[0].z - cent_point.z) / cube_side[0].z)
        y1 = (cube_side[0].y - cent_point.y) * ((cube_side[0].z - cent_point.z) / cube_side[0].z)
        x2 = (cube_side[1].x - cent_point.x) * ((cube_side[1].z - cent_point.z) / cube_side[1].z)
        y2 = (cube_side[1].y - cent_point.y) * ((cube_side[1].z - cent_point.z) / cube_side[1].z)
        """ 
        x1 = (cube_side[0].x * cent_point.z - cube_side[0].z * cent_point.x) / (cent_point.z - cube_side[0].z)
        y1 = (cube_side[0].y * cent_point.z - cube_side[0].z * cent_point.y) / (cent_point.z - cube_side[0].z)
        x2 = (cube_side[1].x * cent_point.z - cube_side[1].z * cent_point.x) / (cent_point.z - cube_side[1].z)
        y2 = (cube_side[1].y * cent_point.z - cube_side[1].z * cent_point.y) / (cent_point.z - cube_side[1].z)
        """
        lines.append([[x1, y1], [x2, y2]])

    return lines
