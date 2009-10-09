# -*- coding: cp1252 -*-
from visual import *
from math import *


def showaxes(length):
    axiswidth = length / 100
    axis_x = arrow(pos = (0,0,0), axis = (length,0,0), shaftwidth = axiswidth, color = color.red)
    axis_y = arrow(pos = (0,0,0), axis = (0,length,0), shaftwidth = axiswidth, color = color.blue)
    axis_z = arrow(pos = (0,0,0), axis = (0,0,length), shaftwidth = axiswidth, color = color.green)

# Initial setup
set_angle = 10
angle = radians(-1*set_angle)
direction = vector(cos(angle), sin(angle), 0)
distO = 100

# Resistance factor in m/s^2
resistance_factor = 0

slope_length = 1000
slope_width = slope_length / 10
slope_thickness = slope_length / 100

falling_size = slope_width / 3

# Scene setup
scene.title = 'Skråt fald'
scene.height = scene.width = 800
scene.forward = (-4,-3,-6)
scene.center = (slope_length / 15, slope_length / 6, 0)
scene.range = (slope_length * 5/6, slope_length * 5/6, slope_length * 5/6)

# Show the x-, y- and z-axis
showaxes(100)

# The slope

slope_pos = vector(distO,distO,distO)


slope = box(pos = slope_pos,
            length = slope_length,
            height = slope_thickness,
            width = slope_width)

slope.rotate(angle = angle,
           axis = (0,0,1),
           origin = slope_pos)

# The falling box http://vpython.org/contents/docs/visual/rotation.html
if set_angle*-1 < 0:
    falling_pos = vector(distO - slope_length/2 + falling_size/2,
                         distO + slope_thickness/2 + falling_size/2,
                         distO)
else:
    falling_pos = vector(distO + slope_length/2 - falling_size/2,
                         distO + slope_thickness/2 + falling_size/2,
                         distO)

falling_thing = box(pos = falling_pos,
                    length = falling_size,
                    height = falling_size,
                    width = falling_size)
falling_thing.rotate(angle = angle,
                     axis = (0,0,1),
                     origin = slope_pos)

# Gravity
g = -9.8

# The gravity split up along our slope-vectors
d_x = g * cos(angle + pi)
d_y = g * sin(angle + pi)

dt = 0.001
slowness = 0.1

# Set resistance
resistance = vector(cos(angle + pi), sin(angle + pi),0) * resistance_factor

# Calculate acceleration
if (abs(set_angle) < 90):
    accel = vector(d_x, d_y, 0) * sin(abs(angle)) * slowness
    if accel.y + resistance.y * slowness < 0:
        accel = accel + resistance * slowness
    else:
        accel = vector(0,0,0)
else:
    accel = vector(0,g,0) * slowness

# Calculate speed
speed = accel * dt

initial_falling_pos_y = falling_thing.pos.y

while initial_falling_pos_y - abs(slope_length * sin(angle)) < falling_thing.pos.y:
    rate(1/dt)
    if set_angle*-1 < 0:
        falling_thing.pos = falling_thing.pos + speed
    else:
        falling_thing.pos = falling_thing.pos - speed
    ds = accel*dt
    speed = speed + ds
