# Loop
from math import *
from visual import *


def circle(angle, (x_c, y_c), radius, width, z_begin, z_end):
    """
    Gives a <angle> part of a circle created with faces
    from VPython.
    """
    def uvect(origin, mid):
        """
        Calculates a unit vector from the <origin> (a vertice
        on the circle) to the <mid> of the circle
        """
        vec = mid - origin
        vec.mag = 1
        return vec

    z_displacement = float(z_end) - float(z_begin)
    z_delta = z_displacement / float(angle)

    mid = vector(x_c, y_c)

    f = frame()

    z_a = z_begin + width / 2.
    z_b = z_begin - width / 2.

    positions = []
    normals = []

    rad_n = radians(0)
    x_rn  = x_c + cos(rad_n) * (radius)
    y_rn  = y_c + sin(rad_n) * (radius)
 
    for i in range(angle):
        rad = rad_n
        x_r = x_rn
        y_r = y_rn

        z_a = z_a + z_delta
        z_b = z_b + z_delta
     
        rad_n = radians(i + 1)
        x_rn  = x_c + cos(rad_n) * (radius)
        y_rn  = y_c + sin(rad_n) * (radius)

        corner_1 = vector(x_r,  y_r,  z_b)
        corner_2 = vector(x_r,  y_r,  z_a)
        corner_3 = vector(x_rn, y_rn, z_b)
        corner_4 = vector(x_rn, y_rn, z_a)

        # Front
        positions.extend([corner_1,
                          corner_2,
                          corner_4])
        positions.extend([corner_4,
                          corner_3,
                          corner_1])

        # Back
        positions.extend([corner_1,
                          corner_4,
                          corner_2])
        positions.extend([corner_1,
                          corner_3,
                          corner_4])

        # Normals
        normals.extend([uvect(corner_1, mid),
                        uvect(corner_2, mid),
                        uvect(corner_4, mid),
                        uvect(corner_4, mid),
                        uvect(corner_3, mid),
                        uvect(corner_1, mid),
                        uvect(corner_1, mid),
                        uvect(corner_4, mid),
                        uvect(corner_2, mid),
                        uvect(corner_1, mid),
                        uvect(corner_3, mid),
                        uvect(corner_4, mid)])

    z_curmid = (z_a + z_b) / 2.

    model = faces(pos = positions, normal = normals, frame = f)

    return (f, model, z_curmid)
