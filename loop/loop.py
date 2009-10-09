# Loop
from math import *
from visual import *

# x = x_c - r * cos(angle)
# y = y_c - r * sin(angle)

def circle(angle, (x_c, x_y), radius):
    """
    Gives a <angle> part of a circle created with faces
    from VPython.
    """

    f = frame()

    # 3 points to a triangle, 2 triangles per square, 2 sides to a square = 12
    multiplier = 12
    model = faces(pos = zeros( (multiplier*angle, 3), float))

    current_angle = 0

    x_this, x_next = 0
    y_this, y_next = 0

    z_a = 5
    z_b = -5

    for i in arange(angle):
        rad = radians(i)
        rad_next = radians(i+1)

        x_this = x_c - radius * cos(rad)
        x_next = x_c - radius * cos(rad_next)
        y_this = y_c - radius * sin(rad)
        y_next = y_c - radius * sin(rad_next)

        model.pos[angle*multiplier + 0] = (x_this, y_this, z_a)
        model.pos[angle*multiplier + 1] = (x_this, y_this, z_b)
        model.pos[angle*multiplier + 2] = (x_next, y_next, z_b)
        model.pos[angle*multiplier + 3] = (x_next, y_next, z_a)
        model.pos[angle*multiplier + 4] = (x_next, y_next, z_b)
        model.pos[angle*multiplier + 5] = (x_this, y_this, z_a)

    return (f, model)

print circle(0)
