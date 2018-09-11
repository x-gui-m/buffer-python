import math


def azimuthAngle (x1, y1, x2, y2):
    angle = 0.0
    dx = x2 - x1
    dy = y2 - y1
    if x2 == x1:
        angle = math.pi / 2.0
        if y2 == y1:
            angle = 0.0
        elif y2 < y1:
            angle = 3.0 * math.pi / 2.0
    elif y2 == y1:
        angle = math.pi
    elif x2 > x1 and y2 > y1:
        angle = 2.0 * math.pi - math.atan(dy / dx)
    elif x2 > x1 and y2 < y1:
        angle = math.atan(-dy / dx)
    elif x2 < x1 and y2 < y1:
        angle = math.pi - math.atan(dy / dx)
    elif x2 < x1 and y2 > y1:
        angle = math.pi + math.atan(dy / -dx)
    #return angle * 180 / math.pi
    return angle


#print(azimuthAngle(-20,-100,42,40))